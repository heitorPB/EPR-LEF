//18/11/2016 13:53 

#include <Arduino.h>
#include <Wire.h>
#include <stdlib.h>
// external libraries
#include <Nanoshield_ADC.h>
#include <SoftReset.h>
#include <SoftwareSerial.h>
//#include <WString.h>

const int channel_x = 1;
const int channel_b = 2;

const int pinLed13  = 13;

const int start_r = 2;
const int stop_r = 3;

const int temp_A = 4;
const int temp_B = 5;

const int campo_A = 6;
const int campo_B = 7;


Nanoshield_ADC adc;
SoftwareSerial mySerial(10, 11); // RX, TX

void setup()
{
	adc.begin();
	Serial.begin(115200);
        mySerial.begin(9600);
        delay(2000);
        
	while (!Serial);

        pinMode(start_r, OUTPUT);
        pinMode(stop_r,OUTPUT);
        
        pinMode(temp_A, OUTPUT);
        pinMode(temp_B, OUTPUT);
        
        pinMode(campo_A, OUTPUT);
        pinMode(campo_B, OUTPUT);
        
        delay(1000);
        
        digitalWrite(start_r, LOW);
        
        digitalWrite(stop_r, HIGH);
        delay(7);
        digitalWrite(stop_r, LOW);
        
        digitalWrite(temp_A, LOW);
        digitalWrite(temp_B, LOW);
        
        digitalWrite(campo_A, LOW);
        digitalWrite(campo_A, LOW);
        
	pinMode(pinLed13, OUTPUT);

	analogReference(DEFAULT);
        while (mySerial.available() > 0)
          Serial.print(mySerial.read());
        //mySerial.flush();
        mySerial.print("W0\r");
        adc.setGain(GAIN_EIGHT);
}


void loop()
{
	int opcao = 100;
	int media = 1;
	int i;
	double x;
	double y;
        double b;
	char result[20];
        int merda;
        int tempo_aux = 0;
        int campo_aux = 0;
        char aux_y[11];
        int j;

	if (Serial.available() > 0) {
		opcao = Serial.read();

		switch(opcao) {
		case 'A':
			/*while(Serial.peek() < 0);
			media = Serial.parseInt();*/
			ret1:
				if (Serial.available() > 0)
					media = Serial.parseInt();
				else
					goto ret1;

			opcao = 100;
                        //Serial.println(media);
			break;

		case 'B':
			// TODO separar isso aqui em duas funcoes. Ou Nao.
			// pode nao ser uma boa ideia por questao de tempo
			// de medida.
                        // FIXME primeira leitura do lockin nao funciona
			digitalWrite(pinLed13, HIGH);
                        //while (mySerial.available() > 0)
                          //    merda = mySerial.read();
			x = 0;
			y = 0;
                        b = 0;
			for(i = 0; i < media; i++){
				x += 2*adc.readVoltage(channel_x);
                                b += adc.readVoltage(channel_b);  
                                mySerial.print("q\r");
                                //delay(1);
                                j = 0;
                                while(mySerial.available() > 0 && j < 20){
                                  aux_y[j]= mySerial.read();
                                  j++;
                                }
                                //Serial.print("\nj: ");
                                //Serial.println(j);
                                //for (int k = 0; k < j; k++)
                                  //Serial.print(aux_y[k]);
                                //Serial.println("");
				y += atof(aux_y);
			}
			x /= (double) media;
			y /= (double) media;
                        b /= (double) media;

			dtostrf(x, 3, 6, result);
			Serial.write('x');
			Serial.print(strlen(result));
			Serial.print(result);
			Serial.write('X');

			dtostrf(y, 4, 10, result);
			Serial.write('y');
			Serial.print(strlen(result));
			Serial.print(result);
			Serial.write('Y');

                        dtostrf(b, 3, 6, result);
			Serial.write('b');
			Serial.print(strlen(result));
			Serial.print(result);
			Serial.write('B');


			digitalWrite(pinLed13, LOW);
			opcao = 100;
			break;

		case 'C':
			opcao = 100;
			soft_restart();
			break;

		case 'Z':
			opcao = 100;
			mySerial.print("z\r");
                        break;
                        
                case 'I':
                        opcao = 100;
                        digitalWrite(start_r, HIGH);
                        delay(10);
                        digitalWrite(start_r, LOW);
                        break;
                                  
                case 'P':
                        opcao = 100;
                        digitalWrite(stop_r, HIGH);
                        delay(10);
                        digitalWrite(stop_r, LOW);
                        break;
                // selecao de Tempo
                // 0 - 0.5 min
                // 1 - 1   min
                // 2 - 3   min
                // 3 - 5   min
                case 'T':
                        opcao = 100;
                        while(Serial.peek() < 0);
			tempo_aux = Serial.read();
			Serial.write('t');
			Serial.write(tempo_aux);
			Serial.write('T');

                        switch(tempo_aux) {
                              case '1':
                                    digitalWrite(temp_B, LOW);
                                    digitalWrite(temp_A, HIGH);
                                    break;
                                    
                              case '2':
                                    digitalWrite(temp_B, HIGH);
                                    digitalWrite(temp_A, LOW);
                                    break;
                                    
                               case '3':
                                    digitalWrite(temp_B, HIGH);
                                    digitalWrite(temp_A, HIGH);
                                    break;
                              case '0':
                              default:
                                    digitalWrite(temp_B, LOW);
                                    digitalWrite(temp_A, LOW);
                                    break;
                                    
                        }
                        break;
                // Selecao de delta B
                // 0 - 50   gauss
                // 1 - 100  gauss
                // 2 - 500  gauss
                // 3 - 1000 gauss
                case 'D':
                        opcao = 100;
                        while(Serial.peek() < 0);
			campo_aux = Serial.read();
			Serial.write('d');
			Serial.write(campo_aux);
			Serial.write('D');

                        switch(campo_aux) {
                              case '1':
                                    digitalWrite(campo_B, LOW);
                                    digitalWrite(campo_A, HIGH);
                                    break;
                                    
                              case '2':
                                    digitalWrite(campo_B, HIGH);
                                    digitalWrite(campo_A, LOW);
                                    break;
                                    
                               case '3':
                                    digitalWrite(campo_B, HIGH);
                                    digitalWrite(campo_A, HIGH);
                                    break;
                              case '0':
                              default:
                                    digitalWrite(campo_B, LOW);
                                    digitalWrite(campo_A, LOW);
                                    break;
                        }
                        break;                      
                
		default:
			opcao = 100;
		}
	}
}
