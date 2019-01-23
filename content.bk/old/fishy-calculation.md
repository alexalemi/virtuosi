Title: Fishy Calculation
Date: 2010-04-09 14:26:00
Tags: fermi, guestimation, fun, fermi problem, fish
Category: old
Slug: fishy-calculation
Author: Alemi


Aaron Santos over at [A Diary of
Numbers](http://diaryofnumbers.blogspot.com/), author of [How Many
Licks?](http://www.amazon.com/How-Many-Licks-Estimate-Anything/dp/0762435607),
has posted a [Fermi
Contest](http://diaryofnumbers.blogspot.com/2010/04/fermi-contest-3.html).
For the uninitiated, a [Fermi
Problem](http://en.wikipedia.org/wiki/Fermi_problem) is a seemingly
unanswerable problem, which you can actually estimate reasonable by
breaking the problem down into smaller parts. They're really fun, and I
intend to post more in the future. The question at hand is: *How far
would the oceans sink if we took all the fish out?* I'll answer in two
very different ways.

### Preliminaries

In both cases, I'll answer how much the ocean depth would decrease by
first calculating the total volume of fish in the ocean. Why is this
helpful? Because for a spherical shell, you can estimate its volume by
just taking its surface area and multiplying by the thickness, i.e. $$ V
\sim 4 \pi R^2 \Delta R $$ So, if I can estimate the total volume of
fish in the ocean, if I take all of those fish out, change in the height
of the ocean will just be this volume divided by the surface area of the
ocean, which I will take to be the surface area of the earth times 70%
or so. Now I just need to estimate the volume of all of the fish in the
oceans...

### Energy Budget

First I'll estimate the volume of fish in a rather general way. I'll try
to do it on energy grounds. I know how much solar energy hits the earth
per meter squared on average (340 W/m^2). I'm going to assume that fish
get their energy from plankton, and plankton get their energy from the
sun, both with about 10% efficiency. I'll also assume that life occupies
as much space as possible, probably about half of the ocean surface
counts as liveable. From this I get the total energy available to make
fish. How many fish does that allow? I'll assume that fish use about as
much energy per kilogram as humans do. I know that humans have to take
in about 2000 food Calories or 2,000,000 calories a day to survive. From
this I get the total weight of all of the fish in the ocean, and for
their volume I assume they're the density of water (fish are bouyant).
My calculation: $$ \underset{\text{ \tiny mean solar flux} }{\left(
340 \frac{\text{W}}{\text{m}^2} \right)} \cdot \underset{\text{
\tiny earth surface}}{4 \pi \left( 6 \times 10^6 \text{ m}
\right)^2} \cdot \underset{\text{ \tiny frac ocean}}{(0.70)}
\cdot \underset{\text{ \tiny frac liveable} }{\left( \frac 12
\right)} = 5.4 \times 10^{20} \text{ W} \text{ (ocean life energy
budget)} $$ $$ \cdot \underset{ \text{\tiny plankton eff}}{(0.10)}
\cdot \underset{\text{\tiny fish eff}}{(0.10)} = 5.4 \times
10^{18} \text{ W} \text{ (fish energy budget)} $$ $$ \cdot
\underset{\text{\tiny energy budget of man}}{\left( \frac{ 75
\text{ kg} }{ 2 \times 10^6 \text{ cal/day} } \right)} \cdot
\underset{\text{\tiny cal $\leftrightarrow$ Ws}}{\left( \frac{ 1
\text{ cal} }{ 4 \text{ Ws} } \right)} \cdot
\underset{\text{\tiny s $\leftrightarrow$ day}}{\left( \frac{ 60
\cdot 60 \cdot 24 \text{ s} }{ 1 \text{ day} } \right)} = 4.4
\times 10^{14} \text{ kg} \text{ (mass of fish)} $$ $$ \cdot
\underset{ \rho_{\text{fish}} = \rho_{\text{water}} }{\left(
\frac{ 1 \text{ m}^3 }{ 1000 \text{ kg} } \right)} \cdot
\underset{ \text{\tiny ocean surface}}{\left( \frac{ 1}{ 4 \pi (6
\times 10^6 \text{ m})^2 (0.7) } \right)} = \text{ change in depth
(m)} = 1.38 \times 10^{-3} \text{ m} \approx 1 \text{ mm} $$ So in
the end I get about a millimeter change in the ocean height. Honestly,
this is a lot larger than I expected. The ocean is a big place. I
suppose there are also a lot of fish in the world. If you look, if we
assume the average fish is about 10 kg, I've calculated that the
population of fish in the ocean is 4.4E13 fish, or 4 million billion
fish. That's a lot of fish. I'm not so sure about my estimate, so I'll
do it again from a different direction...

### Fishing

Next, I'll try and estimate again, this time guessing based on how much
we fish fish. I know that overfishing is a problem, which means that for
some fish species we fish more than fish make little fishies, so if I
can estimate how much fish we eat, I can estimate how much we fish, so I
can estimate how many fish there are, and then I can estimate how much
the ocean depth changes. This calculation is very rough, I took some
very basic order of magnitude guesses at some of the parameters. In
particular, I had to guess how many fish species we fish, which I took
to be 1/100 for no very good reason. My calculation is below: $$
\underset{\text{ \tiny fish eaten per person}}{ \left( \frac{ 1
\text{ fish}}{ 1 \text{ week}} \right)} \cdot \underset{\text{
\tiny fish weight}}{\left( \frac{1 \text{ kg}}{1 \text{
fish}}\right)} \cdot \underset{ \text{ \tiny week
$\leftrightarrow$ year}}{ \left( \frac{ 52 \text{ weeks}}{ 1 \text{
year} }\right)} \cdot \underset{\text{\tiny people who eat
fish}}{\left( 10^9 \right)} =5.2 \times 10^{9} \text{ fish/year
fished} $$ $$ \cdot \underset{\text{\tiny fish we eat}}{ \left(
\frac{100 \text{ tot fish}}{1 \text{ fish eaten}} \right) } \cdot
\underset{\text{\tiny fish lifetime}}{\left( 10 \text{ years}
\right)} = 5.2 \times 10^{13} \text{ kg (total fish)}$$ $$ \cdot
\underset{ \rho_{\text{fish}} = \rho_{\text{water}} }{\left(
\frac{ 1 \text{ m}^3 }{ 1000 \text{ kg} } \right)} \cdot
\underset{ \text{\tiny ocean surface}}{\left( \frac{ 1}{ 4 \pi (6
\times 10^6 \text{ m})^2 (0.7) } \right)} = \text{ change in depth
(m)} = 1.6 \times 10^{-4} \text{ m} \approx 0.2 \text{ mm} $$ This
time I got 0.2 mm or so, which is in relatively good agreement with my
other number. At least its not several orders of magnitude off.

### Geometric Average

Honestly I trust my first number more than the second, but I'm going to
average my two results in order to come up with the number that I'll
submit to the contest. But, I'm not going to average my two numbers
arithmatically: $$ \mu = \frac{1}{2} ( x_1 + x_2 ) $$ as you
normally do to average numbers, instead I am going to average them
*geometrically*, i.e. I'm going to take the square root of their
product: $$ \mu = \sqrt{ x_1 x_2 } $$

### My Answer

This kind of averaging is logarithmic in nature, and my experience has
been that it is much more successful average to use when you are doing
fermi problems. Doing this on my two numbers I obtain my entry: $$
\Delta x = \sqrt{ 0.164 \text{ mm} * 1.38 \text{ mm} } \approx
\frac{1}{2} \text{ mm} $$ About half a millimeter. I'll be sure to let
everyone know how I do in the contest. Drop us an email or leave a
comment to let me know how good you think my guess is. Happy Fishing.
