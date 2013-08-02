Title: Batman, Helicopters, and Center of Mass
Date: 2012-06-26 11:10:00
Tags: Center of Mass, Batman
Category: old
Slug: batman-helicopters-and-center-of-mass
Author: DTC


<div dir="ltr" style="text-align: left;" trbidi="on"><div class="separator" style="clear: both; text-align: center;"><a href="http://cdn.medialib.computerandvideogames.com/screens/screenshot_263713.jpg" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="180" src="http://cdn.medialib.computerandvideogames.com/screens/screenshot_263713.jpg" width="320" /></a></div>

A couple weeks ago, I came home after a long day at work looking for a break.  I thought to myself, “What’s more fun than physics? Batman*.”  I sat down to play the <a href="http://en.wikipedia.org/wiki/Arkham_City" target="_blank">latest Batman videogame</a>, in which Batman’s current objective was to use his grappling hook to jump onto an enemy helicopter to steal an electronic MacGuffin.  As awesome as this was, it occurred to me that something was very wrong about the way the helicopter moved while Batman zipped through the air.

<a href="http://youtu.be/81qN-PHucqM?t=3m12s">See if you can spot it too</a>.  (Watch for about 5 seconds after the video starts.  Ignore the commentary.  Note: The grunting noises are the sounds that Batman makes if you shoot him with bullets.)

What occurred to me was this:  If the helicopter’s rotors provided enough lift to balance the force of gravity, wouldn’t Batman’s sudden additional weight cause the helicopter to fall out of the sky?  Also, to get lifted up into the air, the helicopter must be pulling up on Batman: shouldn’t Batman also be pulling down on the helicopter?  By how much should we expect to see the helicopter’s altitude change?
<a name='more'></a>
To address the first question, let's go to Newton's second law:
$$ \sum \vec{F} = m\vec{a} $$
Let’s assume that the helicopter is hovering stationary, minding its own business, when Batman jumps onto it.  <span style="background-color: white;">Let's also assume the helicopter pilots are totally oblivious to Batman and make no flight corrections after Batman jumps onto it.  </span><span style="background-color: white;">In order to hover, the lift from the helicopter's rotors exactly matched the pull of gravity. </span>

$$ \sum \vec{F} =  \vec{F}_{rotors} - \vec{F}_{gravity} =  0 $$

Batman's sudden additional weight would cause the helicopter to start falling, as the forces would no longer balance:


$$ \sum \vec{F} =  \vec{F}_{rotors} - \vec{F}_{gravity} - \vec{F}_{Batman} &lt;  0 $$


<div><span style="background-color: white;">So the helicopter does accelerate (and move) when Batman jumps onto it.  How much does it move?  </span><span style="background-color: white;">Let’s assume there are no crazy winds or other external forces acting on the helicopter or Batman while Batman grapples onto the helicopter.  “No external forces” means that momentum of helicopter + Batman does not change during Batman's flight.</span>

Let's make things a little simpler and assume that neither Batman nor the helicopter had any vertical momentum before Batman used his grappling hook.  (I can choose to approach this problem from a reference frame where the center of mass is stationary.  Choosing a frame where the center of mass moves won't change the results, it will just make the calculation more complicated.)  Because the momentum of helicopter + Batman does not change, then the center of mass does not move while Batman zips through the air:

$$ \frac{d}{dt} y_{COM} = \frac{d}{dt} \frac{m_{Bat} y_{Bat} + m_{Copter} y_{Copter}}{m_{Bat} + m_{Copter}} = \frac{p}{m_{Bat} + m_{Copter}} = 0 $$</div><div>
The center of mass must remain stationary, so we can find how much the helicopter's height changes by if Batman starts on the ground (y = 0) and both end up at the same height with Batman hanging from the helicopter:

$$ y_{COM} = \frac{m_{Copter} y_{Copter} + m_{Bat} (0)}{m_{Bat} + m_{Copter}} = \frac{m_{Copter} y_{final} + m_{Bat} y_{final}}{m_{Bat} + m_{Copter}} $$
$$ \Delta y = y_{Copter} - y_{final} = \frac{m_{Bat}}{m_{Bat} + m_{Copter}} y_{Copter}$$</div><div>
Now, some numbers: The police helicopters in the game are pretty small, probably about <a href="http://en.wikipedia.org/wiki/Bell_206">1500 kg</a>.  Batman is a big guy who works out and probably weighs around 100 kg (220 lb).  Plus, he’s wearing body armor (hence surviving when bullets hit him) and a utility belt and all of those other Bat-gadgets, which probably adds about 30 kg (~30 lb for the gadgets, <a href="http://www.nationaldefensemagazine.org/archive/2011/February/Pages/ManufacturersAnswerMilitary%E2%80%99sCalltoReduceBodyArmorWeight.aspx">~30 lb for the armor</a>).  If Batman has to grapple onto a helicopter 30 meters above him, then the helicopter should drop out of the air by about 2.4 m.  This is greater than the height of Batman himself, and would be noticeable if the helicopter physics in the game were perfect.

Of course, if the helicopters appearing in the game were the giant army helicopters (they do carry rockets, after all), their mass would be much larger (~5000-10000 kg) so the effect of Batman’s additional weight would be much smaller.

None of these considerations detracted from the fun I had playing the game, but it did seem odd that the helicopters appeared to be nailed to the sky instead of moving freely through the air.  I’ll be writing the game developers a strongly-worded letter directly.


* The DC superhero, not the <a href="http://en.wikipedia.org/wiki/Batman,_Turkey">city</a> or the <a href="http://www.newcritters.com/2007/01/23/the-batman-fish-otocinclus-batmani/">fish</a>.

</div></div>
