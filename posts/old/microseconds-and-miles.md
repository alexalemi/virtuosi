<--
.. title: Microseconds and Miles
.. date: 2010-09-12 23:04:00
.. tags: dr. dre, GPS, scott bakula
.. category: old
.. slug: microseconds-and-miles
.. author: Corky
.. has_math: true
-->


The following is an unfinished manuscript found under heaps of rubble
and pizza boxes here at Virtuosi headquarters. It appears to be some
sort of screen play, though one would be hard-pressed to figure this out
solely from the script. The true giveaway was the 100 page addendum (not
published) full of potential titles and acceptance speeches. I dare not
bore you with these vanity pages in their entirety, but just for
completeness and posterity I include some samples.
For possible titles we have: "Dr. Dre, OR: How I Learned to Stop
Worrying and Love the Metric," "How to Teach Physics to your Dee Oh
Double G (West Coast Edition)," "Bring Da Ruckus: ODEs by ODB" and
"Flavor Flav's Flavor Physics...boooyeeeee!" among other even worse and
less relevant titles.
Among the acceptance speeches we have one that starts: "I would like to
thank the Academy, Scott Bakula and Chuck D. You know what you did.
Here's a song I wrote...", etc. It is all very painful.
There is almost no value to this document whatsoever, but it does
present a nice fun fact about GPS. The legible parts of the script are
thus presented below. The illegible parts appear to have been obscured
by some caustic mixture of Mountain Dew, pizza sauce and tears. ** *We
descend to the bottom of the abandoned mineshaft recently converted to
the headquarters of General Stanley K. Ripper. He is currently engaged
in a heated discussion with his science advisor, Dr. Vontavious Dre. We
join mid-sentence as a result of lazy writing...*
**
*DR. DRE: ...shortage of scientists! What's that? Yeah, you could
definitely call it a "chronic" shortage if you want. But semantics
aren't important right now. The "G"-sector needs more funding.*
**
*GEN. RIPPER: You are my most trusted science advisor, Dr. Dre, but you
already have one staff scientist...a Dr. Snoop Dogg, I believe...? How
many scientists do we need doing relativity here? This is the military!
We need Moonraker lasers and nuclear hand grenades. So no more funding
unless... That is, unless you figured out the...*
**
*DR. DRE: No sir, we still don't have a Stargate.*
**
*GEN. RIPPER: Well then you are just wasting my time! I want something
useful. Either something that goes boom or something that helps
something that goes boom. What I don't need is a theoretical money
drain.*
**
*DR. DRE: And how did you find your way to work today, sir?*
**
***GEN. RIPPER: What? You know very well I ride my horse, Neigh-braham
Lincoln. He knows how to get here.*
**
*DR. DRE: And how does Nifty 'Nabe know where to go...?*
**
*GEN RIPPER: GPS, of course!*
**
*DR. DRE: Bingo. That's our department. Without correcting for general
relativistic effects (the specialty of the "G"-sector, I may add), GPS
would be completely useless. Let me show you.*
**
*A large blackboard drops down from the ceiling and a slow steady beat,
just barely audible, seems to come from all directions. Dre writes the
following equation on the board:*
$$ ds^2 = -\left(1-\frac{R_s}{r} \right)c^2dt^2+ \left( 1 -
\frac{R_s}{r} \right)^{-1} dr^2 + r^2 \left( d{\theta}^2 +
{\sin\theta} {d\phi}^2 \right)$$
This equation gives the line element for a Schwarzschild metric. The
R_s in the equation is called the "Schwarzschild Radius" and is given
by
$$ R_s = \frac{2GM}{c^2} .$$
GEN RIPPER: Is that Karl Schwarzschild? I remember reading a delightful
biography of him somewhere...? Anyway, what the heck is this "line
element" thing...?
DR. DRE: Good question. Essentially what we get is the differential
change in the space-time interval ( ds ) if we change all the
coordinates by a very tiny little bit. What is nice about this is that
although coordinates are a tricky thing in general relativity and can
change from one observer to another, the space-time interval is an
invariant quantity. That is, different observers will measure the same
space-time interval between events even though they may measure
different times and distances.
GEN RIPPER: So this space-time interval is just a kind of space-time
distance that different observers will agree on?
DR. DRE: Right-o. And this invariance allows us to compare different
reference frames. Eventually, we will use this invariance to get the
frequencies observed by an observer on the surface of the earth and one
traveling along with a satellite in orbit. Since we will only be
considering observers at fixed radius and fixed theta = 90 degrees (ie
at the equator), we can simplify things a bit. Since we will have a
fixed radius and theta value we have that:
$$ dr = 0 $$
$$ d\theta = 0 $$
and
$$\sin\theta = 1 $$
Plugging these simplifications into our line element gives:
$$ ds^2 = -\left( 1 - \frac{R_s}{r} \right)c^2 dt^2 + r^2
d\phi^2 $$
GEN RIPPER: Neato Toledo!
DR DRE: Right, so now we divide out the -c^2 dt^2 term on the right
hand side. So we have:
$$ ds^2 = -c^2 dt^2 \left[ \left( 1 - \frac{R_s}{r} \right) -
\frac{r^2}{c^2} \frac{d\phi^2}{dt^2} \right] $$
But this is just $$ ds^2 = -c^2 dt^2 \left[ \left( 1 -
\frac{R_s}{r} \right) - \frac{r^2}{c^2} {\left(\frac{d\phi}{dt}
\right)}^2 \right] $$
But what does that d phi / dt term look like?
GEN RIPPER: Sure looks like an angular velocity to me. But don't we need
to be careful with these rates?
DR. DRE: Yep, that is an angular velocity term. We need to be a little
careful with these rates. Essentially, in the coordinate system we have
chosen the time is something like the time measured at r = infinity and
thus the rate would also be measured from r = infinity. Plugging in
omega as our angular velocity, we now have:
$$ ds^2 = -c^2 dt^2 \left[ \left( 1 - \frac{R_s}{r} \right)
-\left( \frac{r {\omega}}{c} \right)^2 \right] $$
But we want to figure out the times on the GPS satellites, so we'll need
some measure of how time ticks by as measured by the orbiting observer.
In the rest frame of the observer, we have that
$$ ds^2 = -c^2 {d\tau}^2 $$
where the tau is the "proper time" of the observer. It tells us the time
that the observer measures on his clocks. To find the frequency (in
other words, how quickly the observer clock ticks by a second) we just
have
$$ f = \frac{1}{d\tau} $$
And now we have enough background to start talking about GPS!
GEN RIPPER: Hooray! Should I go get my horse...?
DR. DRE: I don't think that's necessary...? Anyway, let's model our GPS
system as a satellite in a 26,000 km orbit [1]. Meanwhile our earth
reference frame will be an observer standing on the surface of the
earth. So let's write out our line element for each reference frame.
First the satellite frame:
*As Dr. Dre works, the beat steadily gets louder.*
$$ ds^2 = -c^2 {dt}^2 \left[ \left( 1 - \frac{R_s}{R_{sat}}
\right) -{\left( \frac{\omega_{sat} R_{sat}}{c} \right)}^2
\right] $$
So the frequency at which a satellite clock ticks is
$$ f_{sat} = \frac{1}{dt} \left[ \left( 1 - \frac{R_s}{R_{sat}}
\right) -{\left(\frac{\omega_{sat} R_{sat}}{c} \right)}^2
\right]}^{-1/2} $$ and likewise the earth frame:
$$ ds^2 = -c^2 {dt}^2 \left[ \left( 1 - \frac{R_s}{R_{earth}}
\right) -{\left(\frac{\omega_{earth} R_{earth}}{c} \right)}^2
\right] $$
So the frequency at which an earth clock ticks is
$$ f_{earth} = \frac{1}{dt} \left[ \left( 1 -
\frac{R_s}{R_{earth}} \right) -{\left( \frac{\omega_{earth}
R_{earth}}{c} \right)}^2 \right]}^{-1/2} $$
Taking the ratio of these frequencies tells us how quickly the satellite
clocks tick relative to the earth clocks. We get:
$$ \frac{f_{sat}}{f_{earth}} = {\left[ \frac{\left( 1 -
\frac{R_s}{R_{earth}} \right) -{\left( \frac{\omega_{earth}
R_{earth}}{c} \right)}^2 }{\left( 1 - \frac{R_s}{R_{sat}}
\right) -{\left( \frac{\omega_{sat} R_{sat}}{c} \right)}^2 }
\right]}^{1/2} $$
And we're done. So what do we get? Let's plug in some numbers:
$$ r_{sat} = 26 \times 10^6 m $$
$$ R_{earth} = 6.3 \times 10^6 m$$
$$\omega_{earth} = 7.3 \times 10^{-5} rad/s $$
$$\omega_{sat}=\sqrt{\frac{GM}{{r_{sat}}^3}}=15 \times 10^{-5}
rad/s $$
$$ c = 3 \times 10^8 m/s $$
We can also find the Schwarzschild radius of the Earth to be
$$ R_s = 8.9 mm $$
Now you still have that fancy calculator, right General? Can you plug
all this stuff in there and tell me what you get?
*General Ripper works diligently on the calculator for a few minutes,
then shows the calculator to Dr. Dre.*
**
DR. DRE: "01134"..? No that can't be correct. Did you plug in the values
I ... ?
*General, with a wry smile, turns the calculator upside down and shows
Dr. Dre.*
**
DR. DRE: Ah, well "hello" to you to sir. GEN. RIPPER: And I've got
another! Now where's that eight key...? DR. DRE: I guess I'll just do
the math in my head...
*The background beat, which had just reached a crescendo immediately
drops out as Dre thinks*. *Then comes right back in as he begins to
speak again...*
**
Alright, I got that
$$\frac{f_{sat}}{f_{earth}} = 1 + 4.4 \times 10^{-10} $$
From this we see that the satellite clock ticks faster (i.e. at a higher
frequency) than does the earth clock. The difference is very very small.
For every second that ticks by on earth, we see that the difference in
the earth and satellite clocks increases by 4.4 * 10^{-10} seconds.
GEN RIPPER: But we are talking about half a billionth of a second!
There's no way that can do much harm.
DR. DRE: Well remember, that's per second. So over the course of a day
(86,400 s), the satellite has picked up 38 microseconds. But that
corresponds to
$$ d = c \times t = ( 3 \times 10^8 m/s ) \times ( 38 \times
10^{-6} s ) = 11 km $$
So without correcting for general relativity, GPS systems would be off
by 11 km per day!
GEN RIPPER: I am impressed! Here's millions of dollars in funding!
Hooray!
DR. DRE: Hooray!
*Dr. Dre and General Ripper jump up and give each other a mid-air high
five. We freeze-frame this scene and*"Don't You Forget About Me" *plays
as the credits roll.*
**
*THE END (?)* ** ** [1] Thanks to Tom from [Swans on
Tea](http://blogs.scienceforums.net/swansont/) (one of my favorite
physics blogs) for fixing a mistake for me. I had initially done the
calculation assuming the satellite was in a geosynchronous orbit (about
42,000 km) and got a time delay of 48 microseconds. As it turns out, the
GPS satellites are really at an orbit of about 26,000 km, which gives a
time delay of 38 microseconds. I have made the appropriate changes and
the calculations now reflect this more accurate value.
**
