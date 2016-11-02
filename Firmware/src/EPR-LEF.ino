#include <Nanoshield_ADC.h>
#include <Wire.h>
#include <SoftReset.h>

long int i;
int opcao = 'B';
int media = 5;
long int pot;
int RESH; 
int RESL;
float x;
float y;
byte *data_x;
byte *data_y;

const int channel_x = 0;
const int channel_y = 1;
const int pinLed13 = 13;

Nanoshield_ADC adc;

void setup()
{
	Serial.begin(115200);
	pinMode(pinLed13, OUTPUT);
	analogReference(DEFAULT);
	media = 1;
	adc.begin();
}

 void loop()
{
	if (Serial.available() > 0) {
		opcao = Serial.read();
		//opcao= 'B';
		switch(opcao)
		{
		case 'A':
			ret1:
			if (Serial.available( ) > 0)
				media = Serial.parseInt();
			else
				goto ret1;

			opcao=100;
			break;

		case 'B':
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
			/*Serial.print(x);
			Serial.print("\t");
			Serial.println(y);*/

			/*RESH = int (x / 256);
			Serial.write((byte)  RESH);
			RESL = x - RESH * 256; 
			Serial.write((byte)  RESL);

			RESH = int (y / 256);
			Serial.write((byte)  RESH);
			RESL = y - RESH * 256; 
			Serial.write((byte)  RESL);*/

			data_x = (byte *) &x;
			Serial.write(data_x, 4);
			delay(1);
			data_y = (byte *) &y;
			Serial.write(data_y, 4);

			//Serial.println (pot); 
			digitalWrite(pinLed13, LOW);

			opcao = 100;
			//opcao = 'B';
			break;

		case 'C':
			opcao=100;
			soft_restart();
			opcao=100;
			break;

		}
	}
}
