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


Observações importantes
~~~~~~~~~~~~~~~~~~~~~~~

O programa *EPR-LEF.py* foi testado nos computadores dos alunos, e no
computador disponível no laboratório.

Os resultados obtidos nos computadores dos alunos foram satisfatórios, foram
coletados pontos suficiente para observar todos os sinais necessários. O
computador do laboratório não obteve pontos o suficientes para apresentar
resultados aceitáveis: estava lento demais mesmo antes do programa
ser rodado. Levantamos a hipótese de que o sistema operacional não era
adequado, o computador estava usando *Windows XP*, formatamos a máquina e
colocamos nela o sistema *lubuntu*, um sistema específico para máquinas com
restrição de recursos. Nesse sistema o programa *EPR-LEF.py* obteve resultados
melhores porém, ainda assim, não foi o suficiente para observar sinais claros e
limpos.

Nas três máquinas testadas, os resultados foram substancialmente melhorados
quando retiramos a função de desenhar o gráfico enquanto os dados são obtidos.

Instabilidades no gerador de rampa também dificultaram as medidas, o mesmo
apresenta perda de linearidade no final da varredura a qual não conseguimos
solucionar. A imagem :numref:`fig_rampa_osciloscopio` a seguir mostra este
problema. Ligamos um osciloscópio digital nas saídas de tensão para a fonte
do eletroímã (mostrado na curva amarela) e também na saída para registrador
gráfico (em azul).

A curva azul deveria ser linear de zero a cerca de um vol, com duração de
300 segundos, mas vemos que rampa está muito instável: após cerca de 100
segundos, a tensão sobe abruptamente para o valor máximo, tendo duração de
cerca de 140 segundos.

.. _fig_rampa_osciloscopio:

.. figure:: img/rampa_osciloscopio.jpg
   :width: 75%
   :align: center

   Saídas do controlador de varredura vistas no osciloscópio. Em amarelo, vemos
   o sinal enviado para a fonte do magneto, em azul está a rampa a ser usada em
   registrador gráfico. Esse sistema apresenta um problema de instabilidade
   muito acentuado: a rampa (azul) era para ser linear, de zero a um volt, com
   duração de 300 segundos, mas após cerca de 100 segundos rampa atinge
   abruptamente o valor máximo.

Recomendamos fortemente aos alunos que irão realizar esta prática que utilizem
seus próprios computadores para coleta de dados com o programa *EPR-LEF.py*


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

        #. SoftReset.h - biblioteca utilizada para resetar o arduino através
           de software.

        #. SoftwareSerial.h - biblioteca utilizada para se comunicar com o
           software, python nesse caso.

Todas as bibliotecas se emcontram no projeto *EPR-LEF* na pasta Firmware/libs.

.. literalinclude:: ../Firmware/src/EPR_LEF.ino
   :language: c++
