Title: Something Bugging Me
Date: 2010-07-20 23:24:00
Tags: collision, bug, summer
Category: old
Slug: something-bugging-me
Author: Jesse

<div class="separator" style="clear: both; text-align: center;"><a href="http://4.bp.blogspot.com/_SYZpxZOlcb0/TEZsSZmSnUI/AAAAAAAAAB8/6ArQgAym3Fk/s1600/3063594778_019489ef21.jpg" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="136" src="http://4.bp.blogspot.com/_SYZpxZOlcb0/TEZsSZmSnUI/AAAAAAAAAB8/6ArQgAym3Fk/s200/3063594778_019489ef21.jpg" width="200" /></a></div>Apparently July is a quiet month here at the Virtuosi.  We're busy with research, travel, vacation, etc.  I, myself, have been busy with only a few of those things, though I've also been studying for my qualifying exam, which is coming up in less than a month.  However, that's not the question before us today.  Today I'd like to think about the density of bugs in the air.  I was walking outside this past weekend, there was a fierce wind blowing, and twice in five minutes a bug hit my ear.  That seemed like a lot.  But for 1 hour of previous walking no bugs hit my ear.  How many bugs would there have to be per cubic meter of air to achieve that rate?

<a name='more'></a>We'll restrict ourselves to small bugs, like nats, nothing really mobile like house flies.  We have an observed bug impact rate of 2 bug/hour.  I'd estimate that my ear is ~1"x2", an area of 2 in^2.  Let's convert to metric, that's about 13 cm^2.  Next I need to know how fast the wind was blowing.  I'd guess about 15 miles per hour, it was a good stiff wind off the lake.  From here, we just need to write down an equation for the bug collision rate.  The simplest theory I can imagine would go something like this:

(Bug density)(ear cross section)(wind speed)=(collision rate)

In the above I've assumed that the bugs are moving with the wind (hence my initial assumption that the bugs are small, and thus will more or less move with the wind).  If you check the above, it has the right units, bugs per time on both sides of the equation.  Now we just need to solve for the bug density, we'll call that <i>B</i>, in terms of the rest of our knowns: ear cross section area <i>A</i>, wind speed <i>v</i>, and collision rate <i>R</i>.  This gives

$$B=\frac{R}{Av}=\frac{2 bug/hour}{(13cm^2)(15mph)}$$

We've got a big of a units problem with our wind speed in miles per hour and our ear area in cm^2, so I'll convert from mph to cm/hour, and come out with a bug density of

$$B=\frac{2 bug/hour}{(13cm^2)(2.4 Mcm/hour)}=6.4*10^{-8}bugs/cm^3$$

That seems like an absurdly small number.  Let's convert from cm^3 to m^3.  That gives us .064 bugs/m^3.  This still seems rather low to me.  Put another way, we'd need ~16 m^3 to find 1 bug (this is only ~160 bugs/olympic swimming pool!).  What might be amiss with the estimate?  Well, I'm fairly happy with the ear area.  I could be misremembering the length of my walk. More importantly, I'd wager that not all of my walk was perpendicular to the direction the wind was blowing.  If I were at an angle to the wind I'd have a commensurately smaller ear surface area presented to the wind.  Of course, this will at best probably gain us around a factor of two.  I'm not very familiar with wind speeds, so maybe we could pick up another factor of two there.

Still, I imagine that the main problem with my calculation is that I assumed that all of the bugs were stationary and would be blown against my ear.  Even little bugs are very mobile (as you well know if you've ever tried to swat them), and were probably actively trying to avoid my ear for the most part.  Only the really weak, senseless (literally), or stupid bugs got blown against my ear, and apparently those aren't that common.  How common are they?  You tell me.  Make an estimate for the bug density of air, compare it to my senseless bug density, and find the percent of bugs that fit my description!  Or not, if you only come here to watch the rest of us toil over our calculations.
