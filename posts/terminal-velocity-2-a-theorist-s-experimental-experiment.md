<--
.. title: Terminal Velocity 2: A Theorist's Experimental Experiment
.. date: 2010-08-12 17:23:00
.. tags: data, bike, measurement, fun
.. category: old
.. slug: terminal-velocity-2-a-theorist-s-experimental-experiment
.. author: Yariv
.. has_math: true
-->


Yesterday we rode down Ithaca's hills in an attempt to estimate the
terminal velocity of a bike rider braving the city's potholes. But
estimations are easy, and we relied on a number of factors - the drag
coefficient and area of the bicyclist, in particular - to get them. To
see how well we did, it's time to move on to the experimental portion
this exercise. Our tools? My bike (figure 1), and my beloved
accelerometer (figure 2), with Google's [My
Tracks](http://mytracks.appspot.com/) app installed.

[![image](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRzmU_-t0I/AAAAAAAACFA/6JFhG9Z9YiA/s200/bike.jpg)](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRzmU_-t0I/AAAAAAAACFA/6JFhG9Z9YiA/s1600/bike.jpg)Figure
1: Our vehicle

[![image](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRn_JN3A6I/AAAAAAAACEQ/b02aLvN9_ys/s200/Droid+2.png)](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRn_JN3A6I/AAAAAAAACEQ/b02aLvN9_ys/s1600/Droid+2.png)

Figure 2: Our instrumentation

I took data twelve times while driving down two paths ([University
avenue](http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=University+and+Cornell,+Ithaca+NY&sll=42.44395,-76.485014&sspn=0.016721,0.038581&ie=UTF8&hq=&hnear=University+Ave+%26+Cornell+Ave,+Ithaca+College,+Tompkins,+New+York+14850&ll=42.447243,-76.493082&spn=0.01672,0.038581&t=p&z=15)
and [State
street](http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=State+and+Stewart,+Ithaca,+NY&sll=42.447243,-76.493082&sspn=0.01672,0.038581&ie=UTF8&hq=&hnear=E+State+St+%26+Stewart+Ave,+Ithaca+College,+Tompkins,+New+York+14850&ll=42.439262,-76.489692&spn=0.016722,0.038581&t=p&z=15)),
measuring both the speed and elevation as a function of time. I came up
with a lot of noisy data, some of it useful and a lot of it not. A
typical plot out of the software looks something like (figure 3); out of
those I identified moments of what seemed to be free acceleration, where
I was not applying the brakes. I then calculated the slope and the
acceleration at each point by subtracting subsequent measurements; this
resulted in much noisier data, as seen on (figure 4).

[![image](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRoiavSb4I/AAAAAAAACEY/3Yee3_k-TiY/s400/University7.png)](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRoiavSb4I/AAAAAAAACEY/3Yee3_k-TiY/s1600/University7.png)Figure
3: Typical data riding downhill
[![image](http://1.bp.blogspot.com/_JIGLe2C6VxI/TGRo0pVcbSI/AAAAAAAACEg/qdGFWsUS4X8/s400/University7DiffFocus.png)](http://1.bp.blogspot.com/_JIGLe2C6VxI/TGRo0pVcbSI/AAAAAAAACEg/qdGFWsUS4X8/s1600/University7DiffFocus.png)Figure
4: Derivatives

The next question was what to fit these graphs to. I can't compare
directly to the formula I had for terminal velocity, since I don't
believe I achieve it at any point and we never see the velocity graph
plateau. What we do have is the formula for the acceleration, which
depends on both the angle and the velocity: $$ a = g\sin\theta -
\frac{1}{2}\frac{\rho A C_d}{m} v^2. $$ It's a little hard to plot
three-dimensional surfaces like this, but I can try to plot the
acceleration as a function of the velocity squared. Assuming that the
slope of each of my routes is constant and that they are both different,
this should give me two straight lines offset by a constant. Seen in
(figure 5), this yields less than optimal result. A first correction
would be to account for the differing slope at different measurement
points. Once we do that the data looks a little more linear, and we can
fit a line through it, as seen in (figure 6).

[![image](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRpFDSXYbI/AAAAAAAACEo/pce7SNz6s_U/s400/avv.png)](http://2.bp.blogspot.com/_JIGLe2C6VxI/TGRpFDSXYbI/AAAAAAAACEo/pce7SNz6s_U/s1600/avv.png)Figure
5: Acceleration vs. velocity

[![image](http://1.bp.blogspot.com/_JIGLe2C6VxI/TGRpIHtielI/AAAAAAAACEw/-MuDiahJbxg/s400/avvfixed.png)](http://1.bp.blogspot.com/_JIGLe2C6VxI/TGRpIHtielI/AAAAAAAACEw/-MuDiahJbxg/s1600/avvfixed.png)Figure
6: Adjusted for slope and fitted

The fits are given by: $$ a = (1.022 \rm{m}) - (0.00427 \rm{1/m})
v^2\;\; \rm{(University)} $$ $$ a = (1.465 \rm{m}) - (0.00572
\rm{1/m}) v^2\;\; \rm{(State)} $$ and we can quickly extract the
terminal velocity out of the coefficients to get a factor of 47.9 m/s
for the first line and 41.4 m/s for the second. These both fall within
20% of our initial estimate, which is quite satisfying considering how
bad the data looks. A few final thoughts:

-   Why is the data so noisy? I can think of a lot of reasons. My Droid
    phone is not quite a scientific measuring device to begin with, and
    we did some numerical derivation of the initial data we got from it.
    On top of that, the way I sit on the bike, the weight of the bag I
    carry with me and other factors like the wind changed from ride to
    ride.
-   I tried to avoid biasing the analysis and I was quite relieved when
    the final numbers came out so close to my original estimate. I did
    play around a little with a different presentation that didn't look
    linear at all, but other than that I think what I did was pretty
    straightforward.
-   The one thing that I don't like about the final results is the
    constant addition to both acceleration fits, or put another way, the
    fact that after subtracting the gravitational pull from the
    acceleration I still get positive numbers, while the drag force
    should work to reduce it. I suspect this implies that my
    cancellation of the sinθ term was less than perfect.
-   Can you figure out what the trajectory the bike as a function of
    time looks like? There's a (non-trivial) analytic expression.

