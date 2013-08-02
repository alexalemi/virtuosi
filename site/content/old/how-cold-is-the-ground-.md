Title: How Cold is the Ground?
Date: 2012-05-18 00:20:00
Tags: 
Category: old
Slug: how-cold-is-the-ground-
Author: Brian


It snowed in Ithaca a few weeks ago. Which sucked. But fortunately, it
had been warm for the previous few days, and the ground was still warm
so the snow melted fast. Aside from letting me enjoy the absurd
arguments against global warming that snow in April birthed, this got me
thinking: How cold is the ground throughout the year? At night vs.
during the day? And the corollary: How cold is my basement? If I dig a
deeper basement, can I save on heating and cooling? (I'm very cheap.)
Well, we want to know the temperature distribution *T* of the ground as
a function of time *t* and position *x*. So some googlin' or previous
knowledge shows that we need to solve the [heat
equation](http://en.wikipedia.org/wiki/Heat_equation). For our purposes,
we can treat the Earth as flat (I don't plan on digging a basement deep
enough to see the curvature of the Earth), so we can assume the
temperature only changes with the depth into the ground *x*: $$ \frac
{\partial T}{\partial t} = a \frac {\partial^2 T} {\partial x^2}
\qquad (1) $$ where *a* is the thermal diffusivity of the material, in
units of square meters per second. It looks like we're going to have to
solve some partial differential equations! Or will we? We can get a very
good estimate of how much the temperature changes with depth just by
dimensional analysis. Let's measure our time *t* in terms of a
characteristic time of our problem *w* (it could be 1 year if we were
trying to see the change in the ground's temperature from summer to
winter, or 1 day if we were looking at the change from day to night).
Then we can write: $$ \frac {\partial T } {\partial t} = \frac 1 w
\frac {\partial T} {\partial t/w} $$ ... plugging this in Eq. (1),
rearranging, and calling *l*= sqrt(*w*a*) gives.... $$ \frac
{\partial T}{\partial (t/w)} = \frac {\partial ^2 T} {\partial (x/
l )^2} $$ Now let's say we didn't know how to or didn't want to solve
this equation. (Don't worry, we do & we will). From rearranging this
equation, we see right away there is only one "length scale" in the
problem, *l*. So if we had to guess, we could guess that the ground
changes temperature a distance *l* into the ground. A quick look at
Wikipedia for [thermal
diffusivities](http://en.wikipedia.org/wiki/Thermal_diffusivity) gives
us the following table, for materials we'd find in the ground:
Material
*a*, mm^2/s
*l* (cm), *w* = 1 day
*l* (cm), *w* = 1 year
Polycrystalline Silica (glass, sand)
0.83
27 cm
5.1 meters
Crystalline Silica (quartz)
1.4
35
6.6
Sandstone
1.15
32
6.0
Brick
0.52
21
4.0
[Soil](http://soilphysics.okstate.edu/software/SoilTemperature/document.pdf)
0.3-1.25
16-33
3.1-6.3
So we would expect that the temperature of the ground doesn't change
much on a daily basis a foot or so below the ground, and doesn't change
ever about 15-20 feet into the ground. Just to pat ourselves on the back
for our skills at dimensional analysis, a quick check shows that
[permafrost](http://en.wikipedia.org/wiki/Permafrost#Time_to_form_deep_permafrost)
penetrates 14.6 feet into the ground after 1 year. So our dimensional
estimates looks pretty good! In the next few days I'll solve this
equation exactly and throw up a few pretty graphs, and maybe talk a
little about PDE's and Fourier series in the process.
