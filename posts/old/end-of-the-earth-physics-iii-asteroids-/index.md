<--
.. title: End of the Earth Physics III- Asteroids!
.. date: 2010-04-22 18:45:00
.. tags: bruce willis, dinosaur, scott bakula, asteroid
.. category: old
.. slug: end-of-the-earth-physics-iii-asteroids-
.. author: Corky
.. has_math: true
-->


[![image](http://1.bp.blogspot.com/_fa6AZDCsHnY/S9EZLq8fRRI/AAAAAAAAAAc/pg5n-zg70QE/s200/armageddon.jpg)](http://1.bp.blogspot.com/_fa6AZDCsHnY/S9EZLq8fRRI/AAAAAAAAAAc/pg5n-zg70QE/s1600/armageddon.jpg)No
day of earth destroying celebration would be complete without that
apocalyptic all-time favorite: the asteroid. And to be fair, it deserves
to be the favorite. Of all the doomsday predictions out there (nuclear
holocaust for the cynics, death by snoo-snoo for the optimists) it is
the only one that is just about certain to occur at some point in the
geological near future. On top of that, it's one that we could
potentially avoid with enough time and some [neat
ideas](http://en.wikipedia.org/wiki/Asteroid_deflection_strategies) .
Let's model an asteroid impact on the earth. We will assume an asteroid
starting from rest at infinity and falling to the surface of the earth
due to earth's gravity only. Now obviously these assumptions are not
exactly correct. We can imagine our asteroid not starting from rest or
feeling some force due to the sun. Each of these would certainly change
our answer, but should still be within an order of magnitude of our
result. By conservation of energy, we have that $$ \text{KE}_{i} +
\text{PE}_{i} = \text{KE}_{f} + \text{PE}_{f} $$ Plugging in the
formulas for kinetic and potential energy, we have $$
\frac{1}{2}m{v_i}^{2} + \frac{-GM_{\oplus}m_a}{{r_{i}}} =
\text{KE}_f + \frac{-GM_{\oplus}m_a}{{r_{f}}}$$ Now, plugging in
our initial conditions of starting at rest at infinity and rearranging,
we have that $$ \text{KE}_f =
\frac{GM_{\oplus}m_a}{{R_{\oplus}}} $$ Assuming that all of this
kinetic energy is deposited into the earth as heat, we have that our
total energy added to the earth is $$ \text{E} =
\frac{GM_{\oplus}m_a}{{R_{\oplus}}} = \frac{(7 \times 10^{-11}
J m kg^{-2})(6 \times 10^{24} kg)}{6 \times 10^{6} m}m_a \approx
(10^{8} J)(\frac{m_a}{1kg}) $$ Now let's consider an asteroid made
out of iron. Iron is about 10 times denser that water so it has a
density of 10^4 kg/m^3. If our asteroid is a sphere, we can find its
radius given $$ m_a = \frac{4}{3} \pi {R_a}^{3} \rho $$ Plugging
this into our energy equation gives energy as a function of asteroid
radius: $$ \text{E} \approx (4 \times 10^{8} J) \times (
\frac{R_a}{1m} )^{3} $$. Now we have the energy released during an
asteroid impact in terms of either the size or the mass. So let's do
some destruction. We have heard in the last decade or so that even
relatively small changes in average global temperatures can result in
catastrophe. So let's see how big of an asteroid we would need to
deposit enough energy to raise global temperatures by 1 degree (NOTE:
this is very much a toy model. For a more realistic and sadistically
addicting model, check out
[this](http://www.lpl.arizona.edu/impacteffects/) site). To do this,
let's pretend increasing global temperatures is the same as increasing
ocean temperatures. Since water has a much much higher specific heat
than air, this seems like a reasonable assumption. Plus, we have already
made this calculation before. In the first End of the Earth post a bit
ago, we found that the amount of energy required to raise the
temperature of the world's oceans by 100 degrees is $$ E_{\text{100}}
\approx 10^{26} J $$ Since the scaling is linear, we can see that the
energy to heat up the oceans by 1 degree is just one hundredth of this
value, or $$ E_{\text{heat}} \approx 10^{24} J $$ So how big of an
asteroid is this? Using our equation from before, setting E = Eheat, we
have that $$ R_a = \frac{E_\text{heat}}{4 \times 10^{8} J m^{-1}}
= (\frac{10^{24}}{4 \times 10^8})^{1/3}m = (2.5)^{1/3}
\times{10^5}m \approx 100 km $$ For comparison, the asteroid that
killed the dinosaurs was thought to be about 30 km or so. This is a big
rock. FUN FACT FINALE: We all know that an asteroid killed the
dinosaurs. But what would happen if instead of an asteroid, we dropped a
dinosaur from infinity? According to wikipedia, a brontosaurus was about
30 tons which is about 30,000 kg. Using the equation for energy as a
function of mass derived earlier, we have that $$\text{E} = (10^{8}
J)(\frac{m_a}{1kg}) = 3 \times 10^{12} J \approx 1 \text{kiloton}
\text{TNT} $$ For comparison, the Hiroshima bomb was about 15 kilotons.
So to reproduce the Hiroshima energy yield we need about 15
brotosauruses falling from infinity.
