========
EPR-LEF
========

Sistema de Aquisição Digital para o experimento de EPR do Laboratório de
Ensino de Física do IFSC - USP.

Desenvolvido por Emilio Galera e Heitor Pascoal de Bittencourt, sob
orientação do Professor Luiz Antônio de Oliveira Nunes e do técnico
Antenor Fabbri Petrilli Filho.


Funcionalidades
---------------

- Sistema digital, permitindo salvar o espectro como figura e/ou exportar
  o sinal obtido.
- Aquisição de sinal do *lock-in* usando comunição digital.
- Controle manual de varredura do campo magnetico.


Instalação
----------

Interface Gráfica
~~~~~~~~~~~~~~~~~

É necesario Python com as bibliotecas:

- pySerial
- matplotlib
- TKinter

O código fonte encontra-se em Software/GUI/EPR-LEF.py

Firmware
~~~~~~~~

Para compilar o *firmware* para Arduino, utilize a IDE do mesmo. O código
encontra-se em Firmware/src e as bibliotecas necessárias em Firmware/libs.


Uso
----

    Te vira, bixo.
