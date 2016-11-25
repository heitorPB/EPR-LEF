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
const int channel_y = 0;
const int pinLed13  = 13;


Nanoshield_ADC adc;
SoftwareSerial mySerial(10, 11); // RX, TX

void setup()
{
	adc.begin();
	Serial.begin(9600);
        mySerial.begin(9600);
        delay(2000);
        
	while (!Serial);

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
	long media = 5;
	int i;
	double x;
	double y;
	char result[20];
        char merda;
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
			for(i = 0; i < media; i++){
				x += adc.readVoltage(channel_x);

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

		default:
			opcao = 100;
		}
	}
}
