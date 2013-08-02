Title: The malleability of theory
Date: 2010-04-13 17:18:00
Tags: office hours, EM
Category: old
Slug: the-malleability-of-theory
Author: Yariv


There were some undergrads in my office for office hours the other day,
asking questions for the midterm. I'm teaching the engineering course on
optics and waves (also known as Things that go Sine) and the students
were looking at a problem dealing with quarter-wave plates. A
quarter-wave plate, the question goes, is a kind of optical instrument
that turns light with linear polarization into circular polarization.
Show, it continues, that it also turns light with circular polarization
linear. After a minute or two of discussing how a quarter-wave plate
work ("what, does it act differently on different axes?" giggled one,
and everybody gasped when I said yes) we went to the math. I wrote down
the equations for light with linear and circular polarization, $$ E\_0
\\hat{x} \\cos\\left(kz-\\omega t\\right) \\to
\\frac{E\_0}{\\sqrt{2}}\\hat{x}\\cos\\left(kz-\\omega t\\right) +
\\frac{E\_0}{\\sqrt{2}}\\hat{y}\\sin\\left(kz-\\omega t\\right) $$ with
a little arrow in between them to signify that the quarter-wave plate
turns one into the other. This was acceptable, so we continued. What
happens when light with circular polarization enters the plate? Well, we
start out the other way:
$$\\frac{E\_0}{\\sqrt{2}}\\hat{x}\\cos\\left(kz-\\omega t\\right) +
\\frac{E\_0}{\\sqrt{2}}\\hat{y}\\sin\\left(kz-\\omega t\\right) $$ and
then break it up into components. The first term obviously behaves
exactly the same as in the previous case,
$$\\frac{E\_0}{\\sqrt{2}}\\hat{x}\\cos\\left(kz-\\omega t\\right) \\to
\\frac{E\_0}{2}\\hat{x}\\cos\\left(kz-\\omega t\\right) +
\\frac{E\_0}{2}\\hat{y}\\sin\\left(kz-\\omega t\\right) $$ while the
second term is easy to extrapolate from there,
$$\\frac{E\_0}{\\sqrt{2}}\\hat{y}\\sin\\left(kz-\\omega t\\right) \\to
-\\frac{E\_0}{2}\\hat{x}\\cos\\left(kz-\\omega t\\right) +
\\frac{E\_0}{2}\\hat{y}\\sin\\left(kz-\\omega t\\right) $$ and adding
them both up, we get on the other side of the quarter-wave plate
$$E\_0\\hat{y}\\sin\\left(kz-\\omega t\\right)$$ a linearly polarized
wave. Simple, right? Almost simple. There's one trick in there, which
you may have noticed if you were following. My student noticed it - but
she's a clever one - and she asked me why I put that minus sign in the
second transformation equation. And my honest answer was that I put it
there to get the result I wanted. Sure, I can back it up with more math
(handedness, or maybe I can figure it out by redrawing the axes) but
when I was writing those equations on the board, I put that minus sign
there because I was expecting a certain result. And really, we do this
all the time. The math isn't neutral; it's an ally (or an enemy,
sometimes) that we're bending to get the result we want - because of
intuition, because of a previous results, because this is a homework
problem with a known solution - or because we have an experimental
result that we really want to be in accord with. This isn't a problem,
necessarily. Sometimes it leads us to wrong results, sometimes it helps
us reach the correct ones. It usually makes our life easier, and
sometimes makes them a lot harder. Keeping this bias in mind when we do
our math should hopefully lead to more of the first and less of the
second.
