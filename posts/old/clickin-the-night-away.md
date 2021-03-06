<--
.. title: Clickin' the Night Away
.. date: 2011-05-31 00:07:00
.. tags: ungodly large images, clicky, MEGAPIXELS (srsly)
.. category: old
.. slug: clickin-the-night-away
.. author: Corky
.. has_math: true
-->


Hey, everybody! Do you remember
[Clicky](http://thevirtuosi.blogspot.com/2011/04/collective-wanderings.html)
[1]? Well, we finally got around to analyzing data, so here goes. But
first, a brief summary.
Matt, Alemi and I came up with the idea for Clicky in the beginning of
April. Perhaps "idea" is a bit too generous... it was really just a
passing thought: "Hey wouldn't it be cool if we had an internet Ouija
board?" It was just a stupid lunch-time discussion that wouldn't have
gone anywhere had Alemi and Matt not taken it as some sort of challenge.
So after a few hours that night we had Clicky.
To say we had some goal with Clicky would be an overstatement. But, if
anything, we were kind of hoping to see some sort of Brownian motion. We
figured if we had lots of people pulling on the same dot, some kind of
Brownian walk would show up. This was grossly overestimating how many
people actually view this blog and it turned out that most of the time
Clicky was moved by one person at a time. Anyway, what we did end up
finding was more interesting than just a Brownian random walk...
Behold, in its full 133,000 point glory, Clicky!
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://1.bp.blogspot.com/-Ugbn0uGZnOU/TeRUMSPqMLI/AAAAAAAAAMk/KTgArv-WShU/s400/clicky_far_eq.png)](http://1.bp.blogspot.com/-Ugbn0uGZnOU/TeRUMSPqMLI/AAAAAAAAAMk/KTgArv-WShU/s1600/clicky_far_eq.png)
  Far View of Clicky. Click to super-size.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Well, I guess that isn't that impressive. But you can click on it for a
larger view or download the data and plot it yourself from
[here](http://www.mattbierbaum.com/clicky/clickydat.tar.bz2).
Alternatively, you can view a super-duper large version of the above
picture that will almost certainly make your browser sad (seriously,
it's big) at his website
[here](http://www.mattbierbaum.com/clicky/clickyfull.png).
We note that each step taken by Clicky is 1 unit long, and the above
image goes about 2500 on the y-axis and about 5000 in the x-axis. Though
we make no explicit comparison between our humble traveler and the great
men of lore, we do note that Clicky's long and tortuous path both begins
and ends in Ithaca [2].
Now the big picture is all well and good for some folks, but let's zoom
in a bit. We'll now zoom into a portion that is about 1000 by 1000 and
is located about in the middle of the Clicky map.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://2.bp.blogspot.com/-xGLDJGxVTDo/TeRYoMvFAiI/AAAAAAAAAMo/ejKB6Xd3D-I/s400/clicky_mid.png)](http://2.bp.blogspot.com/-xGLDJGxVTDo/TeRYoMvFAiI/AAAAAAAAAMo/ejKB6Xd3D-I/s1600/clicky_mid.png)
  Mid-level view of Clicky. Click for a more cromulent view.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So this view is pretty neat. Whereas the previous view appeared largely
random, we start to seem some structure here. We can see that some brave
soul has made a spiral that, at its biggest, goes for about a hundred
squares (remember, you could only see ten squares at a time!). We can
also see that most of the steps are small and tend to cluster, but every
now and again there is a large jump to uncharted territory.
Neat! Let's zoom in a bit more. Now we will zoom down to about a 100 by
100 square.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://1.bp.blogspot.com/-2nvaMlGiAM4/TeRaNsOYlpI/AAAAAAAAAMs/PMHfhKDroF4/s400/clicky_near.png)](http://1.bp.blogspot.com/-2nvaMlGiAM4/TeRaNsOYlpI/AAAAAAAAAMs/PMHfhKDroF4/s1600/clicky_near.png)
  Near view. Note the primitive form of communication.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

So this is neat. We see some very non-random structures. We see spelled
out the phrase "IM IN FIVE-TEN" (Phys 510 is the required graduate
physics lab here). This was actually not uncommon. There are lots of
little communications that go on throughout the Clicky map. Most are
just people marking their territory, but there are some fun ones. If you
find anything neat, let us know! (MILD WARNING: As this was open to The
Internet, we make no claims that everything written is appropriate, but
the worst thing I've seen so far is "butts lol." So I think you're
safe).
Now dedication to write something is fine, but how about some real
dedication. I found this little Italian gem here, although its means of
creation are suspect, to say the least...
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://3.bp.blogspot.com/-R6-E1Gf25S4/TeRdkV2Cu8I/AAAAAAAAAMw/rYY3YpIaYgc/s400/clicky_nonrandom.png)](http://3.bp.blogspot.com/-R6-E1Gf25S4/TeRdkV2Cu8I/AAAAAAAAAMw/rYY3YpIaYgc/s1600/clicky_nonrandom.png)
  It's a Mario!
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hot dog. So is there anything quantitative we can say about the path of
Clicky? Sure. Let's take a look at the distribution of step sizes. By
step sizes I mean the lengths of continuously straight paths. So if you
go right for 5 clicks in a row, the length will be five. Unfortunately,
this will not include the lengths of diagonal paths. Anyway, here's what
I get:
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://3.bp.blogspot.com/-fLEC65jbG3I/TeRfaN41EKI/AAAAAAAAAM0/KeHoRtCGtyc/s400/MLE_FIT.png)](http://3.bp.blogspot.com/-fLEC65jbG3I/TeRfaN41EKI/AAAAAAAAAM0/KeHoRtCGtyc/s1600/MLE_FIT.png)
  Power-law fit to Click step-size distribution
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The red line here is a maximum likelihood fit to a power law
distribution of the form:
$$ p(x) \propto x^{-\mu}. $$
(For an outstanding reference guide to fitting power law distributions
see this [preprint](http://arxiv.org/pdf/0706.1062v2).)
So it appears as though we have a power law distribution here (but see
the paper above!). Well what does that mean? Well it seems we have a
roughly random walk path where the step sizes are pulled from a power
law distribution. This type of random walk is called a Levy flight (a
nice tutorial
[here](http://classes.yale.edu/fractals/randfrac/Levy/Levy.html)) and
shows up (or at least appears to) in all kinds foraging patterns in
animals (for example,
[sharks](http://physicsworld.com/cws/article/news/42899)).
To test this, we can simulate a Levy flight on a grid like Clicky. Doing
this with the power law found in the above fit gives:
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![image](http://4.bp.blogspot.com/-e3vHjTxPqs0/TeRirLWJd8I/AAAAAAAAAM4/HZe7gFheYwI/s400/fake_clicky.png)](http://4.bp.blogspot.com/-e3vHjTxPqs0/TeRirLWJd8I/AAAAAAAAAM4/HZe7gFheYwI/s1600/fake_clicky.png)
  Impostor Clicky!
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Not exactly the same, but still looks pretty close!
So that's all for this installment of *Virtuosi Theatre*, but there's
still a whole lot to be analyzed with Clicky. With that much data,
you're bound to find *something* (whether it's there or not!). So if you
find something neat, let us know. (Remember the data can be downloaded
as a txt file
[here](http://www.mattbierbaum.com/clicky/clickydat.tar.bz2)).
---------------------------------------------
Superfluous Footnotes:
[1] Yes, I know you loved him as Mr. Dottington. I did too! But
apparently "the man" thought that was a "lame" name and made it all
"commercial" with the buzzname Clicky. So it goes.
[2] Although if Clicky is Odysseus, then I guess that makes you Homer.
D'oh! [3]
[3] All my knowledge of "culture" comes from The Simpsons.
