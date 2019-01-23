<--
.. title: Why Black Holes from the Large Hadron Collider Won't Destroy the World
.. date: 2010-05-16 19:53:00
.. tags: LHC, physics, end of the earth
.. category: old
.. slug: why-black-holes-from-the-large-hadron-collider-won-t-destroy-the-world
.. author: Nic Eggert
.. has_math: true
-->


Hi everyone. As this is my first post, I thought I'd introduce myself.
Like the rest of the Virtuosi, I'm a graduate student in physics at
Cornell University. I work in experimental particle physics, in
particular on the Compact Muon Solenoid, one of the detectors at the
Large Hadron Collider. I'll post more on what I actually do at some
point in the future, but I thought I'd start with a post in the spirit
of some of the other fun calculations that we've done. My goal is to
convince you that black holes created by the LHC cannot possibly destroy
the world.
To start with, the main reason no one working on the LHC is too
concerned about black holes is because of [Hawking
radiation](http://en.wikipedia.org/wiki/Hawking_radiation). While we
usually think of black holes as objects that nothing can escape from,
Stephen Hawking predicted that black holes actually do emit some light,
losing energy (and mass) in the process. In the case of the little bitty
black holes that the LHC could produce, they should just evaporate in a
shower of Hawking radiation.
That's great you say, but Hawking radiation has never actually been
observed. What if Hawking is wrong and the black holes won't evaporate?
Well, the usual next argument is that [cosmic
rays](http://en.wikipedia.org/wiki/Cosmic_ray) from space bombard the
earth all the time, producing collisions many times more energetic than
what we'll be able to produce at the LHC. To me, this is a fairly
convincing argument. However, let's pretend we don't know about these
cosmic rays and that there's no Hawking radiation. We can calculate what
effect black holes produced by the LHC would have on the earth if they
do stick around.
To start out with, the most massive black hole the LHC could produce
would be around 10 Tera-electron-volts, or TeV. We're probably
overestimating here. The eventual goal is for the LHC collisions to be
14 TeV, but producing a particle with the entire collision energy is
incredibly unlikely (see [Tomasso Dorigo's
post](http://www.scientificblogging.com/quantum_diaries_survivor/fascinating_new_higgs_boson_search_dzero_experiment)
for more details on why, along with more details than you probably
wanted to know about hadron colliders). However, we want to think about
the worst case scenario here, and we're just going to do an order of
magnitude calculation, so 10 TeV is a good number. Note that I'm using a
particle physics convention here of giving masses in terms of energies
using E=mc^2. For reference, 10 TeV is about 1000 times smaller than a
small virus.
Now from the mass of our black hole, we can get its size by calculating
something called the [Schwarzschild
radius](http://en.wikipedia.org/wiki/Schwarzschild_radius). The
Schwarzchild radius for a black hole of mass m is given by
$$r = \frac{2Gm}{c^2}\text{.}$$
Here G is Newton's gravitational constant and c is the speed of light.
Plugging our mass in gives us
$$r = 10^{-50} \text{meters.}$$
This is incredibly small! In fact as I was writing this, I realized that
it's actually smaller than the Planck length, which means our equation
for the Schwarzschild radius may be somewhat suspect. Nonetheless, let's
hope that if we ever figure out quantum gravity, it gives us a
correction of order one and proceed with our calculation, which is just
an order-of-magnitude affair anyway.
Now, anything that enters the Schwarzschild radius of the black hole is
absorbed by it. The lightest thing that we could imagine the black hole
swallowing is an electron. Let's figure out how long on average a black
hole would have to travel through material with the density of the earth
before it absorbs an electron. In the spirit of considering the worst
case scenario, we'll have the black hole travel at the speed of light,
and consider the earth to be the density of lead.
We could do a complicated cross-section calculation to find the rate at
which the black hole accumulates mass, but we can also get it right up
to factors of pi through unit analysis. We know that the answer should
involve the area of the black hole, the density of the earth, and the
speed of the black hole. We want our answer to have units of mass per
time to represent the mass accumulation rate of the black hole. The only
combination that gives the right units is
$$a=\frac{\text{mass}}{\text{time}} = \rho c
r^2=\frac{10,000\text{kg}}{\text{m}^3}\frac{3\times 10^8
\text{m}}{\text{s}}(10^{-50}\text{m})^2} =
10^{-88}\text{kg/s}\text{.}$$
Alright, now that we know how fast our black hole accumulates mass,
let's figure out how long it takes it to accumulate an electron. The
electron mass is
$$m_e = 10^{-30}\text{kg,}$$
so the time to accumulate an electron is
$$t = \frac{m_e}{a} = 10^{50}\text{s.}$$
Now, the current age of the universe is 10^17 seconds. The time it
takes our black hole to accumulate an electron is longer than the age of
the universe by many orders of magnitude! So, if the LHC produces black
holes, and if Hawking is wrong, the black holes will just fly straight
through the earth without interacting with anything. Even if we take the
size of the black hole to be the Planck length, our black hole
accumulates an electron in 10^25 seconds, which is still much longer
than the age of the universe.
So the moral of the story is that you should be excited about the new
discoveries that the LHC might produce, and you don't need to worry
about black holes.
