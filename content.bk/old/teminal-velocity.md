Title: Teminal Velocity
Date: 2010-08-11 14:04:00
Tags: analysis, guestimation, bike, wiki, equations
Category: old
Slug: teminal-velocity
Author: Yariv


The impetus for this post lies with three facts. First, I like to bike
to work. Second, Cornell sits on a
[hill](http://www.cornell.edu/search/index.cfm?tab=facts&q=&id=272). And
finally, I'm not very brave. As a result of all of these, along with
Ithaca's less-than-optimal road maintenance, my semi-daily rides home
tend to produce a lot of wear on my brakes as I cruise downhill at what
appears to me to be very high speeds. I began to ponder just how high
this speed really is, and if I could reduce my use of the brakes or if
I'm going to end up using them anyway at the bottom of the hill.
![image](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGLwOVisUAI/AAAAAAAACD4/V9TvWzmEv9k/s200/200px-Free_body.svg.png)

Figure 1: An inclined plane

So, I asked myself, what do I remember about bikes going down the hill?
Well, I remember the good old inclined plane (figure 1), and I remember
that air resistance is proportional to velocity, so that the equation of
motion is given by $$ ma = mg\sin\theta - \alpha v. $$ I had no idea
what α was, though. My first stop in considering it was naturally
Wikipedia. A quick
[search](http://en.wikipedia.org/wiki/Terminal_velocity) came up with
the formula $$m a = mg\sin\theta - \frac{1}{2}\rho A C_d v^2$$
where ρ is the density of air, A the projected area of the body and C~d~
the drag coefficient The first thing to notice here is that I was wrong
- drag in a fluid acts like the velocity squared, and not the velocity.
Second, we can easily determine terminal velocity out of this formula -
it's the speed at which the sum of the forces equals to zero, or $$v_t
= \sqrt{\frac{2mg\sin\theta}{\rho A C_d}}.$$ We can throw in some
numbers into that. ρ = 1.2 kg/m^3^ for air; Wikipedia estimates C~d~ =
0.9 for a [cyclist](http://en.wikipedia.org/wiki/Drag_coefficient). For
the mass, we need to add up mine (\~75 kg), the bike's (15-20 kg) and my
bag's (let's say 5 kg). We come to about 100 kg, give or take 5%. A is a
little harder to estimate, but height times width gives me an initial
guess of 0.62 m^2^, which I'll revise to 0.7 m^2^ to account for the
bike, flailing arms and fashionable helmet, up to about 10% accuracy.
We're left with sinθ, which varies by road, but in general we expect the
terminal velocity to look like $$v_t \approx \left(50 \pm 3
\rm{m/s}\right) \sqrt{\sin\theta}.$$ This appears not-unreasonable.
For an 8% grade like we have down University avenue this yields about 50
km/h and for a 13% grade like we have down Buffalo street this will
bring us up to a respectable 65
[km/h](http://www.blogger.com/post-edit.g?blogID=8807287158334608095&postID=6743488546064317383#miles "That's - sigh - about 30 mph and 40 mph, respectively, in crazy units").
Both, incidentally, are faster than I'm willing to go down a badly
maintained, not entire straight road. So we have some numbers, and I
begin to feel justified about pressing those breaks often, but all of
this is really an introduction for the next post, in which I go against
all my theorist instincts and take some data in the field. Stay tuned.

1.  [](http://www.blogger.com/post-edit.g?blogID=8807287158334608095&postID=6743488546064317383)That's
    - sigh - about 30 mph and 40 mph, respectively, in crazy units

