=================
Descrição Teórica
=================

EPR ou Ressonância Paramagnética Eletrônica é uma técnica espectroscópica
utilizada para analisar amostras que possuem orbitais populados por
apenas um elétron. Elétrons são partículas de spin meio, tais partículas
podem ter momento magnético :math:`m_s g_e \mu_B`, onde :math:`m_s` pode
ser 1/2 ou -1/2, :math:`\mu_B` é o magneton de Bohr e :math:`g_e` é o
fator g de Landé, que para o elétron livre vale aproximadamente *2.0023*.

Na presença de um campo magnético externo, o momento magnético acopla
paralelamente ou anti paralelamente com o campo e da origem a energias
ligeiramente diferentes de acoplamento, esse acoplamento é conhecido como
efeito Zeeman. A energia desse acoplamento é dada por:

.. math::

   E = m_s g_e \mu_B B_0

A variação de energia entre esses níveis é

.. math::

   \Delta E = g_e \mu_B B_0.

Note que quando um elétron passa de um nível a outro ele pode emitir ou
absorver :math:`\Delta E` na forma de um foton com frequência :math:`\nu`
e energia :math:`h\nu` que é igual a energia de transição
:math:`\Delta E`.

Essa associação, entre a frequência do foton e :math:`\Delta E`, é importante
pois esse espectrômetro usa uma fonte de radiação de frequência conhecida e
uma varredura de campo magnético para obter o espéctro de amostras.

Dentro da amostra a probabilidade de um elétron ter spin :math:`m_s = 1/2` é:

.. math::

   P_{1/2} = \frac{e^{-\frac{E_{1/2}}{k_bT}}}{e^{-\frac{E_{1/2}}{k_bT}}+
            e^{-\frac{E_{-1/2}}{k_bT}}}

e a probabilidade de um eletron ter spin :math:`m_s = -1/2` é, de maneira
similar:

.. math::
   P_{-1/2} = \frac{e^{-\frac{E_{-1/2}}{k_bT}}}{e^{-\frac{E_{1/2}}{k_bT}}+
             e^{-\frac{E_{-1/2}}{k_bT}}}

A partir da razão entre as duas probabilidades é possível obter uma entimativa
da quantidade relativa de elétrons com spin :math:`1/2` e :math:`-1/2`.

.. math::
   \frac{P_{1/2}}{P_{-1/2}} =
   \frac{ e^{-\frac{E_{1/2}}{k_bT}} }{e^{-\frac{E_{-1/2}}{k_bT}}} =
   e^{ - \left (  \frac{E_{1/2}}{k_bT} - \frac{E_{-1/2}}{k_bT} \right )} =
   e^{-\frac{\Delta E}{k_bT}} = e^{-\frac{h\nu}{k_bT}}

O :math:`\Delta E` típico para acoplamento entre spin e campo magnético está
dentro do espéctro de frequência de micro-ondas, para uma frequência de
:math:`\nu \approx 9.75GHz` e temperatura de :math:`298 K` a equação acima da
uma razão aproximadamente :math:`0.998`.

Isso mostra que há um número ligeiramente maior de elétrons com spin
:math:`-1/2`. Tais elétrons absorvem energia para mudar de estado, portanto
a espectroscopia por EPR funciona observando a absorção de micro-ondas pela
amostra na região de energia entre os níveis acoplados pelo campo magnético
externo.

O sinal de absorção do EPR é extremamente pequeno e uma maneira de observa-lo é
utilizar um amplificador *lock-in*.

O lock-in utiliza um tipo de detecção chamada detecção sensível a fase.
Para isso ele necessita de um sinal de referência, que nesse experimento é
um sinal senoidal, esse sinal também é passado para a bobina interna do EPR,
pois o lock-in mede sinais modulados pelo sinal de referência.

Vamos supor que :math:`Y(H)` seja a função absorção de uma amostra dentro
do EPR onde *H* é o campo produzido pelo eletroímã, esse campo varia de maneira
bem lenta e passa pelos eventuais picos de absorção da amostra. O sinal de
referência do *lock-in* também passa pelo EPR e esse varia de maneira muito
rápida em comparação com o a variação do campo *H*.
Com isso em mente, expandindo a função de absorção *Y(H)* do campo gerado
pelo eletroímã em terno de um ponto *h - h'* na curva de *Y(H)* temos:

.. math::

	Y(h') = Y(h) + {\frac{\mathrm{d} Y}{\mathrm{d} H}}(h'-h) +
	\frac{1}{2}\frac{\mathrm{d}^2 Y}{\mathrm{d} H^2}(h'-h)^2 + ...

Como a função *Y(H)* varia de maneira muito lenta no tempo em comparação com o
sinal de referência do lock-in diferença *h' - h* pode ser vista como uma
função periódica de frequência igual a do sinal de referência.

.. math::

	h - h' = f(t) = H_m sen(\omega_m t)

Isso é possível pois o campo é modulado pelo sinal de referência do
lock-in. O campo varia lentamente mas, há uma modulação pequena e muito rápida
que ocorre em torno do valor *H*.

.. math::

	Y(h') = Y(h) + {\frac{\mathrm{d} Y}{\mathrm{d} H}}H_msin(\omega t) +
        \frac{1}{2}\frac{\mathrm{d}^2 Y}{\mathrm{d} H^2}H_m^2sin^2(\omega t) + ...

O lock-in funciona multiplicando o sinal de entrada, a ser amplificado, pela
referência :math:`sen(\omega t)`.

.. math::

	Y(h') = Y(h)sin(\omega t) + {\frac{\mathrm{d} Y}{\mathrm{d} H}}
	H_msin^2(\omega t) + \frac{1}{2}\frac{\mathrm{d}^2 Y}{\mathrm{d} H^2}
	H_m^2sin^3(\omega t) + ...

O resultado dessa multiplicação passa por um filtro passa baixa, isso é
equivalente a integrar o sinal em um período de tempo. O primeiro termo
dignificativo que sobra dessa forma é:

.. math::
	S(H) = \frac{1}{2}H_m\frac{\mathrm{d} Y}{\mathrm{d} H}

Portando vemos que o que realmente observamos no EPR é a derivada do sinal
de absorção.
