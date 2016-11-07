#include <Arduino.h>
#include <Wire.h>
#include <stdlib.h>
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
	double x;
	double y;
	char result[11];

	if (Serial.available() > 0) {
		opcao = Serial.read();

		switch(opcao) {
		case 'A':
			// TODO deixar esse case decente
			ret1:
			if (Serial.available() > 0)
				media = Serial.parseInt();
			else
				goto ret1;

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

			dtostrf(x, 4, 6, result);
			Serial.write('x');
			Serial.print(strlen(result));
			Serial.print(result);
			Serial.write('X');

			dtostrf(y, 2, 8, result);
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

		default:
			opcao = 100;
		}
	}
}
