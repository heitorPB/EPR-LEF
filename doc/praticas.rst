========
Práticas
========

Ligar o equipamento
-------------------

Ligue o equipamento e entenda cada parâmetro


Espectro da amostra DPPH
------------------------

Nesta prática vamos utilizar uma amostra que é comumente empregada para
procedimentos de calibração dos espectrômetros de RPE. Trata-se do DPPH,
ou, diph enyl picryl hydrazyl . Na forma sólida (como a que vamos usar)
o espectro de EPR do DPPH consiste de uma única linha muito intensa,
relativamente estreita (largura de aproximadamente 2 G), centralizada em
g = 2.0038 , e ligeiramente assimétrica. Colocar o tubo contendo DPPH na
cavidade. A amostra é muito pequena (fração de milímetros) e está colocada
no fundo do tubo, enrolada em fita teflon (por isso ela é branca e não
negra, como seria a cor natural do DPPH). Posicione cuidadosamente a amostra
no centro da cavidade. Ajustar o espectrômetro e medir o sinal utilizando
varredura de 50G. Meça o valor do campo magnético no centro da linha com uma
sonda Hall e a freqüência da microonda com o frequencímetro e, a partir
destes dados, calcule o fator g do DPPH. Compare com o valor tabelado : g =  2.0038.

Análise do efeito conjunto da constante de tempo e velocidade de varredura
--------------------------------------------------------------------------

Varie a constante de tempo entre os valores de 10ms a 10s, registrando os
sinais com varreduras de 0.5 min, 1 min e 3 min. Explique os resultados
com base nas informações deste texto e das referências 3 e 4.

Lock-in no modo “2f”
--------------------

Novamente meça o sinal do DPPH com o programa EPR-LEF.py com o lock-in em modo
"f" (primeira derivada) com a amplitude de modulação ótima,
:numref:`fig_lockin`. Passe o lock-in para o modo “2f” e registre o sinal
novamente com o EPR-LEF.py . Para que os dois sinais fiquem com amplitudes
similares será necessário que a sensibilidade (vertical) do sinal "2f" tenha
que ser maior.Para entender melhor o que significa o modo "2f", estude o Apêndice1.

Para esta amostra de DPPH, qual deve ser a melhor configuração dos
parâmetros amplitude da modulação, constante de tempo, amplitude de varredura
e tempo da varredura para que o espectro represente corretamente a derivada do
sinal de absorção?

:math:`MgO + Cr3^{++} Mn2^{+}`
------------------------------

Esta é uma amostra de um cristal MgO dopado com :math:`Cr^{3+}` e :math:`Mn^{2+}`.
Apesar de ser uma amostra cristalina, seu espectro é isotrópico e consiste de
duas componentes: um sexteto resultante da interação hiperfina com o núcleo
do Manganês, I = 5/2, e uma linha intensa (com transições proibidas laterais)
proveniente do Cromo. O fator g da linha intensa é 1.9797. Esta amostra também
é muito pequena e está colocada no fundo do tubo. Posicione cuidadosamente a
amostra no centroda cavidade.

Devido ao fato de que a linha central é intensa e relativamente estreita e ter
um fator g menor que 2, esta amostra é também muitas vezes utilizadas como
marcador para finalidades de calibração. Em adição a esta linha central mais
intensa, você deverá observar também seis linhas menos intensas, separadas por
cerca de 80-100 Gauss devido ao :math:`Mn^{2+}`. Como o espectro é largo, faça
a medida utilizando uma varredura lenta de 1000 Gauss.

Duas amostras
-------------

Realizar a calibração das varreduras de 100 G, 500 G e 1000 G. Para isto,
deve-se montar as duas amostras, DPPH e MgO simultaneamente na cavidade,
ver figura :numref:`fig_amostra_centro`. A idéia é registrar os dois sinais
simultaneamente, em uma única varredura. Como o sinal do DPPH é mais intenso,
esta amostra deve ser colocadapor baixo, um pouco abaixo do centro da cavidade.

Para isso, não toque na amostra de MgO já instalada e medida; e introduza o
tubo com a amostra de DPPH na cavidadepor baixo, com cuidado, até que ele toque
o outro tubo e, depois, volte um pouquinho. A amostra de DPPH deve ficar a apenas
alguns milímetros abaixo da de MgO. Nesta situação, os dois espectros irão ser
registrados com intensidades semelhantes. Como os fatores g das duas amostras são
conhecidos pode-se determinar, com precisão, a distância entre as duas linhas e
a partir daí fazer a calibração do papel, emG/cm,nastrêsescalas de varredura:
100 G, 500 G e 1000 G.
