<--
.. title: My Pepsi* Challenge
.. date: 2010-06-08 01:30:00
.. tags: pepsi, how do i get free stuff?, scott bakula, baseball
.. category: old
.. slug: my-pepsi-challenge
.. author: Corky
.. has_math: true
-->


[![image](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAz2-SbRtAI/AAAAAAAAAFY/eaUWEFQHTDs/s200/bottles.png)](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAz2-SbRtAI/AAAAAAAAAFY/eaUWEFQHTDs/s1600/bottles.png)The
basement of the Physics building has a Pepsi machine. Over the course of
two semesters Alemi and I have deposited roughly the equivalent of the
GDP of, say, Monaco to this very same Pepsi machine (see left, with most
of Landau and Lifshitz to scale). It just so happens that Pepsi is now
having a contest, called "Caps for Caps," in which it is possible to win
a baseball hat. There are several nice things about this contest.
Firstly, I drink a lot of soda. Secondly, I like baseball hats. So far
so good. Lastly (and most important for this post), is that it is fairly
straightforward to calculate the statistics of winning (or at least
simulate them).
So how does the game work? Well, on each soda cap the name of a Major
League Baseball team is printed. All thirty teams are (supposedly)
printed with the same frequency, so the odds of getting any particular
team are 1/30. You can win a hat by collecting three caps with the same
team printed on them. So if I had five caps, the following would be a
win:
Phillies Cubs Tigers Phillies Phillies
whereas the following would not win me anything:
Yankees Rays Blue Jays Orioles Royals
and I would also lose if I had:
Mets Nationals Braves Braves Mets.
In addition, one in eight caps gets you 15% off on some $50 dollar or
more purchase to MLB.com or something like that. For simplicity, I
ignored these 15% off guys, but all they will do is push back the number
of caps you need by one for every eight purchased. It should not be too
difficult to factor these ones in, but I was lazy and I already made all
these nice graphs, so...
The first thing I tried to do was just simulate the contest. I wrote a
little Python script that randomly generates a team for each cap and
counts my wins over a given number of caps purchased. Running this about
100,000 times for all number of caps between 1 and 61 (with 61
guaranteed to win) and averaging over the number of wins, I could
determine both the expected number of wins per cap value and the
probability of winning at least once. The results are shown below.
[![image](http://4.bp.blogspot.com/_fa6AZDCsHnY/TAwPaC7VV-I/AAAAAAAAAEA/ei6DPQ09bmI/s400/CapsforCaps(sim1).png)](http://4.bp.blogspot.com/_fa6AZDCsHnY/TAwPaC7VV-I/AAAAAAAAAEA/ei6DPQ09bmI/s1600/CapsforCaps(sim1).png)
[![image](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAxwinoE0FI/AAAAAAAAAFA/VTOnToOXcmM/s400/WinsvsSodas.png)](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAxwinoE0FI/AAAAAAAAAFA/VTOnToOXcmM/s1600/WinsvsSodas.png)
But we can also exactly solve this game. This turned out to take longer
for me (I'm bad at probability) than just simulating the darn thing. I
had initially included my derivation in the post but it was long,
muddled, and none too illuminating, so I took it out. But I super-duper
promise I did it and can post if you really really want to know.
Otherwise, I have just plotted the predicted results below (as a red
curve) along with the simulated data (blue dots). Turns out they agree
pretty well!
[![image](http://4.bp.blogspot.com/_fa6AZDCsHnY/TAxxKz3m-MI/AAAAAAAAAFI/S6YpmCcO1Fs/s400/CapsforCapsSimandPred.png)](http://4.bp.blogspot.com/_fa6AZDCsHnY/TAxxKz3m-MI/AAAAAAAAAFI/S6YpmCcO1Fs/s1600/CapsforCapsSimandPred.png)
Just eyeballing the graph, we see that after 18 or 19 sodas the chances
of winning are about a half. Beyond about 25 or so it appears to be
almost 90% that you'll win at least once. In reality, these percentages
would occur about 2 or 3 caps later to compensate for the 15% off
thingies. So now that we have some numbers and can trust our model a
bit, let's see how worth it this contest is for us.
First, we can ask: Is this a good way to get a hat cheaper than retail
value (about $15)? To quantify "worth it" I have chosen to find the
value of winnings (price of hat times expected number of wins) minus the
cost of caps (how much I spend on soda). I am fairly embarrassed to say
that the cost of each soda is $1.75. See plot below.
[![image](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAxzBhvw-4I/AAAAAAAAAFQ/RiKEfFBDqig/s400/ValueDifferential.png)](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAxzBhvw-4I/AAAAAAAAAFQ/RiKEfFBDqig/s1600/ValueDifferential.png)
From this plot, we see that it doesn't become "worth it" (that is, value
of winnings is greater than cost of sodas) until about 40 sodas
purchased. That's a lot! In fact, we see that just when I start feeling
pretty confident I'll win something (around 20-25 sodas), I'm right in a
big valley of "totally not worth it." So if I just want a baseball hat,
I'm better off forking over the $15 dollars.
Although, one does see from this plot that once I get above about 40 or
so sodas, it becomes much more cost effective to just keep buying sodas
and winning hats. However, Pepsi tries to stifle this a bit in the
[rules](http://www.pepsiusa.com/capsforcaps/), stating that "Limit one
(1) Official MLB® baseball cap per name, address or household." Unless I
either make a lot of friends real soon or develop a creative definition
of my address, it looks like I'm out of luck.
But what if I want a hat but I don't want to actually buy soda like a
chump? This contest, like many others, needs to have a "No Purchase
Necessary" clause for some legal reason or another (so they aren't
lotteries or gambling or something). I had assumed they (the nameless
overlords at Pepsi) would limit the number of caps possible from just
mailing in, but it doesn't seem that way. From the Official rules,
Chapter Two, verses nine to twenty-one:
"Limit one (1) free game piece per request, per stamped outer envelope."
That sounds to me like you could get as many as you want, as long as you
use different envelopes. So we can redo our cost analysis with the cost
of getting one cap as the cost of a stamp. Putting the value of a cap
now at the cost of a stamp (44 cents), we get the following:
[![image](http://2.bp.blogspot.com/_fa6AZDCsHnY/TAz3jfb-KcI/AAAAAAAAAFg/erU1nZU7ZCg/s400/mailincaps.png)](http://2.bp.blogspot.com/_fa6AZDCsHnY/TAz3jfb-KcI/AAAAAAAAAFg/erU1nZU7ZCg/s1600/mailincaps.png)
Zooming in:
[![image](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAz3tj6kg8I/AAAAAAAAAFo/MDHgjjjS2J0/s400/mailinZoom.png)](http://1.bp.blogspot.com/_fa6AZDCsHnY/TAz3tj6kg8I/AAAAAAAAAFo/MDHgjjjS2J0/s1600/mailinZoom.png)
Hey, that seems worth it! And it should, since from above we saw that
the probability of winning after about 30 caps was in the high 90% 's.
The cost of getting 30 caps this way is the cost of 30 stamps, which is
less than the $15 that the hat is (supposedly) worth. So if I really
wanted a hat from this contest and didn't feel like drinking all my
money away, I'd just send away for the mail-in pieces.
I may try this method, since it seems to be allowed under the rules.
Although, even a strict constructionist reading of the contest rules
pretty much allows Pepsi to do whatever the heck it wants. Either way,
I'll be sure to update to see how well my model holds up!
-------
*NOTE: In no way is The Virtuosi blog affiliated in any way with Pepsi.
We may occasionally purchase Pepsi products (like sweet tasting Wild
Cherry Pepsi!), but we don't do it because we think it makes us look
"cool" or "hip" or "rad" (we KNOW it does). In fact, drinking too much
soda can have certain adverse health effects (like making you stronger,
faster, and in general more attractive). So if you want to have a Pepsi
product (like sweet tasting Wild Cherry Pepsi!) every now and then
(literally, EVERY INSTANT), go ahead. But drinking too many Pepsi
products (like sweet tasting Wild Cherry Pepsi!) could make you sick
(with awesome-itis).
