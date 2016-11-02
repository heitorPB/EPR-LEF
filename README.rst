========
EPR-LEF
========

Sistema de Aquisição Digital para o experimento de EPR do Laboratório de
Ensino de Física do IFSC - USP.

Desenvolvido por Emilio Galera e Heitor Pascoal de Bittencourt, sob
orientação do Professor Luiz Antônio de Oliveira Nunes.

Funcionalidades
---------------

- Sistema digital, permitindo salvar o espectro como figura e/ou exportar
  o sinal obtido.
- Aquisição de sinal do *lock-in* usando um *ADC* de 16-bits.
- Controle manual de varredura do campo magnetico.


Instalação
----------

É necesario Python com as bibliotecas:

- pySerial
- matplotlib
- TKinter

Para compilar o *firmware* para Arduino:

- avrdude
- avr-gcc < 6.1
- avr-libc

Ou IDE do Arduino.


Uso
----

    Te vira, bixo.
