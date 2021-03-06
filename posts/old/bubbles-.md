<--
.. title: Bubbles!
.. date: 2010-04-13 15:33:00
.. tags: interference, bubbles, thin films
.. category: old
.. slug: bubbles-
.. author: Matt
.. has_math: true
-->


[![image](http://3.bp.blogspot.com/_qY9DSyjj8Ro/S8TMvnGGX6I/AAAAAAAABzU/_o0PHaRQLmg/s320/good-small.jpg)](http://3.bp.blogspot.com/_qY9DSyjj8Ro/S8TMvnGGX6I/AAAAAAAABzU/_o0PHaRQLmg/s1600/good-small.jpg)
Ever wonder why don't you see a standard rainbow when looking at a thin
film such as soap stretched across a membrane ready for bubble making?
Well, I encountered this problem when I presented my intro physics
section with a quiz question today. Properly stated, the question was...
"Suppose white light is incident on a thin film (a soap bubble of
n=1.33) hanging vertically inside of a square loop. The minimum
thickness of the film at the top of the loop is 900nm and it increases
linearly (due to gravity) to 1300nm by the bottom of the loop which is
10cm away. This means that the thickness as a function of distance from
the top of the loop is
$$ d(x) = \text{900nm} + \text{400nm} * \left(
\frac{x}{\text{10cm}} \right) $$
What wavelengths will be most strongly reflected as a function of
distance along our bubble film?"
So I got to thinking - don't the partially interfering wavelengths also
contribute to the image that our eyes see? Isn't there a better mass
profile to use such as an exponential? Linear is just silly.
As for the first question, if you consider a single ray entering the
thin film and reflecting off both the first interface as well as the
second, then there is a phase difference between the two reflected
waves,
$$ \Delta \phi = \pi + 2\pi * \frac{2d}{\lambda} $$
where d is the thickness of the film and lambda is the wavelength. If we
consider these two waves as two standing waves added together with a
phase then we see that the superposition of their electric fields, for
example, is
$$ E_{tot} = E_0 \cos(\omega t) + E_0 \cos(\omega t + \Delta
\phi) $$
$$ E_{tot} = E_0 \sin(\omega t) \cos(\Delta \phi) $$
The intensity that our eyes see then goes like the square of this giving
an effective damping to certain wavelengths as given by
$$ \delta = \cos^2(\Delta \phi) $$
Using a more realistic exponential mass profile and this damping factor
for wavelengths in the visible spectrum, I created the top image using
OpenIL (maybe it's called DevIL, hard to say).
