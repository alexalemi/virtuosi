Title: Freezing in Space II - Turn On The Sun!
Date: 2010-05-13 23:38:00
Tags: power, space, freeze, blackbody, radiation, human
Category: old
Slug: freezing-in-space-ii-turn-on-the-sun-
Author: Jesse


Yesterday I considered how long it would take a human to [freeze in
space](http://thevirtuosi.blogspot.com/2010/05/freezing-in-space-i-blackest-night.html).
However, I considered only what would happen if you were not absorbing
any radiation from nearby sources. Today we consider what happens if you
do have hot objects nearby. Namely, the sun. The sun provides a lot of
energy, even as far away from it as we are. It keeps the earth at a
comfortable \~20 C, good for us humans, and provides the energy for life
on earth, also good for us humans. That's a lot of energy. So maybe the
sun can keep you alive when you're adrift in space. Or at least keep you
warm. I still think you'll asphyxiate. From here on out we're going to
assume that we are adrift in space near earth. You were out for a
joyride in that new spaceship of yours and something went horribly
wrong. We could go through a whole song and dance of calculating how
much power the sun delivers to the earth, but we won't (if you're
interested, let me know, an I can do that later). Instead, we'll quote
the known result, that the sun delivers \~1370W/m^2 in the vicinity of
the earth. To find out what temperature we would cool to we set the
power we absorb from the sun equal to the power we radiate
$$P_{sun}=P_{rad}$$
$$1370W/m^2*A_{ab}*e_{ab}=e_{rad}*A_{rad}*\sigma*T^4$$ Where
A_ab is the surface area absorbing the suns power, e_ab is a factor
between 0 and 1 that indicates how much of the incident power we
actually absorb, and e_rad is the emissivity of us, while A_rad is our
radiating area. Note that the emitting and absorbing areas are not the
same! Take a simple example. If you put a sheet in space, and face the
flat side towards the sun, it will only absorb energy from the sun on
one side, but it will radiate energy from both sides. Likewise e_ab and
e_rad are not necessarily equal because we are radiating and absorbing
at different wavelengths. We can solve the above equation for T, giving
$$T=\left(\frac{A_{ab}}{A_{rad}}\right)^{1/4}\left(\frac{e_{ab}}{e_{rad}}\right)^{1/4}\left(\frac{1370W/m^2}{\sigma}\right)^{1/4}$$
For a first pass, we'll make the simplifying assumption that
e_ab=e_rad. Given this,
$$T=394K*\left(\frac{A_{ab}}{A_{rad}}\right)^{1/4}$$ Now, the
absorption area of an object is just the shape of the object flattened
into the plane the incident radiation is perpendicular to. That is, the
absorption area of a sphere is a circle (a sphere projected to 2D is
always a circle), while the absorption area of a cylinder could be a
sheet or a circle, or something stranger. The best area ratio we can
ever have is that of a flat sheet, which gives 1/2. For a sphere, like
the earth, the ratio is 1/4. As an aside, this gives an equilibrium
temperature of the earth as \~5C, which is too cold. It turns out that
we shouldn't neglect either the emissivity ratio or the natural
greenhouse effect in the case of the earth. Now, we need to figure out
the area ratio for us. In a [previous
post](http://thevirtuosi.blogspot.com/2010/05/human-radiation.html) I
modeled myself as a cylinder with height 1.8 m and radius .14 m. Let us
assume we are facing the sun dead on, beating down on our chests. This
gives the cross sectional area of a sheet with width 2*.14 m =.28 m and
height 1.8 m. This is an area of .5 m^2, while my total surface area is
1.7 m^2. This gives an area ratio of \~.3, or an equilibrium
temperature of $$T=394K*(.3)^{1/4}\approx292K$$ That is an
equilibrium temperature of 19 C. Not too cold, but certainly not body
temperature! So the sun will not save us. We also have to factor in the
fact that we reflect better in the visual that we do in the infrared, so
the emissivity ratio we set to 1 probably is less than that, reducing
our equilibrium temperature even more. It is interesting to note,
though, that if we model a human as a two sided sheet instead of a
cylinder, we can bring our equilibrium temperature up to 331 K. That's
\~58 C! So in our model our geometrical assumptions change whether or
not we freeze or die of heat stroke. Finally, since it looks like the
sun may not save us, lets see how much it might slow down our
temperature loss. Instead of a net loss of 860W at body temperature, as
we calculated yesterday, sticking with our cylindrical human we'll have
a net loss of $$860W-1370W/m^2(.5m^2)=175W$$ Similarly at our lowered
body temperature of \~30 C, we'll be losing a net of \~105 W. Once again
taking a geometric average gives an average power loss of \~135 W. Using
the energy to cool we found yesterday it would take 16300 s, or 4.5
hours to freeze! Also note that if you're getting too hot or cold, given
how much the geometry plays into things, by changing your orientation to
the sun you'll be able to have a certain amount of control over how much
you heat up or cool down. Also, make sure you rotate yourself so that
you end up evenly heated, and not roasted on one side and frozen on the
other!
