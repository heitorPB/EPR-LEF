=================
Descrição Teórica
=================

EPR ou Ressonância Paramagnética Eletrônica é uma técnica espectroscópica
utilizada para analisar amostras que possuem orbitais populados por
apenas um elétron. Elétrons são partículas de spin meio, tais partículas
podem ter momento magnético :math:`m_s g_e \mu_B`, onde :math:`m_s` pode
ser 1/2 ou -1/2, :math:`\mu_B` é o magneton de Bohr e :math:`g_e` é o
fator g de Landé que para o elétron livre.

Na presença de um campo magnético externo, o momento magnético acopla
paralelamente ou anti paralelamente com o campo e da origem a energias
ligeiramente diferentes de acoplamento, esse acoplamento é conhecido como
efeito Zeeman:

.. math::

   E = m_s g_e \mu_B B_0

A variação de energia entre esses níveis é

.. math::

   \Delta E = g_e \mu_B B_0.

Elétrons que estão sozinhos em orbitais podem absorver ou emitir um foton com
energia igual a :math:`\Delta E` e mudar a orientação de seu spin. A energia
de um elétron com spin antiparalelo ao campo é ligeiramente menor que a
energia de um elétron com spin paralelo ao campo isso implica que uma parte
ligeiramente maior dos elétrons estão com seus spins antiparalelos ao campo
e absorvem energia para mudar de estado.

A espectroscopia por EPR funciona observando a absorção de micro-ondas pela
amostra na região de energia entre os níveis acoplados pelo campo magnético
externo.

O sinal de absorção do EPR é extremamente pequeno e para observa-lo é
necessário utilizar um amplificador *lock-in*.

O lock-in utiliza um tipo de detecção chamada detecção sensível a fase.
Para isso ele necessita de um sinal de referência, que nesse experimento é
um sinal senoidal de áudio, esse sinal também é passado para a bobina
interna do EPR, pois o lock-in mede sinais modulados pelo sinal de
referência.

Vamos supor que :math:`Y(H)` seja a função absorção de uma amostra dentro
do EPR onde *H* é o campo produzido pelo eletroímã. Podemos expandir essa
função utilizando uma série de *tylor*:

.. math::

	Y(h') = Y(h) + {\frac{\mathrm{d} Y}{\mathrm{d} H}}(h'-h) +
	\frac{1}{2}\frac{\mathrm{d}^2 Y}{\mathrm{d} H^2}(h'-h)^2 + ...

A diferença *h' - h* pode ser vista como uma função na forma

.. math::

	f(t) = H_m sen(\omega_m t)

isso é possível pois o campo é modulado pelo sinal de referência do
lock-in.

.. math::

	Y(h') =  \left [Y(h) +
	\frac{1}{2}H_m^2\frac{\mathrm{d}^2 Y}{\mathrm{d} H^2} \right ]
	 + \left [ H_m\frac{\mathrm{d} Y}{\mathrm{d} H} \right ]sen(\omega_mt) -
	\left [ \frac{1}{4}H_m^2\frac{\mathrm{d}^2 Y}{\mathrm{d} H^2} \right ]
	sen^2(\omega_mt) + ...

O lock-in funciona multiplicando o sinal de entrada pela referência e o
resultado dessa multiplicação passa por um filtro passa baixa.
O primeiro termo dignificativo que sobra dessa forma é:

.. math::
	S(H) = \frac{1}{2}H_m\frac{\mathrm{d} Y}{\mathrm{d} H}

Portando vemos que o que realmente observamos no EPR é a derivada do sinal
de absorção.
