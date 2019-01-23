<--
.. title: Solar Sails Addendum II
.. date: 2010-05-16 23:27:00
.. tags: 
.. category: old
.. slug: solar-sails-addendum-ii
.. author: Corky
.. has_math: true
-->


This is the schematic version, if you just wanted hints. The full
solution is given in [Solar Sails Addendum
I](http://thevirtuosi.blogspot.com/2010/05/solar-sails-addendum-i.html).
Here we present a schematic solution of the differential equation: $$
\frac{dr}{dt} = \left[ \frac{2\alpha}{m} \left( \frac{1}{r_0} -
\frac{1}{r} \right)\right]^{1/2} $$ This is just a separable
equation, so we rearrange to get an integral equation: $$
\int_{r_0}^{r_f} \frac{dr}{\left[ \frac{2\alpha}{m} \left(
\frac{1}{r_0} - \frac{1}{r} \right)\right]^{1/2}} =
\int_{0}^{t}dt$$ From here it's nice to non-dimensionalize, so our
integration variable is just a number (with no units attached). This
allows us to get the integral into a form like $$ k\int_{1}^{u_f}
\frac{du}{\left[ \left( 1 - \frac{1}{u} \right)\right]^{1/2}} =
t$$ for appropriate values of k and u. Now we are ready to get started!
Typically, when I see something with a square root in the denominator
that's giving me trouble, I just blindly try trig substitutions. After
an appropriate trig substitution, we get something of the form $$
\int_{1}^{u_f} \frac{du}{\left[ \left( 1 - \frac{1}{u}
\right)\right]^{1/2}} = \int_{x_0}^{x_f} -2\csc^3x dx$$, So
now how do we solve this "easier" problem? As a wise man once said,
"When in doubt, integrate by parts." So let's try that. $$ \left[
\mbox{HINT:} -\int_{x_0}^{x_f} \csc^3x dx =
\int_{x_0}^{x_f}\csc x \left(-\csc^2x \right)dx \right]$$
Remembering that integration by parts goes like $$ \int u dv = uv -
\int v du $$ we can pick appropriate values of u and v to get something
nice, which eventually leads to $$ -\int_{x_0}^{x_f}\csc^3x dx =
\csc x \cot x \Big |_{x_0}^{x_f} - \int_{x_0}^{x_f} \csc x
dx + \int_{x_0}^{x_f} \csc^3 x dx$$ But this is just what we
want! Rearranging we now have that $$ -2\int_{x_0}^{x_f}\csc^3x
dx = \csc x \cot x \Big |_{x_0}^{x_f} - \int_{x_0}^{x_f}
\csc x dx$$ Evaluating our integrals, we see that $$
-2\int_{x_0}^{x_f}\csc^3x dx = \sqrt{u}\sqrt{u-1} + \ln{ |
\sqrt{u} + \sqrt{u-1}|} $$ And this is what we have sought from the
beginning. Plugging back in to our earlier equations and rearranging
gives $$ t = \left(\frac{m{r_0}^3}{2\alpha}
\right)^{1/2}\left[\sqrt{u(u-1)} + \ln{\left( \sqrt{u} +
\sqrt{u-1}\right)} \right] $$ where u = r / r_0 is our
non-dimensional distance measurement. And this is (up to some algebra)
exactly what we get in the initial post.
