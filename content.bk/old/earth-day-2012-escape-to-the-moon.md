Title: Earth Day 2012: Escape to the Moon
Date: 2012-04-22 15:12:00
Tags: 
Category: old
Slug: earth-day-2012-escape-to-the-moon
Author: Brian


It is now Earth Day 2012, and, according to the Mayan predictions, [The
Virtuosi will destroy the
earth](http://thevirtuosi.blogspot.com/search/label/end%20of%20the%20earth).
In a futile attempt to fight my own mortality, I decided to send
something to the Moon. It seems, for a poor graduate student trying to
get to the Moon, the most difficult part is the Earth holding me back.
So first I'll focus on escaping the Earth's gravitational potential
well, and if that's possible, then I'll worry about more technical
problems, such as actually hitting the moon. Moreover, in honor of the
destructive spirit of The Virtuosi near Earth Day, I'll try to do this
in the most Wiley-Coyote-esque way possible. **Preliminaries** If we
want to get to the Moon, we need to first figure out how much energy
we'll need to escape the Earth's gravitational pull. "That's easy!" you
say. "We need to escape a gravitational well, and we know from Newton's
law that the potential from a spherical mass *ME* 's gravity for a test
mass *m* is : \begin{equation} \Phi = - \frac {G M_{E} m}{r}
\label{eqn:gravpot} \end{equation} We're currently sitting at the
radius of the Earth *RE*, so we simply need to plug this value in and
we'll find out how much energy we need." This is all well and good, but
i) I can never remember what the gravitational constant *G* is, and ii)
I have no idea what the mass of the Earth *ME* is. So let's see if we
can recast this in a form that's easier to do mental arithmetic in.
Well, we know that the force of gravity is the related to the potential
by: $$ \vec{F}(r) = - \vec{\nabla} \Phi = - \frac {d\Phi}{dr}
\hat{r} \\ \vec{F} = - \frac {G m M_E } {r^2}
\label{eqn:gravforce} $$ Moreover, we all know that the force of
gravity at the Earth's surface is *F(r=RE)=-mg*. Substituting this in
gives: $$ \frac {G m M_E} {R_E^2} = m g \quad \textrm{, or} $$
\begin{equation} \frac {G m M_E}{R_E} = m g {R_E} \quad .
\label{eqn:betterDef} \end{equation} So the depth of the Earth's
potential well at the Earth's surface is *mgRE*. If we use *g* = 9.8
m/s^2 \~ 10 m/s^2 and *RE* = 6378 km \~ 6x10^6 m, then we can write
this as \begin{equation} \Delta \Phi = m g {R_E} \approx m \times
6 \times 10^7 \textrm{m}^2/\textrm{s}^2 \quad \textrm{(1)},
\end{equation} give or take. How fast do we need to go if we're going
to make it to the Moon? Well, at the minimum, we need the kinetic energy
of our object to be equal to the depth of the potential well
[[1]](#footnote-1), or $$ \frac 1 2 m v^2 = 6 m \times 10^7
\textrm{m}^2/\textrm{s}^2 \quad \textrm{or} \\ v \approx 1.1
\times 10^4 \textrm{ m/s (2)} . $$ So we need to go pretty fast --
this is about Mach 33 (33 times the speed of sound in air). At this
speed, we'd get from NYC to LA in under 7 minutes. Looks difficult, but
let's see just how difficult it is. **Attempt I: Shoot to the Moon**
What goes fast? Bullets go fast. Can we shoot our payload to the moon?
Let's make some quick estimates. First, can we shoot a regular bullet to
the moon? Well, we said that we need to go about Mach 33, and a fast
bullet only goes about Mach 2, so we won't even get close. Since energy
is proportional to velocity squared, we'll only have (2/33)^2 \~ 0.4 %
of the necessary kinetic energy. [[2]](#footnote-2) So let's make a
bigger bullet. How big does it need to be? Well, loosely speaking, we
have the chemical potential energy of the powder being converted into
kinetic energy of the bullet. Let's assume that the kinetic energy
transfer ratio of the powder is constant. If a bullet receives kinetic
energy *1/2mbvb^2* from a mass *mP* of powder, then for our payload to
have kinetic energy *1/2 M V^2*, we need a mass of powder *MP* such
that \begin{equation} \frac {M_P} {m_P} = \frac M {m_b} \times
\frac {V^2}{v_b^2} \end{equation} A quick reference to Wikipedia
for a [7.62x51mm NATO
bullet](http://en.wikipedia.org/wiki/7.62%C3%9751mm_NATO) shows that
\~25 grams of powder propels a \~10 gram bullet at a speed of \~Mach
2.5. We need to get our payload moving at Mach 33, so (*V/vb*)^2 \~
175. If we send a 10 kg payload to the Moon, we have *M/mb* \~ 1000. So
we'll need about 1.75 x 10^5 the amount of powder of a bullet to get us
to the Moon, or about 4400 kg, which is 4.8 tons (English) of powder.
That's a lot of gunpowder to get us to the Moon. For comparison, if we
are going to construct a tube-like "case" for our 10 kg
bullet-to-the-Moon, it will have to be about half a meter in diameter
and 17 feet tall. So I'm not going to be able to shoot anything to the
Moon anytime soon. **Attempt II: Charge to the Moon** OK, shooting
something to the Moon is out. Can we use an electric field to propel
something to the Moon? Well, we would need to pass a charged object
through a potential difference such that \begin{equation} q \Delta
\Phi_E = m g R_E = 6 m \times 10^7 \textrm{m}^2/\textrm{s}^2
\quad . \label{eqn:chargepot} \end{equation} After the humiliation of
the last section, let's start out small. Can we send an electron to the
Moon? We could plug numbers into this equation, but I'm too lazy to look
up all those values. Instead, we know that we need to get our electron
(rest mass 511 keV) to a speed which is (Eq. 2) $$v \approx 1.1 \times
10^4 \textrm{m/s} \approx 4 \times 10^{-5} c. $$ So an electron
moving at this velocity will have a kinetic energy of $$ \textrm{KE} =
m c^2 \times \frac 1 2 \frac {v^2}{c^2} = 511 \textrm{ keV}
\times \frac 1 2 \frac {v^2}{c^2} \\ \qquad \approx 511
\textrm{ keV} \times 0.8 \times 10^{-9} \approx 0.4 \times
10^{-3} eV. $$ So we can give an electron enough kinetic energy to get
to the moon with a voltage difference of 0.4 mV, assuming it doesn't hit
anything on the way up (it will). We can send an electron to the Moon!
How about a proton? Well, the mass of a proton is 1836x that of an
electron, but with the same charge, so we'd need 1836 * 0.4 mV \~ 0.73
V to get a proton to the Moon -- again, pretty easy. Continuing this
logic, we can send a singly-charged ion with mass 12 amu (*i.e.* C-)
with a 9V battery, and a singly-charged ion with mass 150 amu (something
like caprylic acid) using a 110V voltage drop. (Again, assuming these
don't hit anything on the way up.) How about our 10 kg object? Let's say
we can miraculously charge it with 0.01 C of charge. [[3]](#footnote-3)
Then from Eq. (1), we'd need $$ 0.01 C \times \Delta \Phi_E \approx
6 \times 10^8 \textrm{ J ,} $$ or a potential difference of $$
\Delta \Phi_E = 6 \times 10^{10} \textrm{ V. } $$ That is a HUGE
potential drop. For comparison, if we have 2 parallel plates with a
surface charge of 0.01 C/m^2 (again, a huge charge density), they'd
have to be a distance $$ d = 6 \times 10^{10} \textrm{V} \times
\epsilon_0 / (0.01 \textrm{C/m}^2) \approx 53 \textrm{ meters
apart} $$ It looks like I won't be able to send something to the Moon
using tools from my basement anytime soon.
[1] We'll ignore both air resistance and the Moon's gravitational
attraction for simplicity.
[2] Since the potential *U \~ - 1/r*, if we increase our potential
energy by 0.4%, this is (to 1st order) the same as increasing *r* by
0.4%. So we'll get 0.004 * 6378 km \~ 25 km above the Earth's surface.
Of course [air resistance slows it down a
lot](http://scienceblogs.com/dotphysics/2009/09/how-high-does-a-bullet-go.php).
[3] According to Wikipedia, this is [0.04% of the total charge of a
thundercloud](http://en.wikipedia.org/wiki/Orders_of_magnitude_%28charge%29).
And if our object is uniformly charged with a radius of 1 m, it will
have an electrical self-energy of ** $$ U = \frac 1 2 \int
\epsilon_0 E^2 dV \approx 36 \textrm{kJ} $$
