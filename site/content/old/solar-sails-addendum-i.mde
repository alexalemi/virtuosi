Title: Solar Sails Addendum I
Date: 2010-05-16 23:28:00
Tags: 
Category: old
Slug: solar-sails-addendum-i
Author: Corky


As requested, below is an explicit evaluation of the silly looking
integral in [Solar Sails
I](http://thevirtuosi.blogspot.com/2010/05/solar-sails-i.html). If you
just want some hints to do the integral, see [Solar Sails Addendum
II](http://thevirtuosi.blogspot.com/2010/05/solar-sails-addendum-ii.html).
Here we present a step-by-step solution of the differential equation: $$
\\frac{dr}{dt} = \\left[ \\frac{2\\alpha}{m} \\left( \\frac{1}{r\_0} -
\\frac{1}{r} \\right)\\right]\^{1/2} $$ This is just a separable
equation, so we rearrange to get an integral equation: $$
\\int\_{r\_0}\^{r\_f} \\frac{dr}{\\left[ \\frac{2\\alpha}{m} \\left(
\\frac{1}{r\_0} - \\frac{1}{r} \\right)\\right]\^{1/2}}
=\\int\_{0}\^{t}dt$$ We see that the right hand side here will just
evaluate to t. Let's rearrange the left hand side to get the integration
variable to be dimensionless. This is important because it allows the
integral to just be a number, with all the unit-dependent terms pulled
outside. So we have $$ \\int\_{r\_0}\^{r\_f} \\frac{dr}{\\left[
\\frac{2\\alpha}{mr\_0} \\left( 1 - \\frac{r\_0}{r}
\\right)\\right]\^{1/2}} =t$$ \\noindent Now we can do a change of
variables to get the dimensionless variable u = r/r0. This is just
giving us our distance in terms of our initial distance. In the problem
I took r\_0 to be 1 AU. So u just gives our distance now in terms of AU:
$$ \\int\_{1}\^{u\_f} \\frac{du}{\\left[ \\frac{2\\alpha}{m{r\_0}\^3}
\\left( 1 - \\frac{1}{u} \\right)\\right]\^{1/2}} =t$$ So lets set $$ k
= (m{r\_0}\^3}/{2 \\alpha)\^{1/2} ,$$ which just gives $$
k\\int\_{1}\^{u\_f} \\frac{du}{\\left[ \\left( 1 - \\frac{1}{u}
\\right)\\right]\^{1/2}} =t$$ Now we are ready to get started!
Typically, when I see something with a square root in the denominator
that's giving me trouble, I just blindly try trig substitutions. Let's
try u = [csc(x)]\^2, so 1/u = [sin(x)]\^2 and du = -(csc x)\^2 \* cot x,
and $$ \\int\_{1}\^{u\_f} \\frac{du}{\\left[ \\left( 1 - \\frac{1}{u}
\\right)\\right]\^{1/2}} =\\int\_{x\_0}\^{x\_f} \\frac{-2\\csc\^2x \\cot
x dx}{\\left(1-\\sin\^2x \\right)\^{1/2}} = \\int\_{x\_0}\^{x\_f}
-2\\csc\^3x dx ,$$ where x\_0 = pi/2 and x\_f = arcsin u\_f . The last
equality above just comes from simplifying the trig expressions. So now
how do we solve this "easier" problem? As a wise man once said, "When in
doubt, integrate by parts." So let's try that. Expanding out a bit we
see that: $$ -\\int\_{x\_0}\^{x\_f} \\csc\^3x dx =
\\int\_{x\_0}\^{x\_f}\\csc x \\left(-\\csc\^2x \\right)dx $$ Remembering
that integration by parts goes like $$ \\int u dv = uv - \\int v du $$
we can set u = csc x and v = \\cot x$ to get $$
\\int\_{x\_0}\^{x\_f}\\csc x \\left(-\\csc\^2x \\right)dx = \\csc x
\\cot x \\Big |\_{x\_0}\^{x\_f} - \\int\_{x\_0}\^{x\_f} \\cot x
\\left(-\\csc x \\cot x \\right) dx $$ which is just $$
-\\int\_{x\_0}\^{x\_f}\\csc\^3x dx = \\csc x \\cot x \\Big
|\_{x\_0}\^{x\_f} + \\int\_{x\_0}\^{x\_f} \\cot\^2 x \\csc x dx $$
Remembering that $$ \\cot\^2 x = \\csc\^2 x -1 ,$$ we have $$
-\\int\_{x\_0}\^{x\_f}\\csc\^3x dx = \\csc x \\cot x \\Big
|\_{x\_0}\^{x\_f} + \\int\_{x\_0}\^{x\_f} \\left(\\csc\^2 x - 1 \\right)
\\csc x dx $$ which we can expand to $$ -\\int\_{x\_0}\^{x\_f}\\csc\^3x
dx = \\csc x \\cot x \\Big |\_{x\_0}\^{x\_f} - \\int\_{x\_0}\^{x\_f}
\\csc x dx + \\int\_{x\_0}\^{x\_f} \\csc\^3 x dx$$ But this is just what
we want! Rearranging we now have that $$
-2\\int\_{x\_0}\^{x\_f}\\csc\^3x dx = \\csc x \\cot x \\Big
|\_{x\_0}\^{x\_f} - \\int\_{x\_0}\^{x\_f} \\csc x dx$$ Remembering that
the integral for csc is $$ \\int \\csc x dx =-\\ln | \\csc x + \\cot x|
+ C $$ and evaluating our limits we have that $$
-2\\int\_{x\_0}\^{x\_f}\\csc\^3x dx = \\csc x\_f \\cot x\_f - \\csc x\_0
\\cot x\_0 +\\ln \\left( \\frac{| \\csc x\_f + \\cot x\_f|}{| \\csc x\_0
+ \\cot x\_0|} \\right) $$ Now we just need to evaluate at x\_0 = pi/2
and x\_f = arcsin u\_f. We can draw a right triangle with far angle
x\_f, hypoteneuse of length sqrt{u}, and legs of length 1 and sqrt{u-1}
to see that csc x\_f = sqrt{u} and cot x\_f = sqrt{u-1}, so $$
-2\\int\_{x\_0}\^{x\_f}\\csc\^3x dx = \\sqrt{u}\\sqrt{u-1} + \\ln{ |
\\sqrt{u} + \\sqrt{u-1}|} $$ And this is what we have sought from the
beginning. Using the last two equations on the first page we see that $$
t = k\\int\_{1}\^{u\_f} \\frac{du}{\\left[ \\left( 1 - \\frac{1}{u}
\\right)\\right]\^{1/2}} = k\\left[-2\\int\_{x\_0}\^{x\_f}\\csc\^3x dx
\\right] = k \\left[\\sqrt{u}\\sqrt{u-1} + \\ln{ | \\sqrt{u} +
\\sqrt{u-1}|} \\right] $$ Plugging back in our value of k, we have $$ t
= \\left(\\frac{m{r\_0}\^3}{2\\alpha}
\\right)\^{1/2}\\left[\\sqrt{u}\\sqrt{u-1} + \\ln{ | \\sqrt{u} +
\\sqrt{u-1}|} \\right] $$ Simplifying a bit and dropping the absolute
value bars since u will always be bigger than u-1, we have our final
answer: $$ t = \\left(\\frac{m{r\_0}\^3}{2\\alpha}
\\right)\^{1/2}\\left[\\sqrt{u(u-1)} + \\ln{ \\left( \\sqrt{u} +
\\sqrt{u-1}\\right)} \\right] $$ where u = r / r\_0 is our
non-dimensional distance measurement. And this is (up to some
rearranging) exactly what we get in the initial post.
