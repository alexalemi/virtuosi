Title: A Homemade Viscometer I
Date: 2012-07-24 22:32:00
Tags: 
Category: old
Slug: a-homemade-viscometer-i
Author: Brian


Stirring a bowl of honey is much more difficult than stirring a bowl of
water. But why? The mass density of the honey is about the same as that
of water, so we aren't moving more material. If we were to write out
Newton's equation, *ma* would be about the same, but yet we still need
to put in much more force. Why? And can we measure it? The reason that
honey is harder to stir is of course that the drag on our spoon depends
on more than just the density of the fluid. The drag also depends on the
viscosity of the fluid -- loosely speaking, how thick it is -- and the
viscosity of honey is about 400 times that of water, depending on the
conditions. In fact, a quick perusal of the Wikipedia article on
[viscosity](http://en.wikipedia.org/wiki/Viscosity) shows that
viscosities can vary by a fantastic amount -- some 13 orders of
magnitude, from easy-to-move gases to [thick pitch that behaves like a
solid except](http://en.wikipedia.org/wiki/Pitch_drop_experiment) on
long time scales. The situation is even more complicated than this, as
some fluids can have a [viscosity that changes depending on the
flow](http://en.wikipedia.org/wiki/Non-Newtonian_fluid). I wanted to
find a way to measure the viscosities of the stuff around me, so I made
the [viscometer](http://en.wikipedia.org/wiki/Viscometer) pictured below
for about $1.75 (the vending machines in Clark Hall are pretty
expensive). How? Well, I

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://1.bp.blogspot.com/-3R2mNiV_-KY/UA4pOLSKLSI/AAAAAAAAABA/X4MHVcrh93M/s400/DSCF4438.JPG)](http://1.bp.blogspot.com/-3R2mNiV_-KY/UA4pOLSKLSI/AAAAAAAAABA/X4MHVcrh93M/s1600/DSCF4438.JPG)
  My homemade viscometer, taking data on the viscosity of water.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Enjoyed the crisp, refreshing taste of Diet Pepsi from a 20 oz
    bottle (come on, sponsorships).
2.  Cut the top and bottom off the bottle, so all that was left was a
    straight tube.
3.  Mounted the bottle with on top of a small piece of flat plastic.
4.  Mounted a single-tubed coffee stirrer horizontally out of the bottle
    (I placed the end towards the middle of the bottle to avoid end
    effects).
5.  Epoxied or glued the entire edge shut.
6.  Marked evenly-spaced lines on the side of the bottle.

I can load my "sample" fluid in the top of the Pepsi bottle, and time
how long it takes for the sample level to drop to a certain point. A
more viscous fluid will take more time to leave the bottle, with the
time directly proportional to the viscosity. (This is a consequence of
Stokes flow and the equation for flow in a pipe. It will always be true,
as long as my fluid is viscous enough and my apparatus isn't too big.)
So we're done! All we need to do is calibrate our viscometer with one
sample, measure the times, and then we can go out and measure stuff in
the world! No need to stick around for the boring calculations! We can
do some fun science over the next few blog posts! But this is a physics
blog written by a bunch of grad students, so I'm assuming that a few of
you want to see the details. (I won't judge you if you don't though.) If
we think about the problem for a bit, we basically have flow of a liquid
through a pipe (i.e. the coffee stirrer), plus a bunch of other crap
which hopefully doesn't matter much. We first need to think about how
the fluid moves. We want to find the velocity of the fluid at every
position. This is best cast in the language of vector calculus -- we
have a (vector) velocity field ***u*** at a (vector) position ***x***.
There are two things we know: 1) We don't (globally) gain or lose any
fluid, and 2) Newton's laws *F=ma* hold. We can write these equations as
the Navier-Stokes equations: $$ \\vec{\\nabla}\\cdot \\vec{u} = 0 \\quad
(1) $$ $$ \\ \\rho \\left( \\frac {\\partial \\vec{u}} {\\partial t} +
(\\vec{u}\\cdot\\vec{\\nabla})\\vec{u} \\right) = - \\vec{\\nabla}p +
\\eta \\nabla\^2 \\vec{u} \\quad (2) $$ The first equation basically
says that we don't have any fluid appearing or disappearing out of
nowhere, and the second is basically *m**a**=**F***, except written per
unit volume. (The fluid's mass-per-unit-volume is *rho*, the rate of
change of our velocity is *d**u**/dt*, and our force per unit volume is
***grad**(p)*, plus a viscous term *laplacian(**u**)*. The only
complication is that *d**u**/dt* is a total derivative, which we need to
write as *d**u**/dt + d**u**/d**x**\*d**x**/dt*.) I won't drag you
through the [gory
details](http://www.4shared.com/office/y9ay-fNh/Homemade_viscometer_-gory_sect.html?refurl=d1url),
unless you want to see them, but it turns out that for my system the
height of the fluid *h* (measured from the coffee stirrer) versus time
*t* is $$ h(t) = h(0)e\^{- t/T}, \\quad T= 60.7 \\textrm{sec} \\times
[\\eta / \\textrm{1 mPa\*s}] \\times [\\textrm{ 1 g/cc} / \\rho] $$ [For
my viscometer, the coffee stirrer has length 13.34 cm and inside
diameter 2.4 mm, and the Pepsi bottle has a cross-sectional area of 36.3
square centimeters (3.4 cm inner radius). You can see how the timescale
scales with these properties in the [gory details
section](http://www.4shared.com/office/y9ay-fNh/Homemade_viscometer_-gory_sect.html?refurl=d1url).]

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://1.bp.blogspot.com/-RsGC2KaafVA/UA4pwpCbz6I/AAAAAAAAABI/S740sriRWg4/s400/5.png)](http://1.bp.blogspot.com/-RsGC2KaafVA/UA4pwpCbz6I/AAAAAAAAABI/S740sriRWg4/s1600/5.png)
  A run with measured heights vs times & error bars. The majority of the uncertainty turns out to come from not knowing the exact proportions of the viscometer. I don't know exactly why the heights are systematically deviating from the fit, but I suspect it's that my gridlines aren't perfectly lined up with the bottom of my viscometer (it looks like \~5 mm off would do it, which I can totally believe looking at the picture of my viscometer). However, because of the linearity of the equations for steady flow in a pipe, we know that the time scales linearly with the viscosity, so we should be able to accurately measure relative viscosities.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Well, how well does it work? Above is a plot of the height of water in
my viscometer versus time, with a best-fit value from the equations
above. To get a sense of my random errors (such as how good I am at
timing the flow), I measured this curve 5 separate times. If I take into
account the uncertainties in my apparatus setup as systematic errors, I
find a value for my viscosity as $$ \\eta \\approx 1.429 \\textrm{mPa\*
s} \\pm 0.5 \\% \\textrm{Rand.} \\pm 55\\% \\textrm{Syst.} $$ The actual
value of the viscosity of water at room temperature (T=25 C) is about
0.86 mPa\*s, which is more-or-less within my systematic errors. So it
looks like I won't be able to measure absolute values of viscosity
accurately without a more precise apparatus. But if I look at the
variation of my measured viscosity, I see that I should probably be able
to measure changes in viscosity to 0.5% !! That's pretty good! Hopefully
over the next couple weeks I'll try to use my viscometer to measure some
interesting physics in the viscosity of fluids.
