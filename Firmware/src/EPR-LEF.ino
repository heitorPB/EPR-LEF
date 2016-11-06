#include <Arduino.h>
#include <Wire.h>
// external libraries
#include <Nanoshield_ADC.h>
#include <SoftReset.h>


const int channel_x = 0;
const int channel_y = 1;
const int pinLed13  = 13;


Nanoshield_ADC adc;


void setup()
{
	adc.begin();
	Serial.begin(115200);
	while (!Serial);
	pinMode(pinLed13, OUTPUT);
	analogReference(DEFAULT);
}


void loop()
{
	int opcao = 100;
	int media = 5;
	int i;
	
	/*float x;
	float y;
	int RESH;
	int RESL;
	byte *data_x;
	byte *data_y;*/
	
	//char lixo;
	static double x;
	static double y;
	char result_x[9], result_y[9];

	if (Serial.available() > 0) {
		opcao = Serial.read();

		switch(opcao) {
		case 'A':
			// TODO deixar esse case decente
			/*ret1:
			if (Serial.available() > 0)
				media = Serial.parseInt();
			else
				goto ret1;
			*/
			while(Serial.peek() == -1);
			media = Serial.parseInt();
			opcao=100;
			break;

		case 'B':
			// TODO separar isso aqui em duas funcoes. Ou Nao.
			// pode nao ser uma boa ideia por questao de tempo
			// de medida.
			// TODO fazer um esquema de comunicacao decente,
			// cf github.com/heitorPB/arduino-temp-logger
			digitalWrite(pinLed13, HIGH);

			x = 0;
			y = 0;
			for(i = 0; i < media; i++){
				x += adc.readVoltage(channel_x);
				y += adc.readVoltage(channel_y);
				delay(2);
			}
			x /= media;
			y /= media;
			
			dtostrf(x, 8, 4, result_x);
			dtostrf(y, 8, 4, result_y);
			
			Serial.write('x');
			Serial.print(strlen(result_x));
			Serial.print(result_x);
			Serial.white('X');

			Serial.write('y');
			Serial.print(strlen(result_y));
			Serial.print(result_y);
			Serial.write('Y');
			
			//Ou a passagem de dados pode ser feita assim:
			//Dessa maneira passa sempre 6 bytes.
			//o primeiro identifica a coordenada
			//o proximos 4 sao dados e o ultimo eh um '\n'
			//Para ler em python basta usar o comando readline() da Serial
				
			/*
			Serial.print('x');
			data_x = (byte *) &x;
  			Serial.write(data_x, 4);
			Serial.print("\n");
			
			Serial.print('y');
			data_y = (byte *) &y;
			Serial.write(data_y, 4);
			Serial.print("\n");
			*/
				
			/*Serial.print(x);
			Serial.print("\t");
			Serial.println(y);

			RESH = int (x / 256);
			Serial.write((byte)  RESH);
			RESL = x - RESH * 256;
			Serial.write((byte)  RESL);

			RESH = int (y / 256);
			Serial.write((byte)  RESH);
			RESL = y - RESH * 256;
			Serial.write((byte)  RESL);

			data_x = (byte *) &x;
			Serial.write(data_x, 4);
			delay(1);
			data_y = (byte *) &y;
			Serial.write(data_y, 4);

			digitalWrite(pinLed13, LOW);*/
			opcao = 100;
			break;

		case 'C':
			opcao = 100;
			soft_restart();
			break;

		default:
			opcao = 100;
		}
	}
}
