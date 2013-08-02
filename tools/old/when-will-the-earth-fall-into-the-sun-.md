Title: When will the Earth fall into the Sun? 
Date: 2012-11-29 22:58:00
Tags: 
Category: old
Slug: when-will-the-earth-fall-into-the-sun-
Author: Brian



<table cellpadding="0" cellspacing="0" class="tr-caption-container" style="float: right; text-align: right;"><tbody><tr><td style="text-align: center;"><a href="http://4.bp.blogspot.com/-_71xzP94MDc/ULgp7n5LP3I/AAAAAAAAACM/WU5UgsRyUYg/s1600/RetardedPic.png" imageanchor="1" style="clear: right; margin-bottom: 1em; margin-left: auto; margin-right: auto;"><img border="0" height="143" src="http://4.bp.blogspot.com/-_71xzP94MDc/ULgp7n5LP3I/AAAAAAAAACM/WU5UgsRyUYg/s200/RetardedPic.png" width="200" /></a></td></tr><tr><td class="tr-caption" style="text-align: center; width: 200px;">The time I spent making this poster could have been spent doing research. </td></tr></tbody></table>Since December 2012 is coming up, I thought I'd help the Mayans out with a look at a possible end of the world scenario. (I know, it's not Earth Day yet, but we at the Virtuosi can only go so long without fantasizing about wanton destruction.) As the Earth zips around the Sun, it moves through the <a href="http://en.wikipedia.org/wiki/Heliosphere">heliosphere</a>, which is a collection of charged particles emitted by the Sun. Like any other fluid, this will exert drag on the Earth, slowly causing it to spiral into the Sun. Eventually, it will burn in a blaze of glory, in a bad-action-movie combination of Sunshine meets Armageddon.
<a name='more'></a>
Before I get started, let me preface this by saying that I have no idea what the hell I'm talking about. But, in the spirit of being an arrogant physicist, I'm going to go ahead and make some back-of-the-envelope calculations, and expect that this post will be accurate to within a few orders of magnitude.

Well, how long will the Earth rotate around the Sun before drag from the heliosphere stops it? This seems like a problem for fluid dynamics. How do we calculate what the drag is on the Earth? Rather than solve the fluid dynamics equations, let's make some arguments based on dimensional analysis.

What can the drag of the Earth depend on? It certainly depends on the speed of the Earth v -- if an object isn't moving, there can't be any drag. We also expect that a wider object feels more drag, so the drag force should depend on the radius of the Earth R. Finally, the density of the heliosphere might have something to do with it. If we fudge around with these, we see that there is only 1 combination that gives units of force:
 $$
 F_{drag} \sim \rho v^2 R^2
 $$

 Now that we have the force, the energy dissipated from the Earth to the heliosphere after moving a distance <i>d</i> is <i>E_lost = F*d</i>. If the Earth moves with speed v for time t, then we can write <i>E_lost = F*v*t</i>. So we can get an idea of the time scale over which the Earth starts to fall into the Sun by taking <i>E_lost = E_Earth ~ 1/2 M_Earth v^2</i>. Rearranging and dropping factors of 1/2 gives
 $$
 T_\textrm{Earth burns} \sim M_{Earth} v^2 / (F_{drag}\times v) \ \qquad  \sim M_{Earth} / (\rho R^2 v)
$$
Using the velocity of the Earth as <i>2*pi *</i> 1 Astronomical unit/year, Googlin' for some numbers, and taking the <a href="http://web.mit.edu/space/www/helio.review/axford.suess.html">density of the heliosphere</a> to be 10^-23 g/cc  we get... $$ T \approx 10^{19} \textrm{ years} $$  Looks like this won't be the cause of the Mayan apocalypse. (By comparison, the <a href="http://en.wikipedia.org/wiki/Sun#Life_cycle">Sun will burn out </a>after only ~10^9 years.) 
