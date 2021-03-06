<--
.. title: Cell Phone Brain Damage: Part Deux
.. date: 2010-05-19 16:03:00
.. tags: molecules, fun, dimensional analysis, cell phone
.. category: old
.. slug: cell-phone-brain-damage-part-deux
.. author: Alemi
.. has_math: true
-->


[![image](http://3.bp.blogspot.com/_YOjDhtygcuA/S_RDhF0ciII/AAAAAAAAAKg/XexPpWRmpg4/s320/cell-phone-21.jpg)](http://3.bp.blogspot.com/_YOjDhtygcuA/S_RDhF0ciII/AAAAAAAAAKg/XexPpWRmpg4/s1600/cell-phone-21.jpg)

I thought I'd take another look at cell phone damage, coming at it from
a different direction than my colleague. Mostly I just want to consider
the energy of the radiation that cell phones produce, and compare that
with the other relevant energy scales for molecules.

### Cell Phone Energy

So, lets start with cell phones. I looked at my cell phone battery, and
it looks like it is rated for 1 A, at 3.5 V. So when it is running at
its peak it should put out about 3.5 W of power in electromagnetic waves
(assuming it reaches its rating and all of that energy is fully
converted into radiation). But what form does this energy take? Well,
its electromagnetic radiation, so its in the form of a bunch of photons.
In order to determine the energy of each photon, we need to know the
frequency of the radiation. Surfing around a bit on wikipedia, I
discovered that most cell phones operate in the 33 cm radio band, or
somewhere between about 800 - 900 Mhz. How much energy does each \~ 1
Ghz photon have? We know that the energy of a photon is: $$ E = h \nu
\sim 7 \times 10^{-25} \text{ J} \sim 4 \times 10^{-6} \text{
eV} $$ it will be convenient to know the photon energy in "eV's". 1 eV
is the energy of a single electron accelerated through a potential of 1
volt, or $$ 1 eV = (1 \text{ electron charge} ) * ( 1 \text{ Volt} )
= 1.6 \times 10^{-19} \text{ J} $$ So my cell phone is sending out
signals using a bunch of photons, each of which has an energy of about 4
micro eVs. Lets consider the energy scales involved in most molecular
processes and compare those scales with this energy.

### Molecules

Great. We have a number. What what does it mean? A number in physics
means little without some context. Lets try and consider what photons
can do to molecules. I can think of three different processes: first, a
photon could knock out an electron (i.e. ionize the molecule), second
the photon could make the molecule vibrate or wiggle, or third the
photon could make the molecule rotate. Lets see if we can estimate the
energies for these three different types of processes. Lets first
collect some of the information we know about atoms and molecules so
that we can continue our estimations. I know that most atoms are about
an angstrom big, or 10^(-10} meters. I know the charge of an electron
and proton.

#### Ionization

What are typical molecular ionization energies? Well we could try and
estimate it. Whats the energy stored in an electron and proton being
about an angstrom apart? Well, remembering some of our electrostatics we
have $$ E = \frac{ k q_1 q_2 }{ r} \sim (9 \times 10^9) \frac{
(1.6 \times 10^{-19} \text{ C} )^2 }{ (1 \ \AA)} \sim 14 \text{
eV} $$ which is pretty darn close to the ionization energy of hydrogen
at 13.6 eV. So I will claim that since all atoms are about the same
size, typical ionization energies across the board are about 10 eV, in
order of magnitude.

#### Vibration

What about making our molecules vibrate? Well what are the energies of
molecular bonds? They ought to be quite similar to the ionization
energies of molecules, but as we know they are a tad weaker. Bond
energies for most molecules are on the order of a few eV. The
oxygen-hydrogen bond in water for example has a binding energy of 5.2
eV. What does that have to do with vibration? Well, if we consider a
material as made up by a bunch of atoms all stuck together with springs,
we can estimate the spring constant. Assuming that a typical binding
energy of 3 eV or so, and a typical atomic separation of 1 angstrom or
so, we can estimate the spring constant for atoms, knowing $$ U =
\frac{1}{2} k x^2 $$ $$ 3 \text{ eV } \approx \frac{1}{2} k ( 1 \A
)^2 $$ $$ k \approx 100 \text{ N/m} $$ And now having estimated the
spring constant, we can estimate how much energy there is in a quanta of
atomic vibration, i.e. figure out the corresponding frequency from $$
\omega = \sqrt{ k / m } $$ and quantize it in units of hbar. We
discover that a quanta of atomic vibration typically has energies on the
order of $$ U = \hbar \omega = \hbar \sqrt{ \frac{ k }{ m } } $$ $$
= 6.6 \times 10^{-16} \text{ eV s } \sqrt{ \frac{ 100 \text{ N/m}
}{ 2 \times \text{ mass of a proton } } } \sim 0.1 \text{ eV} $$ So
molecular vibration energies are about a tenth of an electron volt.

#### Rotation

I can also make molecules rotate. What is the energy of the lowest
rotational mode of a molecule. Well, bohr taught us that angular
momentum is quantized in units of h, planck's constant. Imagine a two
atom molecule, with two atoms separated by an angstrom. The energy of a
rotating object can be written $$ E = \frac{ L^2 }{2 I } $$ in analogy
to the energy of a moving object $$ E = \frac{ p^2 }{2m} $$ where I is
the moment of inertia for a molecule. We will estimate $$ I = 2 m r^2
\sim 2 (1 * \text{ mass of proton} * ( 1 \text{ \AA} )^2 \sim 3
\times 10^{-47} \text{ kg m}^2 $$ So we can estimate the rotational
energy for a small molecule $$ E = \frac{ h^2 }{ 2 m r^2 } \sim 80
\text{ meV} $$ and this is for a small molecule, and will only go down
for larger molecules, as I will increase. So I will call typical
rotational energies 1 meV for medium sized molecules.

### Heat

Another relevant energy scale to discuss when we are talking about
brains is the energy due to the fact that our brain is rather warm. Body
temperature is about 98 degrees Fahrenheit, or 37 degrees Celsius, or
310 Kelvin. Statistical Mechanics tells us that temperature is an
average energy for a system, and in fact the [Equipartition
theorem](http://en.wikipedia.org/wiki/Equipartition_theorem) tells us
that when a body is in thermal equilibrium, every mode of it has $$
\frac{1}{2} k_B T $$ amount of energy in it. For our brain that means
$$ E = \frac{1}{2} k_B T = 2 \times 10^{-21} \text{ J } = 13
\text{ meV} $$ i.e. just the fact that our brains are hot means that
every degree of freedom in our brain already has 13 millielectron volts
associated with it. Comparing to our results above, this is comparable
to the rotational energies of molecules, but a tad less than their
vibrational energies, which means that we should expect most of the
molecules in our head to already be rotating.

### Results

So going through some very rough calculations, we discovered that for
molecules, there are three obvious ways you can get them hot and
bothered, you can ionize them, make them wiggle, or make them rotate.
There are some typical energy scales for these things, ionization
energies are about 10 eV, vibrational energies are about 0.1 eV, and
rotational energies are about 0.001 eV. In addition, our brain already
has about 13 meV of energy in every one of its degrees of freedom, and
cell phone photons have an energy some 1/3300 of this. And what was the
energy for each cell phone photon? 0.000004 eV. Notice that this energy
is about a hundred times weaker than typical rotational energies, and
some 3300 thousandth times less than the natural thermal energy in our
brains. Now you can begin to understand why most physicists are not too
worried about the effects of cell phones. The radiation from cell phones
is just not on the kind of energy scales that affect molecules in was
that could potentially harm us. So I'm not too worried.
