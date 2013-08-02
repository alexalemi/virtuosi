Title: Solar Sails Addendum I
Date: 2010-05-16 23:28:00
Tags: 
Category: old
Slug: solar-sails-addendum-i
Author: Corky


As requested, below is an explicit evaluation of the silly looking integral in <a href="http://thevirtuosi.blogspot.com/2010/05/solar-sails-i.html">Solar Sails I</a>.  If you just want some hints to do the integral, see <a href="http://thevirtuosi.blogspot.com/2010/05/solar-sails-addendum-ii.html">Solar Sails Addendum II</a>.

<a name='more'></a>


Here we present a step-by-step solution of the differential equation:

$$ \frac{dr}{dt} = \left[ \frac{2\alpha}{m} \left( \frac{1}{r_0} - \frac{1}{r} \right)\right]^{1/2} $$

This is just a separable equation, so we rearrange to get an integral equation:

$$ \int_{r_0}^{r_f} \frac{dr}{\left[ \frac{2\alpha}{m} \left( \frac{1}{r_0} - \frac{1}{r} \right)\right]^{1/2}} =\int_{0}^{t}dt$$

We see that the right hand side here will just evaluate to t.  Let's rearrange the left hand side to get the integration variable to be dimensionless. This is important because it allows the integral to just be a number, with all the unit-dependent terms pulled outside.  So we have

$$ \int_{r_0}^{r_f} \frac{dr}{\left[ \frac{2\alpha}{mr_0} \left( 1 - \frac{r_0}{r} \right)\right]^{1/2}} =t$$

\noindent Now we can do a change of variables to get the dimensionless variable u = r/r0.  This is just giving us our distance in terms of our initial distance.  In the problem I took r_0 to be 1 AU.  So u just gives our distance now in terms of AU:

$$ \int_{1}^{u_f} \frac{du}{\left[ \frac{2\alpha}{m{r_0}^3} \left( 1 - \frac{1}{u} \right)\right]^{1/2}} =t$$


So lets set

$$ k = (m{r_0}^3}/{2 \alpha)^{1/2} ,$$

which just gives

$$ k\int_{1}^{u_f} \frac{du}{\left[ \left( 1 - \frac{1}{u} \right)\right]^{1/2}} =t$$

Now we are ready to get started!  Typically, when I see something with a square root in the denominator that's giving me trouble, I just blindly try trig substitutions.  Let's try u = [csc(x)]^2, so 1/u  = [sin(x)]^2 and du = -(csc x)^2 * cot x, and

$$ \int_{1}^{u_f} \frac{du}{\left[ \left( 1 - \frac{1}{u} \right)\right]^{1/2}} =\int_{x_0}^{x_f} \frac{-2\csc^2x \cot x dx}{\left(1-\sin^2x \right)^{1/2}} = \int_{x_0}^{x_f} -2\csc^3x dx ,$$

where x_0 = pi/2 and x_f = arcsin u_f .  The last equality above just comes from simplifying the trig expressions.  So now how do we solve this "easier" problem?  As a wise man once said, "When in doubt, integrate by parts."  So let's try that.  Expanding out a bit we see that:

$$ -\int_{x_0}^{x_f} \csc^3x dx = \int_{x_0}^{x_f}\csc x \left(-\csc^2x \right)dx $$

Remembering that integration by parts goes like

$$ \int u dv = uv - \int v du $$

we can set u = csc x and v = \cot x$ to get

$$ \int_{x_0}^{x_f}\csc x \left(-\csc^2x \right)dx = \csc x \cot x \Big |_{x_0}^{x_f} - \int_{x_0}^{x_f} \cot x \left(-\csc x \cot x \right) dx $$

which is just

$$ -\int_{x_0}^{x_f}\csc^3x dx = \csc x \cot x \Big |_{x_0}^{x_f} + \int_{x_0}^{x_f} \cot^2 x \csc x dx $$

Remembering that

$$ \cot^2 x = \csc^2 x -1 ,$$

we have

$$ -\int_{x_0}^{x_f}\csc^3x dx = \csc x \cot x \Big |_{x_0}^{x_f} + \int_{x_0}^{x_f} \left(\csc^2 x - 1 \right) \csc x dx $$

which we can expand to

$$ -\int_{x_0}^{x_f}\csc^3x dx = \csc x \cot x \Big |_{x_0}^{x_f} - \int_{x_0}^{x_f} \csc x dx + \int_{x_0}^{x_f} \csc^3 x dx$$

But this is just what we want!  Rearranging we now have that

$$ -2\int_{x_0}^{x_f}\csc^3x dx = \csc x \cot x \Big |_{x_0}^{x_f} - \int_{x_0}^{x_f} \csc x dx$$

Remembering that the integral for csc is

$$ \int \csc x dx =-\ln | \csc x + \cot x| + C $$

and evaluating our limits we have that

$$ -2\int_{x_0}^{x_f}\csc^3x dx = \csc x_f \cot x_f - \csc x_0 \cot x_0 +\ln \left( \frac{| \csc x_f + \cot x_f|}{| \csc x_0 + \cot x_0|} \right) $$

Now we just need to evaluate at x_0 = pi/2 and x_f = arcsin u_f.  We can draw a right triangle with far angle x_f, hypoteneuse of length sqrt{u}, and legs of length 1 and sqrt{u-1} to see that csc x_f = sqrt{u} and cot x_f = sqrt{u-1}, so


$$ -2\int_{x_0}^{x_f}\csc^3x dx = \sqrt{u}\sqrt{u-1} + \ln{ | \sqrt{u} + \sqrt{u-1}|} $$

And this is what we have sought from the beginning.  Using the last two equations on the first page we see that


$$ t = k\int_{1}^{u_f} \frac{du}{\left[ \left( 1 - \frac{1}{u} \right)\right]^{1/2}} = k\left[-2\int_{x_0}^{x_f}\csc^3x dx \right] = k \left[\sqrt{u}\sqrt{u-1} + \ln{ | \sqrt{u} + \sqrt{u-1}|} \right] $$

Plugging back in our value of k, we have

$$ t = \left(\frac{m{r_0}^3}{2\alpha} \right)^{1/2}\left[\sqrt{u}\sqrt{u-1} + \ln{ | \sqrt{u} + \sqrt{u-1}|} \right] $$

Simplifying a bit and dropping the absolute value bars since u will always be bigger than u-1, we have our final answer:

$$ t = \left(\frac{m{r_0}^3}{2\alpha} \right)^{1/2}\left[\sqrt{u(u-1)} + \ln{ \left( \sqrt{u} + \sqrt{u-1}\right)} \right] $$

where u = r / r_0 is our non-dimensional distance measurement.  And this is (up to some rearranging) exactly what we get in the initial post. 
<div>
</div>
