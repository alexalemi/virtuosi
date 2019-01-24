<--
.. title: End of the Earth VI: Nanobot destruction
.. date: 2011-04-22 13:11:00
.. tags: fun, nanobots, end of the earth, earth day
.. category: old
.. slug: end-of-the-earth-vi-nanobot-destruction
.. author: Alemi
.. has_math: true
-->


[![image](http://1.bp.blogspot.com/-hGkMD-tB1RY/TbGfhRvcA6I/AAAAAAAAAQ4/eCaG-z1Zarc/s320/612px-C60a.png)](http://1.bp.blogspot.com/-hGkMD-tB1RY/TbGfhRvcA6I/AAAAAAAAAQ4/eCaG-z1Zarc/s1600/612px-C60a.png)

Let's destroy the earth with technology. A while ago, I read the novel
*Postsingular* by Rudy Rucker, and in the first chapter the Earth gets
destroyed, and then undestroyed, and then the novel unfolds and the
Earth's likelihood is threatened again, and it looks like the Earth will
be destroyed, but it isn't. How does all of this craziness happen you
might ask: nanobots! The story revolves around little self-replicating
robots. The story explores what it would be like to live in a world
where every surface on Earth was coated in little computers, all of
which were networked together. It's certainly a neat idea, but whenever
you have self-replicating things, you need to worry a bit about what
might happen if they get out of control. So, let's assume we, evil
scientists that we are, have managed to create a little self-replicating
nanobot. This little guy can scurry around, running off something
ubiquitous, probably some combination of solar, and some kind of
infrared photovoltaics. This little guy, call him Bob, his only mission
in life is to create a friend. He scurries around collecting the various
ingredients necessary, and using his little robot arms, he slices and
dices up the pieces and welds them together to create another copy of
himself, Rob. Not satisfied with his work; Bob found Rob quite the bore,
and honestly Rob didn't too much like Bob either, both of them part ways
and try to fashion a new friend. How long until Bob and Rob and their
cohorts manage to chew through all of the material on Earth? What we
have here is the setup to a problem in [Exponential
Growth](http://en.wikipedia.org/wiki/Exponential_growth).

### Exponential Growth

Let's simplify things a bit and assume that the nanobots always take a
fixed amount to time to make a new copy of themselves, call that time T.
We'll start with one guy, so we know that at t =0, we have 1 bot $$ N(t
=0 ) = 1 $$ And we know that after T seconds we should have 2 $$ N(T) =
2 $$ and after 2T seconds, we've managed to double twice and get 4 $$
N(2T) = 4 $$ after 3T seconds we'll double again to 8, etc. In fact,
after nT seconds, so m repetitions we should have doubled m times $$
N(nT) = 2^n $$ So if we want to describe all times, we need only ask
how many doublings can fit into t seconds $$ t = n T $$ which gives us
$$ N(t) = 2^{t/T} $$ At this point you might object, as this formula
doesn't always give an integer, so we could ask things like how many
bots are there after 0.5T seconds? We know the true answer is still 1,
Bob hasn't finished Rob yet, but our formula tells us the answer is
1.414... What we've done is made a continuous approximation to a
discrete function. Certainly, we've paid a price, in that our new
formula doesn't get answers right in fractions of T, but its a small
price to pay for the mathematical simplicity afforded by the nice
continuous function, and as long as we don't really care about time
scales smaller than T in the long run, we haven't done any real harm.
These kinds of approximations show up all over the place in physics, and
going both ways too. Sometimes it is advantageous to treat some discrete
quantity as continuous, and sometimes it might be beneficial to treat
some continuous quantity as discrete. These kinds of approximations are
more than adequate, provided you don't really take the answers they give
you in the cases where your approximation starts to break too seriously.
In this case, as long as we don't try to seriously predict the number of
nanobots to an exact count in time scales less than a fraction of their
doubling time, we will have a nice prediction of the number of bots
running around.

### Earth Destruction

As promised, we wanted to calculate the time it would take the nanobots
to devour the earth. For this we need a little bit more to our model.
How will the nanobots eat the earth, I reckon it will be through using
up its mass. Assuming the bots are made out of elements that are rich
enough, something like iron, they ought to have a field day on Earth,
seeing as it's composed of about 5% iron on the surface, and with an
interior that is probably about 32% iron overall
[[ref]](http://en.wikipedia.org/wiki/Abundance_of_the_chemical_elements#Abundance_of_elements_in_the_Earth).
So, we need to estimate the mass of a single nanobot. Let's say the
nanobot is roughly a 1 micron sized cube, made out of iron. This gives
us a nanobot mass of $$ m = (\text{ density of iron }) * (\text{ 1
micron} )^3 = \rho_{\text{Fe}} L^3 \sim 8 \text{ picograms} $$
From here we can estimate the time it would take to chew through the
earth, as the time for the nanobots to be as massive as the earth. $$
\frac{M_{\oplus}}{\rho_{\text{Fe}} L^3 } = N(t) = 2^{t/T} $$
Solving for t we obtain $$ t = T \log_2 \frac{ M_{\oplus}}{
\rho_{\text{Fe}} L^3 } $$

### Solution

Let's say it takes Bob one month to make Rob, which I don't think is a
completely unrealistic time for nanobot replication, assuming Bob and
Rob and all of their cohorts are 1 micron in size, I calculate that in
10 years time they would chew through the Earth. The power of
exponential growth! Even with a 1 month gestation, if left unabashed,
the self-replicating robots would eat the entire earth in 10 years time.
They could eat through Mars in about 2. In fact in *Postsingular* this
is what the humans planned. They wanted a Dyson sphere, so they sent
some self-replicating robots to Mars, let them chew through it a couple
years, and they had 10^37 little robots to do their bidding. That is of
course until the nants set their sites on Earth as their next target...
In order to let you play around with the doubling time and bot size,
I've created a Wolfram Alpha widget that solves the above equation, feel
free to play around with the parameters and see how long Earth would
survive.

The widget should be right above this text. If it isn't working for some
reason, here's a
[link](http://developer.wolframalpha.com/widgets/gallery/view.jsp?id=6a645314f9be6be7b902d4cc1f776d00)
