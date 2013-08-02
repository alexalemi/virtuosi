Title: How Long Will a Bootprint Last on the Moon?
Date: 2012-01-01 20:46:00
Tags: footprint, scott bakula, moon
Category: old
Slug: how-long-will-a-bootprint-last-on-the-moon-
Author: Corky


<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="float: left; margin-right: 1em; text-align: left;"><tbody><tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-gEyp9bylwcQ/Tv5v7PlugjI/AAAAAAAAARU/OnVdFTPRGkI/s1600/bootprint_buzz.jpg" imageanchor="1" style="clear: left; margin-bottom: 1em; margin-left: auto; margin-right: auto;"><img border="0" height="320" src="http://3.bp.blogspot.com/-gEyp9bylwcQ/Tv5v7PlugjI/AAAAAAAAARU/OnVdFTPRGkI/s320/bootprint_buzz.jpg" width="316" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Buzz Aldrin's bootprint (source: Wikipedia)</td></tr></tbody></table>A couple of months ago, I stumbled across a bunch of <a href="http://www.nasa.gov/mission_pages/apollo/revisited/index.html">pictures</a> of Apollo landing sites taken by one of the cameras onboard the Lunar Reconnaissance Orbiter.  The images have a resolution high enough that you can resolve features on the surface down to about a meter.  Looking at the Apollo 17 <a href="http://www.nasa.gov/images/content/584392main_M168000580LR_ap17_area.jpg">landing site</a>, you can see the trails of both astronauts and a moon buggy.  It's pretty cool.

It also got me thinking about how long the landing sites would be preserved. More specifically, I want to know how long Buzz Aldrin's right bootprint (shown, incidentally, to the left) will last on the Moon.  Since the Moon has no atmosphere, the wind and rain that would weather away a similar bootprint here on Earth are not present and it seems as though the print would last a really long time. But how long? Let's try to quantify it <a href="#footnote-yariv">[1]</a><a href="" id="back-yariv"></a>.

<a name='more'></a><span style="font-size: x-large;">Pick Your Poison</span>

Before we get going, we need to figure out what physical process would be most important in erasing a bootprint from the Moon. Although the Moon lacks the conventional "weathering" we experience on Earth (due to wind, rain, etc), it does experience something called "<a href="http://en.wikipedia.org/wiki/Space_weathering">space weathering</a>." Space weathering is the changing of the lunar surface due to cosmic rays, micrometeorite collisions, regular meteorite collisions, and the solar wind <a href="#footnote-wind">[2]</a><a href="" id="back-wind"></a>. Of these phenomena, the most apparent and well-studied would be the meteorites which have covered the Moon in craters. We adopt the meteorite impact as our primary means of wiping out a bootprint and restate our question as follows:

"How long would it take for a meteorite to hit the Moon such that the resulting crater wipes out Aldrin's right bootprint?"

<span style="font-size: x-large;">Background </span>

As it is currently stated, we can answer our question if we knew the rate of formation and size distribution of the craters on the Moon.  We could count up all the craters on the Moon (or a particular region of interest) and tabulate their sizes.  This would give us the size distribution.  It would also give us a headache and potentially drive us to lunacy <a href="#footnote-forced">[3]</a><a href="" id="back-forced"></a>.  Luckily, someone has beat us to it. 

<a href="http://adsabs.harvard.edu/abs/1966MNRAS.134..245C">Cross (1966)</a> used images from the Ranger 7 and 8 missions to count craters and determine the size distribution of craters in three regions of the Moon.  The data for the crater distribution in the Sea of Tranquility (where Apollo 11 landed) are given in the figure below.  Cross found that in the Sea of Tranquility, the number of craters with diameters greater than X meters (per million square kilometers) is given by:

$$ N(d&gt;X) = 10^{10}\left(\frac{X}{1~\mbox{m}}\right)^{-2}, $$

which holds for craters with diameters between 1 meter and 10 kilometers (see figure below). 
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody><tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-kHxcn_PTd5o/TwDg3XGAcqI/AAAAAAAAARg/jl-kb22JD-Y/s1600/fig2.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="400" src="http://3.bp.blogspot.com/-kHxcn_PTd5o/TwDg3XGAcqI/AAAAAAAAARg/jl-kb22JD-Y/s400/fig2.png" width="332" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Figure 2 from Cross (1966)</td></tr></tbody></table>
We can also estimate the rate at which craters are formed from this data.  If we assume that the craters formed at a constant rate over the age of the Moon (about 4 billion years), then we get about 2.5 craters with diameters above 1 meter formed in a million square kilometer area every year.  This is a "crater flux" for the Moon.  Written another way, the crater flux in the Sea of Tranquility is

$$F \approx 1~{\mbox{km}}^{-2} \frac{1}{4\times10^5~\mbox{yr}}, $$

so we get that roughly one crater with diameter greater than 1 meter is formed on a square kilometer of the Moon once every 400,000 years or so.

We now have enough information to do some simulations.

<span style="font-size: x-large;">Simulation</span>

I wrote up a code that simulates craters being formed on a 1 square kilometer patch of the Moon.  A crater is randomly placed in the 1 square kilometer region with a diameter pulled from the above distribution.  The bootprint is placed at the center of the grid and craters are formed until we get a "hit."  At that point, the time is recorded and the run stops. 

As a sanity check, I thought it would be fun to just let the simulation run without caring if the boot was hit or not.  By simulating the craters in this way for 4 billion years, I should get something that looks like the Moon at the present day. Here's a 200 m square from my simulation:
<div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/-DoFPG23CGwg/TwDqo-7GoQI/AAAAAAAAARs/QJW3RxeXFWI/s1600/mymoon_wticks.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="400" src="http://3.bp.blogspot.com/-DoFPG23CGwg/TwDqo-7GoQI/AAAAAAAAARs/QJW3RxeXFWI/s400/mymoon_wticks.png" width="400" /></a></div>and here's a picture of the same-sized region on the surface of the Moon:

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody><tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-qWW5dU-aEN8/TwDrDLPy93I/AAAAAAAAAR4/XGOywC79NFU/s1600/200metersquare.jpg" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="316" src="http://3.bp.blogspot.com/-qWW5dU-aEN8/TwDrDLPy93I/AAAAAAAAAR4/XGOywC79NFU/s320/200metersquare.jpg" width="320" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Cropped from <a href="http://www.nasa.gov/images/content/584398main_M168353795RE_25cm_AP12_area.jpg">this image</a> (Source: LRO)</td></tr></tbody></table>Just eyeballing it, things look pretty good. 

Now it's time for the actual simulation.  I ran the simulation 10,000 times and tabulated the amount of time needed before the bootprint was hit.  The figure below gives the <a href="http://en.wikipedia.org/wiki/Cumulative_distribution_function">CDF</a> for the hit times in the simulation.  That is, for each time T, we find the fraction of simulations in which the bootprint got hit in a time less than or equal to T. The dashed lines in the plot indicate the amount of time needed to pass for half of the simulations to have recorded a hit.  This time turns out to be about 24 billion years.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody><tr><td style="text-align: center;"><a href="http://3.bp.blogspot.com/-L2WLnCepUiw/TwDs7X_njkI/AAAAAAAAASE/jS_-I0Eem4k/s1600/hit_cdf.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" height="300" src="http://3.bp.blogspot.com/-L2WLnCepUiw/TwDs7X_njkI/AAAAAAAAASE/jS_-I0Eem4k/s400/hit_cdf.png" width="400" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">(Click for larger, actually readable version)</td></tr></tbody></table>
<span style="font-size: x-large;">Conclusions and Caveats</span>

Based on the simulations, the bootprint on the Moon would have about even odds of lasting at least 20 billion years <i>if</i> the primary means of destruction is through the formation of a crater from a meteorite.  However, there are a few caveats that should be addressed.  These deal with either the details of the simulation or the assumptions we have made. 

In the simulation, we just took at 1 km square patch of the moon and scaled back the "crater flux" accordingly.  However, this does not fully account for all possible craters that can form.  For example, our simulation would miss an event that hit 50 km away from the target, but had a diameter of 100 km.  Obviously this would hit the target, but we are only seeding craters in the 1 square km region.  This would mean that the actual lifetime of the bootprint would be less than our 24 billion year figure.  Re-running with a 10km by 10km square region, we find a lifetime of 18 billion years.  Thus, an increase in area by a factor of 100 only reduces the age by 25%.  Considering areas much larger than this makes the simulation prohibitively slow, but the order unity effect does not seem too significant.

Additionally, we have made a number of assumptions.  The big one is that we have assumed that the craters currently seen on the Moon were formed uniformly in time.  In fact, a large fraction of the craters may have been formed when the Moon was still very young (see <a href="http://en.wikipedia.org/wiki/Late_Heavy_Bombardment">Late Heavy Bombardment</a>).  If this were the case, we would have greatly overestimated the rate of crater formation and thus underestimated the time needed to hit the bootprint.

In spite of these caveats, let's take our value of 20 billion years to be accurate.  What else can we say?  Well, if we are right then we are wrong because the Moon may not last that long (and it's hard to have bootprints on the Moon without a Moon).  Current <a href="http://en.wikipedia.org/wiki/Sun#Life_cycle">estimates</a> have that the Sun will expand into a red giant and (potentially) destroy the Earth (and the Moon) in about 5 billion years. 

So a record of the Apollo astronauts' boot sizes could potentially last as long as the Moon <a href="#footnote-nixon">[4]</a><a href="" id="back-nixon"></a>.  Not bad.



<span style="font-size: large;">Footnotes and Such</span>

<div id="footnote-yariv">[1] Now with linked footnotes so Yariv doesn't have to scroll! <a href="#back-yariv">[back]</a></div>
<div id="footnote-wind">[2] There was a fairly recent press release about Coronal Mass Ejections from the Sun "sandblasting" the lunar surface.  For more info, check <a href="http://www.nasa.gov/topics/solarsystem/features/dream-cme.html">here</a>, and note the acronymic acrobatics needed to make them the "DREAM team."  But it's totally worth it. <a href="#back-wind">[back]</a></div>
<div id="footnote-forced">[3]  A horribly forced pun.  But it's totally worth it. <a href="#back-forced">[back]</a></div>
<div id="footnote-nixon">[4] Also, <a href="http://en.wikipedia.org/wiki/Lunar_plaque">Nixon</a> <a href="#back-nixon">[back]</a></div>
