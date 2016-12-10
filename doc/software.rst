=======================
Softwares desenvolvidos
=======================

Interface Gráfica
-----------------

A interface gráfica foi feita em linguagem python. Para rodar o programa
corretamente é necessário ter o `*Python* 2.7 <https://www.python.org>`_
com os seguintes pacotes instalados:

        #. `Matplotlib <http://matplotlib.org/>`_ - pacote padrão para plotar
           gráficos.

        #. PySerial - pacote utilizado para comunicação serial entre python
           e arduino.

        #. numpy - pacote fundamental para computação científica com python.

        #. Tkinter - pacote para gerenciar a interface gráfica, um intepretador
           de TK.

Sistemas linux, como `*Ubuntu* <https://www.ubuntu.com/>`_  e
`*Debian* <https://www.debian.org/>`_, costumam vir com python2.7 instalado
como padrão. Caso o aluno não tenha python em seu computador basta instalá-lo
através do gerenciador de pacotes de seu sistema, em ubuntu, por exemplo,
digite *sudo apt-get install python2.7*.

Em windows aconselhamos instalar a distribuição `*Python(x,y)*
<https://python-xy.github.io/>`_, pois nela já se encontram todos os pacotes
necessários. Ao instalar o python(x,y) verifique se as bibliotecas necessárias
estão selecionadas para instalação.

.. literalinclude:: ../Software/GUI/EPR-LEF.py
   :language: python


Firmware para Arduino
---------------------

Para obter os dados de tensão da rampa e sinal do *lock-in* utilizamos um
microcontrolador *Arduino*.

Para programá-lo utilizamos uma linguagem similar a *C++*. O arduino da caixa
já está carregado com o programa de aquisição de dados mas, caso seja
necessário carregá-lo novamente são necessárias algumas bibliotecas adicionais
para que o programa compile corretamente.

	#. Nanoshield_ADC.h - biblioteca para controlar o módulo ADC (convesor
	   analógico digital).

        #. Nanoshield_ADC.h - biblioteca para controlar o módulo ADC (convesor
           analógico digital).

        #. SoftReset.h - biblioteca utilizada para resetar o arduino através
           de software.

        #. SoftwareSerial.h - biblioteca utilizada para se comunicar com o
           software, python nesse caso.

Todas as bibliotecas se emcontram no projeto *EPR-LEF* na pasta Firmware/libs.

.. literalinclude:: ../Firmware/src/EPR_LEF.ino
   :language: c++
