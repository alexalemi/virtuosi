Title: Problem of the Week #1
Date: 2010-11-05 19:39:00
Tags: problem of the week, gravity
Category: old
Slug: problem-of-the-week-1
Author: Holmes


*I thought we could spice things up a bit with a more interactive post
on The Virtuosi. Starting this week, a new problem of the week will be
posted each week. Solutions will be posted the following week. These
problems will be a collection of physics and math problems and riddles,
and although hopefully challenging enough to be fun and interesting,
they should mostly be solvable using concepts from introductory
undergraduate physics and math classes.*
*We welcome you to ponder these problems, and send in solutions, or even
any ideas you have about how to solve the problems
to*[*the.physics.virtuosi@gmail.com*](mailto:the.physics.virtuosi@gmail.com)*with
“problem of the week” in the subject line. We will keep track of the top
Virtuosi problem solvers.*
*Here it goes…***Maximizing Gravity**
**
You are given a blob of Play-Doh (with a fixed mass and uniform density)
that you can shape however you choose. How can you shape it to maximize
the gravitational force at a given point *P* on the surface of the
Play-Doh?
Solution
In cylindrical coordinates, where the point P is taken to be the origin,
the z-component of the gravitational field due to any point (s, z) felt
at the origin, is proportional to
$$\frac{1}{s^{2}+z^{2}}\frac{z}{\sqrt{s^{2}+z^{2}}},$$
where the second factor is necessary to take the z-component. If we have
azimuthal symmetry, the magnitude of the gravitational field is given by
the sum of all the z-components of the forces due to all points in the
planet. For a given contour
$$\frac{z}{\left(s^{2}+z^{2}\right)^{3/2}}=C,$$
[![image](http://3.bp.blogspot.com/_kdZd6FJQtZQ/TN9Jgv8f9gI/AAAAAAAAAAM/qdRknJVbCT0/s320/maxgravity.jpg)](http://3.bp.blogspot.com/_kdZd6FJQtZQ/TN9Jgv8f9gI/AAAAAAAAAAM/qdRknJVbCT0/s1600/maxgravity.jpg)
for some constant C, each point on the interior contributes more to the
total gravitational field than each point on the exterior. Thus, the
gravitational field is maximized if the surface of the planet takes the
shape of one of these contours. Solving for s(z), we
get$$s\left(z\right)=\sqrt{\left(\frac{z}{C}\right)^{2/3}-z^{2}}.$$
If the length of the planet in the z-direction is $$z_0,$$ we can
replace C in the above expression to get
$$s\left(z\right)=\sqrt{\left(z_{0}^{4}z^{2}\right)^{1/3}-z^{2}}.$$
As can be seen by the plot above, this shape looks a lot like a sphere,
but slightly smushed toward the point of interest P. We can rigorously
compare the field of the maximal gravity solid to that of a sphere with
the same volume. The volume of the maximal solid is given by
$$V=\pi\int_{0}^{z_{0}}s^{2}\left(z\right)dz=\pi\int_{0}^{z_{0}}\left[\left(z_{0}^{4}z^{2}\right)^{1/3}-z^{2}\right]dz=\frac{4\pi}{15}z_{0}^{3}$$
The volume of a sphere of radius r is of course $$V=\frac{4}{3}\pi
r^{3},$$ so in order for the volumes to be the same, the sphere must
have a radius of $$r=z_{0}/5^{1/3}.$$
The acceleration due to the maximal solid is proportional to
$$a_{max}=\int dVa_{z}=2\pi
G\rho\int_{0}^{z_{0}}dz\int_{0}^{s\left(z\right)}sds\frac{z}{\left(s^{2}+z^{2}\right)^{3/2}}=\frac{4\pi
G\rho z_{0}}{5},$$
while the acceleration due to the sphere is just
$$a_{sphere}=\frac{G\rho\frac{4}{3}\pi r^{3}}{r^{2}}=\frac{4\pi
G\rho z_{0}}{3\cdot5^{1/3}}.$$
Thus, we have
$$\frac{F_{max}}{F_{sphere}}=\frac{4\pi G\rho z_{0}/5}{4\pi
G\rho
z_{0}/\left(3\cdot5^{1/3}\right)}=\frac{3}{5^{2/3}}\approx1.026.$$
So the solid that gives the maximum gravitational field at a point is
only about 3% better than a sphere.
For a more detailed discussion, see [Alemi's
solution](http://pages.physics.cornell.edu/%7Eaalemi/random/planet.pdf).
