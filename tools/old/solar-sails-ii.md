Title: Solar Sails II
Date: 2010-05-17 01:15:00
Tags: solar sails, Nic shout outs, scott bakula
Category: old
Slug: solar-sails-ii
Author: Corky


<div style="text-align: left;">[NOTE: In my hurry to make up for weeks of non-posts, I managed to almost immediately knock Nic's <a href="http://thevirtuosi.blogspot.com/2010/05/why-black-holes-from-large-hadron.html">first post</a> from the top of the page.   It's got the LHC, black holes, and about 3 full cups of metric awesome, so make sure you check it out (after reading this one, of course).]  </div><div style="text-align: left;">
</div><div style="text-align: left;">Last time we did some calculations on how fast and far our solar sails can go, but those calculations were just for the sail itself.   If you are going to do any science with it, you're going to need a payload.  Let's take it a step further and make it an actual spaceship (with people and everything!)<a name='more'></a>.</div><a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://4.bp.blogspot.com/_fa6AZDCsHnY/S_DXvcSsDXI/AAAAAAAAACg/jK_N-B4mOME/s1600/ssradius.png"></a><div>
</div><div>Comparing it with a typical people-carrying space hotel (the International Space Station), let's give our payload a mass of 300,000 kg.   Remembering from the last post that a sigma of less that about 10^-4 g/cm^2 gave fairly nice results, we can make an effective sigma of our payload carrying sail as</div><div>
</div><div>$$ \sigma_{eff} = \frac{m_{total}}{Area} = \frac{m_s + m_p}{Area}, $$</div><div>
</div><div>where m_s is the mass of the sail and m_p is the mass of our payload (the ship).  Assuming the sail has some surface density of sigma and the sail is circular with some radius r, we have</div><div>
</div><div>$$ \sigma_{eff} = \frac{\pi r^2 {\sigma}_s + m_p}{\pi r^2} = {\sigma}_s + \frac{m_p}{\pi r^2} . $$</div><div>
</div><div>Now we can find the radius of our sail such that </div><div>
</div><div>$$ \sigma_{eff}  \le 10^{-4} \frac{g}{{cm}^2}. $$</div><div>
</div><div>Rearranging our equation above and solving for radius, we find that </div><div>
</div><div>$$ r \ge \left[\frac{m_p}{\pi \left( 10^{-4}\frac{g}{cm^2} - \sigma_s \right)} \right]^{1/2} cm. $$</div><div>
</div><div>Below is a plot of sail radius (in meters) against sail surface density (g/cm^2).</div><div>
</div><div><a href="http://4.bp.blogspot.com/_fa6AZDCsHnY/S_DXvcSsDXI/AAAAAAAAACg/jK_N-B4mOME/s1600/ssradius.png"><img src="http://4.bp.blogspot.com/_fa6AZDCsHnY/S_DXvcSsDXI/AAAAAAAAACg/jK_N-B4mOME/s400/ssradius.png" border="0" alt="" id="BLOGGER_PHOTO_ID_5472110757303553394" style="display: block; margin-top: 0px; margin-right: auto; margin-bottom: 10px; margin-left: auto; text-align: center; cursor: pointer; width: 400px; height: 179px; " /></a>
From this plot, we see that we will need our sail radius to be AT LEAST 10 km and the surface density of our sail must be less than 10^-4 g/cm^2.   Now that's a big sail, but it's not obscenely big (depending, of course, on your definitions of obscenity).   One could certainly imagine such a sail being built, but it would be an impressive engineering feat.  </div><div>
</div><div>So get to work engineers!  I've already made a whole plot in Mathematica, I can't do everything.</div>
