========
Hardware
========

A contribuição dos alunos Emilio Frari Galera e Heitor Pascoal de Bittencurt
para esse experimento foi desenvolver um sistema de controle e aquisião de
dados digital.

Para isso, utilizamos uma placa *Boarduino*, que consiste em um arduino
adaptado, essa pequena placa utiliza o mesmo microcontrolador que que um
*Arduino Uno*, o *ATmega328* :cite:`arduino_uno`, porém, possui a vantagem de ter entradas para 4
periféricos *nanoshields*, :cite:`boarduino`. Nanoshields são pequenos módulos,
de fácil instalação, basta colocá-los na placa e incluir sua biblioteca no
código para usá-los, o próprio boarduino possui um pino fixo para impedir que
os módulos sejam colocados de maneira errada.

Neste projeto utilizamos 2 nanoshields, um convesor analógico digital, *ADC*,
para ler a tensão de referência da rampa e a tensão de estimativa de campo no
EPR, essa duas tensões são medidas no próprio controlador de varredura. Um nanoshield para fazer
comunicação *serial* com o amplificador *lock-in* e obter medidas do sinal do
EPR.

Observando a :numref:`fig_diagrama_blocos_arduino` podemos ver como tudo está
ligado.

O Arduino se comunica com o lock-in por serial *RS232* pelos pinos *D10* e *D11*,
*transmissor* e *receptor* (Tx e Rx), por intermédio do *nanoshield RS232*,
veja o apêndice sobre o nanoshield RS232. O lock-in recebe um comando enviado
pelo arduino e retorna uma resposta correspondente em *string*.

Importante: O programa foi feito para se comunicar com o lock-in com *Baud rate* de
*9600*, qualquer alteração no *Baud rate* deve ser feita com cuidado pois os bits
de configuração do lock-in devem ser reconfigurados, de acordo com
:cite:`lock-in-man`.

O nannoshield ADC se comunica com o arduino através do protocolo *i2c*, o *i2c*
serve tipicamente para comunicar circuitos integrados periféricos (no caso, o
nanoshield ADC) com microcontroladores (no caso, o arduino Boardoino).

O ADC lê as tensões de referência e campo e envia tudo para o arduino pela
*i2c*, :numref:`fig_diagrama_blocos_arduino`.

Note o divisor de tensão na leitura da tensão da rampa,
:numref:`fig_diagrama_blocos_arduino`, isso é importante pois o ADC está
configurado para ganho máximo, para esse conversor isso significa um fundo de
escala para leitura de tensão de *256mV*, tensões maiores podem danificar o
ADC.

O tempo de varredura e a largura do campo magnético são controlados pelo
arduino através dos pinos D4 e D5 para o tempo e D6 e D7 para o campo.

O controlador de varredura permite 4 tempos de varredura e 4 valores diferentes
de larguras de campo. Os 4 valores de tempo são controlados pelos pinos D4 e D5
através de um multiplexador, o campo é controlado de maneira similar, veja os
comentários no código de Firmware.

A comunicação do Boarduino com o computador é feita através de uma porta USB
