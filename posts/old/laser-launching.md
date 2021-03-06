<--
.. title: Laser Launching
.. date: 2010-04-21 22:22:00
.. tags: laser, launch, satellite, physics
.. category: old
.. slug: laser-launching
.. author: Jesse
.. has_math: true
-->


[![image](http://2.bp.blogspot.com/_SYZpxZOlcb0/S8-y4RmjAhI/AAAAAAAAABE/CueT0Sq1ZYc/s200/space-war-laser.jpg)](http://2.bp.blogspot.com/_SYZpxZOlcb0/S8-y4RmjAhI/AAAAAAAAABE/CueT0Sq1ZYc/s1600/space-war-laser.jpg)
Lasers seem to be on my mind recently. Just yesterday, the class I TA
for (E&M for engineers) talked about the momentum carried by E&M waves.
This called to mind a discussion I had with a housemate a few weeks
back. He had heard somewhere that 'they' were thinking of launching
satellites with lasers. *No way*, I thought to myself. *Satellites are
too heavy*. However, his question has been hovering around in my mind,
so I've decided to try and answer it: can we use a laser to launch a
satellite into orbit? Let us begin with a few simplifying assumptions.
I'm going to assume that we want our launched satellite to reach the
escape velocity of the earth. Of course, we don't want a satellite to
escape orbit, but escape velocity is calculated without considering any
kind of drag forces on our launched object. To first order then, I
expect achieving escape velocity will get our satellite into a
relatively high orbit without actually escaping earth's gravity well.
Second, I'm going to assume our laser is on the ground (reusable
launching device!), and that our satellite is perfectly reflective, so
we're not going to be melting it. Finally, I'm going to assume that the
laser will remain effective at targeting our object up to 15 km above
the surface, around the effective range for lasers used as guides for
[adaptive optics](http://en.wikipedia.org/wiki/Adaptive_optics) in
telescopes.
Now, to the meat of the problem. First, we need to find the escape
velocity from the earth. This is defined as the velocity we would need
to give an object to overcome the gravitational energy of the earth upon
the object. This is found by setting the kinetic energy of the object
equal to the change in gravitational potential energy from the earth's
surface to infinity:
$$ KE=\Delta PE $$ so
$$\tfrac{1}{2}mv_{esc}^2 = \frac{GM_{earth}m}{R_{earth}}$$
(for those interested, the gravitational potential energy at infinity is
defined to be zero). We can easily solve this for v,
$$ v_{esc}=\sqrt{\frac{2GM_{earth}}{R_{earth}}$$
To me, the most remarkable feature of the escape velocity is that it is
independent of the mass of the object! We can now plug in numbers, and
find an escape velocity if \~11.2 km/s.
We now make use of our constraint, that we have to achieve this escape
velocity over 15 km. We assume the laser outputs a constant number of
photons per second, n. The force the laser provides the satellite is the
change in momentum with time,
$$F=\frac{dp}{dt}$$
How is our laser imparting momentum to our system? Well, light is
composed of photons, tiny packets of light. Each photon has momentum.
Assume each photon reflects perfectly, that is, straight backwards and
with no energy loss. Then the photon has reversed its momentum. Since
momentum is conserved, the satellite has gained a momentum of 2p. The
momentum of a photon is
$$p=\frac{h}{\lambda}$$
where h is Planck's constant. This gives
$$F=\frac{2nh}{\lambda}$$
Given a constant force, the time taken to reach some velocity is just
$$t=mv/F$$
In our case the v is the escape velocity. Now, given a constant force,
and no initial velocity, an object of mass m travels a distance d in a
time t given by
$$d=\frac{F}{2m}t^2$$
We can substitute our expression for t into this expression, giving
$$d=\left(\frac{F}{2m}\right)\left(\frac{mv}{F}\right)^2$$
$$d=\frac{mv^2}{2F}$$
What we are really interested in is n, the number of photons per second
this process takes, so we substitute our expression for the force, and
solve for n:
$$d=\frac{mv^2\lambda}{4nh}$$
s0
$$n=\frac{mv^2\lambda}{4hd}$$
Now that we have the number of photons per second our laser supplies,
all that is left is to find the power of laser this would take. The
power of a laser will be given by the number of photons per second times
the energy per photon. The energy per photon is given by E=hf where f is
the frequency of our light. So, the power, P, of our laser is
$$P=nE$$ or
$$P=\frac{mv_{esc}^2\lambda f}{4d}$$ so
$$P=\frac{mv_{esc}^2 c}{4d}$$
Where we have recognized that the frequency times the wavelength of a
photon is just the speed of light, c.
All that remains is to plug in numbers. A medium sized satellite might
be about 750kg, giving a laser power of 4.7*10^14W. This is .5 PW.
According to wikipedia, the greatest power output of a continuous
operation laser is on the order of 1 kW, or \~10^12 times less than our
necessary power! There's no way we're getting a normal sized satellite
into orbit with a laser. What about a smaller satellite? In recent years
picosatellites have proposed, with masses of \~.1kg. This gives a
necessary power of 6.2*10^10, or 620 TW. This is still \~10^8 times
greater than our most powerful continuous laser. In fact, reversing the
calculation, our laser could launch a satellite with a mass of \~1.6 mg.
A little googling reveals this is the same order of magnitude as a grain
of rice! Simply put, we're not going to be launching satellites with
lasers anytime soon.
