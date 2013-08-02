Title: Letting Air Out of Tires
Date: 2010-05-03 23:21:00
Tags: bike, tire, thermodynamics, gas, cold, experiment
Category: old
Slug: letting-air-out-of-tires
Author: Jesse


Have you ever noticed how when you let air out of a bike tire (or, I
suppose, a car tire) it feels rather cold? Today we're going to explore
why that is, and just how cold it is. Many people consider the air
escaping from a tire as a classic example of an adiabatic process. What
is an adiabatic process? It is a process that happens so quickly there
is no time for heat flow to occur. For our air in the bike tire this
means we're letting it out of the tire so quickly that no energy can
move into it from the surrounding air. This may not be exactly true,
there may be a little energy flow, but there is little enough that we
can ignore it. Given that, how do we talk about temperature change?
Let's give a physical motivation first. Imagine a gas as a collection of
hard spheres, like baseballs. Envision this bunch of baseballs in a box.
Suppose you make the volume of the box smaller, you move the walls in.
The baseballs will start to bounce around faster. Having trouble
thinking of this? Think of a single baseball in a box. Imagine it hits a
wall moving towards it. What happens? That's just like what happens when
a baseball hits a baseball bat moving towards it, it goes flying. That
is, it starts moving faster. The speed with which these gas particles
are moving is what we measure as temperature. So shrinking our box
increases the temperature. Likewise, expanding our box will decrease the
temperature. The same principle holds here. Our gas is expanding from a
small volume (the bike tire) into a larger volume (the surrounding
world). Thus we expect the temperature to decrease.
Got all that? Good. Now for some math. It turns out that using the ideal
gas law, we can derive that for an (reversible) adiabatic process
$$PV^\gamma=constant$$
where P is the pressure of the gas, V is the volume of the gas, and
gamma is (for our purposes) just a number. The ideal gas law states that
$$PV=NkT$$
Where N is the number of gas molecules we have, T is the temperature of
the gas, and k is a constant. Since N doesn't change in the process
we're considering, we can use this to rewrite the above equation, by
substituting for V. This gives
$$P^{1-\gamma}T^{\gamma}=constant$$
Where the constant is not the same as above.
Because this is equal to a constant, we can say that our initial
pressure and temperature are related to our final pressure and
temperature by
$$P_i^{1-\gamma}T_i^{\gamma}=P_f^{1-\gamma}T_f^{\gamma}$$
We can solve this for the final temperature giving
$$T_f=T_i\left(\frac{P_i}{P_f}\right)^{\tfrac{1-\gamma}{\gamma}}$$
Finally, we can plug in some numbers. Gamma is 7/5 for diatomic gases
(which is most of air). If we assume the air is about room temperature,
20 C, and the tire is at 60 psi, this gives (1 atmosphere of pressure is
15 psi):
$$T_f=293K\left(\frac{60 psi}{15
psi}\right)^{\tfrac{1-7/5}{7/5}}=197K$$
Converting back from Kelvin to C, this is -76 C or -105 F. That's cold!
**For the Expert:**
There is actually a debate as to whether or not adiabatic cooling is
responsible for the chill of air upon being let out of a tire. The
argument for it is fairly straightforward. The released air does work on
the surrounding atmosphere as it leaves, lowering the energy of the gas.
If this is the primary effect, then the change in temperature is given
above. However, it is possible that we can consider this a free
adiabatic expansion. In a free adiabatic expansion (like a gas expanding
into a vacuum), there is no work done, because gas is not acting
'against' anything.
The other possibility is the [Joule-Thomson
effect](http://en.wikipedia.org/wiki/Joule%E2%80%93Thomson_effect). I
don't claim to understand this effect very thoroughly, but it is another
mechanism for cooling when air is let out of a well insulated valve.
I've seen claims both ways as to which process is actually responsible
for cooling.
Fortunately, a simple experiment suggests itself. Helium heats up
through the Joule-Thomson effect (when it starts abot \~50K). It will
cool down through the above described adiabatic cooling. So, fill a bike
tire with Helium gas, and let it out. See if the valve/gas feels hot or
cold. This will determine the dominant effect. As an experimentalist,
this [appeals greatly to me](http://www.brightlywound.com/?comic=42).
But if any theorists out there have ideas, please speak up.
