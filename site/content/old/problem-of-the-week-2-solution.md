Title: Problem of the Week #2: Solution
Date: 2010-11-23 17:46:00
Tags: problem of the week
Category: old
Slug: problem-of-the-week-2-solution
Author: Holmes


Thanks to all who sent in solutions! We are very happy with the vast
number of responses, and we will put up a leader board shortly! Solution
Let A be the fraction of the rubber band that the ant has traversed.
$$A\\left(t\\right)=\\frac{x\\left(t\\right)}{L+vt}.$$ The ant's
velocity relative to any point along the rubber band is equal to the
length of the rubber band times the first time derivative of A:
$$u=\\left(L+vt\\right)\\frac{dA}{dt}=\\left(L+vt\\right)\\left[\\frac{\\dot{x}}{L+vt}-\\frac{vx}{\\left(L+vt\\right)\^{2}}\\right]=\\dot{x}-\\frac{vx}{L+vt}.$$
This gives us an inseparable, first-order differential equation for
x(t). The general differential equation of this type,
$$\\dot{x}+p\\left(t\\right)x=q\\left(t\\right),$$ has the general
solution $$x\\left(t\\right)=e\^{-\\int\_{0}\^{t}
p\\left(t\\right)dt}\\int\_{0}\^{t} q\\left(t\\right)e\^{\\int\_{0}\^{t}
p\\left(t\\right)dt}dt.$$ In our case,
$$p\\left(t\\right)=-\\frac{v}{L+vt},\\quad q\\left(t\\right)=u.$$
Therefore, $$x\\left(t\\right)&=&e\^{\\int\\frac{v}{L+vt}dt}\\int
ue\^{-\\int\\frac{v}{L+vt}dt}dt=\\frac{u}{v}\\left(L+vt\\right)\\ln\\left(1+\\frac{vt}{L}\\right).$$
When the ant has reached the other side, x(t) = L + vt, so
$$x\\left(t\\right)=L+vt=\\frac{u}{v}\\left(L+vt\\right)\\ln\\left(1+\\frac{vt}{L}\\right).$$
Solving for t, we get $$t=\\frac{L}{v}\\left(e\^{v/u}-1\\right).$$ So
the ant always makes it to the other side (unless u = 0)! In the limit
as v -\> 0, we get $$t\\approx\\frac{L}{u},$$ which is exactly what we
would expect. We can show that the ant will reach the other side without
doing any calculations. As the ant moves across the rubber band, the
velocity of the point on the rubber band that the ant is currently
walking on increases from 0 to v. Therefore, the ant is accelerating.
Since the other end of the rubber band is moving at a constant velocity,
the accelerating ant will always eventually catch up to the far end.
Another way to see this is that since the ant is accelerating, if it
makes it halfway, it will make it all the way to the other side; if it
makes it one-quarter of the way, it will make it halfway, and so on. We
know that since the ant is traveling at some nonzero velocity, it must
make it some nonzero fraction of the way to the other side. Therefore,
it must make it twice that far, and so on, all the way to the other
side. Thanks to Frank for pointing this out!
