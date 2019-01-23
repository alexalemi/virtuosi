<--
.. title: Q Factors
.. date: 2010-04-21 00:38:00
.. tags: Q factor, fun
.. category: old
.. slug: q-factors
.. author: Alemi
.. has_math: true
-->


When I walk in my door when I get home, I hook my keys, which I keep on
a carabiner, onto a binder clip that I've clipped onto my window sill.
Its a great way to never lose your keys. But one thing I always notice
is that when I hook it on, it swings, and every time it swings it makes
a click. This you might expect. What always surprises me is how long the
keys keep swinging. They seem to swing for a surprisingly long time,
minutes.
It always catches me off guard. In order to explain why, I get to talk
about [Q Factors](http://en.wikipedia.org/wiki/Q_factor)
[](http://en.wikipedia.org/wiki/Q_factor)
The Q factor stands for quality factor. Its a nondimensional parameter
(my favorite kind) that tells you how pure your oscillator is.
Lets back up a step. Lots of things in the world oscillate. Think about
a swing. If you get going on the swing and then stop rocking, you swing
back and forth, back and forth, but eventually you come to a stop.
Imagine swinging on a rusted old swing set. Now give the joint where the
swing swings from a nice shot of WD-40. You can imagine that if you
repeated the experiment (get swinging to some height and then stop
pumping), you'd continue to swing longer. Why? Because the Q factor has
increased. You're swinging on a higher quality swing.
Mathematically its defined to be
$$ Q = 2 \pi \times \frac{ U }{ \Delta U } $$
or 2 pi times the total energy stored in the oscillator divided by the
energy lost in a cycle.
But, another way to gauge the Q factor is the fact that it tells you
something about how the oscillators get damped each period. As a number
it tells you how many periods need to go by for the amplitude of the
oscillations to be damped by
$$ \frac{1}{e^{2\pi}} \sim \frac{1}{535} $$
This allows you to estimate Q factors for everyday objects. A factor of
1/535 is pretty near to my threshold for observing a lot of things. What
does a factor of 535 mean in terms of sound, one of the most common ways
I interact with things around me? Well, sound is measured in decibels,
which is a logarithmic scale, where a factor of 535 in the power output
by something corresponds to a change in the decibels of
$$ dB = 10 \log_{10} \frac{1}{535} \sim -27 $$
What is a decibel change of 27 mean? Well,
[wikipedia](http://en.wikipedia.org/wiki/Sound_pressure#Examples_of_sound_pressure_and_sound_pressure_levels)
tells me that a calm room is somewhere between 20 and 30 decibels, where
as a TV set about a meter away is at about 60 dB. So that tells me that
if something like my keys start off making a sound comparable to the
volume I set my TV at, I can listen to it until it just gets drowned out
by the room and that should give me some estimate for the Q of my keys.
I'll keep you in suspense just a bit longer. I said I was surprised how
long the keys swing. In order to put the Q that I measured in context,
I'll tell you about a few other Qs of things you might have some
experience with.
Most swinging things that I seem to remember coming in contact with have
quality factors of about 10 or so. Swings, or things letting a meter
stick swing, stuff like that. Tuning forks, which are built to be
accurate resonators will have quality factors of about a thousand or so.
The quartz crystal in your watch, which is really supposed to be a good
oscillator has a quality factor of 10 thousand or so. One of the best Q
factors achieved by man is 10^14.
So, what was the Q factor of my keys? I counted the times I could hear
them swinging and got a count of 435. This number isn't to be taken too
seriously, but it indicated that my swinging keys have a quality factor
of something between 400 and 500, which is pretty darn good for
something that wasn't engineered. That explains why it always surprises
me, the keys always seem to swing much longer than I would anticipate.
