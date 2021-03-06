<--
.. title: Tragedy of Great Power Politics? Modeling International War
.. date: 2013-06-23 23:48:00
.. tags: books, modeling, war
.. category: old
.. slug: modeling-international-war
.. author: Brian
.. has_math: true
-->


<div style="float: right;">
<img src="/images/tgpp.jpg">
</div>

Recently I finished reading John Mearsheimer's excellent political science book
The Tragedy of Great Power Politics. In this book, Mearscheimer lays out his
``offensive realism'' theory of how countries interact with each other in the
world. The book is quite readable and well-thought-out -- I'd recommend it to
anyone who has an inkling for political history and geopolitics. However, as I
was reading this book, I decided that there was a point of Mearsheimer's
argument which could be improved by a little mathematical analysis.

The main tenant of the book is that states are rational actors who act to to
maximize their standing in the international system. However, states don't seek
to maximize their absolute power, but instead their relative power as compared
to the other states in the system. In other words, according to this logic the
United Kingdom position in the early 19th century -- when its army and navy
could trounce most of the other countries on the globe -- was better than it is
now -- when many other countries' armies and navies are comparable to that of
the UK, despite the UK current army and navy being much better now than they
were in the early 19th century. According to Mearsheimer, the main determinant
of state's international actions is simply maximizing its relative power in its
region. All other considerations -- capitalist or communist economy, democratic
or totalitarian government, even desire for economic growth -- matter little in
a state's choice of what actions it will take. (Perhaps it was this
simplification of the problem which made the book really appeal to me as a
physicist.)

<!-- more -->

Most of Mearsheimer's book is spent exploring the logical corollaries of his
main tenant, along with some historical examples. He claims that his idea has
three different predictions for three different possible systems. 1) A balanced
bipolar system (one where two states have roughly the same amount of power and
no other state has much to speak of) is the most stable. War will probably not
break out since, according to Mearsheimer, each state has little to gain from a
war. (His example is the Cold War, which didn't see any actual conflict between
the US and the USSR.) 2) A balanced multipolar system ($N>2$ states each share
roughly the same amount of power) is more prone to war than a bipolar system,
since a) there is a higher chance that two states are mismatched in power,
allowing the more powerful to push the less around, and b) there are more
states to fight. (One of his examples is Europe between 1815 and 1900, when
there were several great-power wars but nothing that involved the entire
continent at once.) 3) An unbalanced multipolar system ($N>2$ states with power,
but one that has more power than the rest) is the most prone to war of all. In
this case, the biggest state on the block is almost able to push all the other
states around. The other states don't want that, so two or more of them collude
to stop the big state from becoming a hegemon -- i.e. they start a war.
Likewise, the big state is also looking to make itself more relatively
powerful, so it tries to start wars with the little states, one at a time, to
reduce their power. (His examples here are Europe immediately before and
leading up to the Napoleonic Wars, WWI, and WWII.) There is another case, which
is unipolarity -- one state has all the power -- but there's nothing
interesting there. The big state does what it wants.

While I liked Mearsheimer's argument in general, something irked me about the
statement about bipolarity being stable. I didn't think that the stability of
bipolarity (corollary 1 above) actually followed from his main hypothesis.
After spending some extra time thinking in the shower, I decided how I could
model Mearsheimer's main tenant quantitatively, and that it actually suggested
that bipolarity was actually unstable!!


<a id="note1"></a>
Let's see if we can't quantify Mearsheimer's ideas with a model. Each state in
the system has some power, which we'll call $P_i$. Obviously in reality there are
plenty of different definitions of power, but in accordance with Mearsheimer's
definition, we'll define power simply in a way that if State 1 has power 
$P_1 > P_2$, the power of State 2, then State 1 can beat State 2 in a 
war[<sup>[1]</sup>](#fnote1).
Each state does not seek to maximize their total power $P_i$, but instead their
relative power $R_i$, relative to the total power of the rest of the states, So
the relative power $R_i$ would be
 
$$ R_i = P_i / \left( \sum_{j=1}^N P_j \right) \qquad , $$

where we take the sum over the relevant players in the system. If there was
some action that changed the power of some of the players in the system (say a
war), then the relative power would also change with time $t$:

$$ \frac{dR_i}{dt} = \frac{dP_i}{dt} \times \left( \sum_{j=1}^N P_j \right)^{-1} - P_i \times \left( \sum_{j=1}^N P_j \right)^{-2} \times \left(\sum_{j=1}^N \frac{dP_j}{dt} \right) \qquad (1) $$

A state will pursue an action that increases its relative power $R_i$. So if we
want to decide whether or not State A will go to war with State B, we need to
know how war affects a state's individual powers. While this seems intractable,
since we can't even precisely define power, a few observations will help us
narrow down the allowed possibilities to make definitive statements on when war
is beneficial to a state:

1. War always reduces a state's absolute power. This is simply a statement that
in general, war is destructive. Many people die and buildings are bombed,
neither of which is good for a state. Mathematically, this statement is that in
wartime, $dP_i/dt < 0$ always. Note that this doesn't imply that that $dR_i/dt$
is always negative.

<a id="note2"></a>

2. The change in power of two states A & B in a war should depend only on
how much power A & B have. In addition, it should be independent of the
labeling of states. Mathematically, $dP_a / dt = f(P_a, P_b)$, and 
$dP_b/dt = f(P_b, P_a)$ with the same function $f$[<sup>[2]</sup>](#fnote2).

3. If State A has more absolute power than State B, and both states are in a
war, then State B will lose power more rapidly than State A. This is almost a
re-statement of our definition of power. We defined power such that if State A
has more absolute power than State B, then State A will win a war against State
B. So we'd expect that power translates to the ability to reduce another
state's power, and more power means the ability to reduce another state's power
more rapidly.

4. For simplicity, we'll also notice that the decrease of a State A's absolute
power in wartime is largely dependent on the power of State B attacking it, and
is not so much dependent on how much power State A has.

In general, I think that assumptions 1-3 are usually true, and assumption 4 is
pretty reasonable. But to simplify the math a little more, I'm going to pick a
definite form for the change of power. The simplest possible behavior that
capture all 4 of the above assumptions is:

$$ \frac{dx}{dt} = -y \qquad \frac{dy}{dt} = -x \qquad (2) $$

<a id="note3"></a>
where $x$ is the absolute power of State X and $y$ is the absolute power of State
y. (I'm switching notation because I want to avoid using too many 
subscripts[<sup>[3]</sup>](#fnote3)). Here I'm assuming that the rate of 
change of State X's power is directly
proportional to State Y's power, and depends on nothing else (including how
much power State Y actually has). <a id="note4"></a>
We'll also call $r$ the relative power of State
X, and $s$ the relative power of State Y[<sup>[4]</sup>](#fnote4). 
Now we're equipped to see when war
is a good idea, according to our hypotheses.

Let's examine the case that was bothering me most -- a balanced bipolar system.
Now we have only two states in the system, X and Y. For starters, let's address
the case where both states start out with equal power $(x = y)$. If State X goes
to war with State Y,  how will the relative powers $r =x/(x+y)$ & $s=y/(x+y)$
change? Looking at Eq. (1), we see that by symmetry both states have to lose
absolute power equally, so $x(t) = y(t)$ always, and thus $r(t) = s(t)$ always. In
other words, from a relative power perspective it doesn't matter whether the
states go to war! For our system to be stable against war, we'd expect that a
state will get punished if it goes to war, which isn't what we have! So our
system is a neutral equilibrium at best.

But it gets worse. For a real balanced bipolar system, both states won't have
exactly the same power, but will instead be approximately equal. Let's say that
the relative power between the two states differs by some small (positive)
number $e$, such that $x(0) = x0$ and $y(0) = x0 + e$. Now what will happen? Looking
at Eq. (2), we see that, at $t=0$,

$$ \frac{dr}{dt} = -(x_0 + e) / (2x_0 + e) + x_0(2x_0 + e) / (2x_0 + e)^2  = -e/(x_0 + e) $$

$$ \frac{ds}{dt} = -(x_0) / (2x_0 + e) + (x_0+e)(2x_0 + e) / (2x_0 + e)^2 = + e/(x_0 + e) \qquad .  $$

In other words, if the power balance is slightly upset, even by an
infinitesimal amount, then the more powerful state should go to war! For a
balanced bipolar system, peace is unstable, and the two countries should always
go to war according to this simple model of Mearsheimer's realist world.

Of course, we've just considered the simplest possible case -- only two states
in the system (whereas even in a bipolar world there are other, smaller states
around) who act with perfect information (i.e. both know the power of the other
state) and can control when they go to war. Also, we've assumed that relative
power can change only through a decrease of absolute power, and in a
deterministic way (as opposed to something like economic growth). To really say
whether bipolarity is stable against war, we'd need to address all of these in
our model. A little thought should convince you which of these either a) makes
a bipolar system stable against war, and b) makes a bipolar system more or less
stable compared to a multipolar system. Maybe I'll address these, as well as
balanced and unbalanced multipolar systems, in another blog post if people are
interested.

<a id="fnote1"></a>
1. [^](#note1) $P_i$ has some units (not watts). My definition of power is strictly
comparative, so it might seem that any new scale of power $p_i = f(P_i)$ with an
arbitrary monotonic function $f(x)$ would also be an appropriate definition.
However, we would like a scale that facilitates power comparisons if multiple
states gang up on another. So we would need a new scale such that 

$$ p_{i+j} = f(P_i + P_j) = f(P_i) + f(P_j) = p_i + p_j $$ 

for all $P_i, P_j$ . The only function that behaves like this is a linear function of 
$P(p_i) = A \times P_i $, where A is some constant. So our definition of power is 
basically fixed up to what "units" we choose. Of course, defining $P_i$ in terms 
of tangibles (e.g. army size or GDP or population size or number of nuclear warheads) 
would be a difficult task. Incidentally, I've also implicitly assumed here that there is a power scale,
such that if $P_1 > P_2$, and $P_2 > P_3$, then $P_1 > P_3$. But I think
that's a fairly benign assumption.

<a id="fnote2"></a>
2. [^](#note2) This implicity assumes that it doesn't matter which state attacked the
other, or where the war is taking place, or other things like that.

<a id="fnote3"></a>
3. [^](#note3) Incidentally this form for the rate-of-change of the power also has the
advantage that it is scale-free, which we might expect since there is no
intrinsic "power scale" to the problem. Of course there are other forms with
this property that follow some or all of the assumptions above. For instance,
something of the form $dx/dt = -xy = dy/dt$ would also be i) scale-invariant, and
ii) in line with assumptions 1 &amp; 2 and partially inline with assumption 3.
However I didn't use this since a) it's nonlinear, and hence a little harder to
solve the resulting differential equations analytically, and b) the rate of
decrease of both state's power is the same, in contrast to my intuitive feeling
that the state with less power should lose power more rapidly.

<a id="fnote4"></a>
4. [^](#note4) Homework for those who are not satisfied with my assumptions: Show that any
functional form for $dP_i/dt$ that follows assumptions 1-3 above does not change
the stability of a balanced bipolar system.
