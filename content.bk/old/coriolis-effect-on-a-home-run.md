Title: Coriolis Effect on a Home Run
Date: 2011-07-03 11:52:00
Tags: scott bakula, baseball, coriolis
Category: old
Slug: coriolis-effect-on-a-home-run
Author: Corky


  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://3.bp.blogspot.com/-LxzlQ5iNaaI/Ta458E_AwvI/AAAAAAAAAMc/D0Z4vZS7IzA/s320/phillies_stadium.jpg)](http://3.bp.blogspot.com/-LxzlQ5iNaaI/Ta458E_AwvI/AAAAAAAAAMc/D0Z4vZS7IzA/s1600/phillies_stadium.jpg)
  Citizen's Bank Park
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I like baseball. Well, technically, I like ~~laying~~[3] lying on the
couch for three hours half-awake eating potato chips and mumbling
obscenities at the television. But let's not split hairs here.
Anyway, out of curiosity and in partial atonement for the sins of my
past [1] I would now like to do a quick calculation to see how much
effect the Coriolis force has on a home-run ball.
The Coriolis force is one of the artificial forces we have to put in if
we are going to pretend the Earth is not rotating. For a nice intuitive
explanation of the Coriolis force see [this
post](http://www.wired.com/wiredscience/2011/04/coriolis-force-in-a-wipeout-rotating-slide/)
over at Dot Physics.
Let's now consider the following problem. Citizen's Bank Park (home to
the Philadelphia Phillies) is oriented such that the line from home
plate to the foul pole in left field runs essentially South-North.
Imagine now that Ryan Howard hits a hard shot down the third base line
(that is, he hits the ball due North). Assuming it is long enough to be
a home run, how with the Coriolis force effect the ball's trajectory?
This is a well-posed problem and we could solve it as exactly as we
wanted. But please don't [make
me](https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0Bwd5hrDOxWsrOGZmMWZkYzQtM2M2Ny00NjlmLTgyYmMtNTQwZjI1ODU1NWI4&hl=en_US).
It's icky and messy and I don't feel like it. So let's do some
dimensional analysis! Hooray for that!
So what are the relevant physical quantities in this problem? Well,
we'll certainly need the angular velocity of the Earth and the speed of
the baseball. We'll also need the acceleration due to gravity. Alright,
so what do we want to get out of this? Well, ideally we'd like to find
the distance the ball is displaced from its current trajectory. So is
there any way we can combine an angular velocity, linear velocity and
acceleration to get a displacement?
Let's see. We can write out the dimensions of each in terms of some
length, L, and some time, T. So:
$$ \left[ \Omega \right] = \frac{1}{T} $$
$$ \left[ v \right] = \frac{L}{T} $$
$$ \left[ g \right] = \frac{L}{T^2} $$
where we have used the notation that [some quantity] = units of that
quantity. Combining these in a general way gives: $$ L = \left[
v^{\alpha} \Omega^{\beta} g^{\gamma} \right] = \left(
\frac{L}{T}\right)^{\alpha}\left(
\frac{1}{T}\right)^{\beta}\left( \frac{L}{T^2}\right)^{\gamma}
= L^{\alpha+\gamma} T^{-(\alpha+\beta+2\gamma)}$$ Since we want
just want a length scale here, we need: $$\alpha+\gamma =
1\~\~\~\mbox{and}\~\~\~\alpha+\beta+2\gamma = 0. $$
We can fiddle around with the above two equations to get two new
equations that are both functions of alpha. This gives: $$\beta =
\alpha - 2\~\~\~\mbox{and}\~\~\~\gamma = 1 - \alpha. $$
Unfortunately, we have two equations and three unknowns, so we have an
infinite number of solutions. I've listed a few of these in the Table
below.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://4.bp.blogspot.com/-_wBdDaNzEP4/Tg_of5pylyI/AAAAAAAAANE/CU2Oe225_UI/s320/table.png)](http://4.bp.blogspot.com/-_wBdDaNzEP4/Tg_of5pylyI/AAAAAAAAANE/CU2Oe225_UI/s1600/table.png)
  Ways of getting a length
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

At this point, we have taken Math as far as we can. We'll now have to
use some physical intuition to narrow down our infinite number of
solutions to one. Hot dog! One way we can choose from these expressions
is to see which ones have the correct dependencies on each variable. So
let's consider what we would expect to happen to the deflection of our
baseball by the Coriolis force if we changed each variable. What happens
if we were to "turn up" the gravity and make g larger? If we make g much
larger, then a baseball hit at a given velocity will not be in the air
as long. If the ball isn't in the air as long, then it won't have as
much time to be deflected. So we would expect the deflection to decrease
if we were to increase g. This suggests that g should be in the
denominator of our final expression. What happens if we turn up the
velocity of the baseball? If we hit the ball harder, then it will be in
the air longer and thus we would expect it to have more time to be
deflected. Since increasing the velocity would increase the deflection,
we would expect v to be in the numerator. What happens if we turn up the
rotation of the Earth? Well, if the Earth is spinning faster, it's able
to rotate more while the ball is in the air. This would result in a
greater deflection in the baseball's path. Thus, we would expect this
term to be in the numerator. So, using the above criteria, we have
eliminated everything on that table with alpha less than 3 based on
physical intuition. Unfortunately, we still have an infinite number of
solutions to choose from (i.e. all those with alpha greater than or
equal to 3). But, we DO have a candidate for the "simplest" solution
available, namely the case where alpha = 3. Since we have exhausted are
means of winnowing down our solutions, let's just go with the alpha = 3
case. Our dimensional analysis expression for the deflection of a
baseball is then $$ \Delta x \sim \frac{v^3 \Omega}{g^2} $$
Plugging in typical values of $$ v =
50\~\mbox{m/s}\~\~\~(110\~\mbox{mi/hr}) $$ $$ \Omega = 7 \times
10^{-5}\~\mbox{rad/s} $$ $$ g = 9.8\~\mbox{m/s}^2 $$ we get $$
\Delta x \approx 0.1\~\mbox{m} = 10\~\mbox{cm}. $$ That's all fine
and good, but which way does the ball get deflected? Is it fair or foul?
Well, remembering that the Coriolis force is given by: $$ {\bf F} =
-2m{\bf \Omega} \times {\bf v} $$ and utilizing Ye Olde Right Hand
Rule, we see that a ball hit due north will be deflected to the East. In
the case of Citizen's Bank Park, that is fair territory. But how good is
our estimate? Well, I did the full calculation (which you can find
[here](https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0Bwd5hrDOxWsrOGZmMWZkYzQtM2M2Ny00NjlmLTgyYmMtNTQwZjI1ODU1NWI4&hl=en_US))
and found that the deflection due to the Coriolis force is given by $$
\Delta x =-\frac{4}{3}\frac{\Omega v^3_0}{g^2} \cos \phi
\sin^3 \alpha \left[1 -3 \tan \phi \cot \alpha \right] $$
where phi is the latitude and alpha is the launch angle of the ball. We
see that this is essentially what we found by dimensional analysis up to
that factor of 4/3 and some geometrical terms. Not bad! Plugging in the
same numbers we used before, along with the appropriate latitude and a
45 degree launch angle we find that the ball is deflected by: $$ \Delta
x = 5\~\mbox{cm}. $$ For comparison, we note that the diameter of a
baseball is 7.5 cm. So in the grand scheme of things, this effect is
essentially negligible. [2] That wraps up the calculation, but I'm
certain that many of you are still a little wary of this voodoo
calculating style. And you should be! Although dimensional analysis will
give you a result with the proper units and will *often* give you
approximately the right scale, it is not perfect. But, it can be
formalized and made rigorous. The rigorous demonstration for dimensional
analysis is due to Buckingham and his famous pi-theorem. The original
paper can be found behind a pay-wall
[here](http://prola.aps.org/abstract/PR/v4/i4/p345_1) and a really nice
set of notes can be found
[here](http://www.math.ntnu.no/~hanche/notes/buckingham/buckingham-a4.pdf).
It's a pretty neat idea and I highly recommend you check it out!
Unnecessary Footnotes:
[1] Once in college I argued with a meteorologist named Dr. Thunder over
the direction of the Coriolis force on a golf ball for the better half
of the front nine at Penn State's golf course. I was wrong. Moral of the
story: don't play golf with meteorologists.
[2] For a counterargument, see Fisk et al. (1975) [3] Text has been
corrected to illustrate our enlightenment by a former English major as
to the difference between 'lay' and 'lie' through the following story:
'Once in a college psych class, a young student said "It's too hot.
Let's lay down." A mature student, a journalist, asked, "Who's Down?" '
