Title: Pi storage
Date: 2012-03-14 15:13:00
Tags: pi day, fun, probability, storage
Category: old
Slug: pi-storage
Author: Alemi


[![image](http://4.bp.blogspot.com/-4x2fD-exJns/T2DAEJqroqI/AAAAAAAAAbI/8_9quiDP4p0/s320/floppies.jpg)](http://4.bp.blogspot.com/-4x2fD-exJns/T2DAEJqroqI/AAAAAAAAAbI/8_9quiDP4p0/s1600/floppies.jpg)

Let me share my worst "best idea ever" moment. Sometime during my
undergraduate I thought I had solved all the world's problems. You see,
on this fateful day, my hard drive was full. I hate it when my hard
drive fills up, it means I have to go and get rid of some of my stuff. I
hate getting rid of my stuff. But what can someone do? And then it hit
me, I had the bright idea:

> What if we didn't have to *store* things, what if we could just
> *compute* files whenever we wanted them back?

Sounds like an awesome idea, right? I know. But how could we compute our
files? Well, as you may know pi is conjectured to be a [normal
number](http://en.wikipedia.org/wiki/Normal_number), meaning its digits
are probably random. We also know that it is irrational, meaning pi
never ends.... Since its digits are random, and they never end, in
principle any sequence you could ever imagine should show up in pi
eventually. In fact there is a nifty website
[here](http://pi.nersc.gov/) that will let you search for arbitrary
strings (using a 5-bit format) in first 4 billion digits, for example
"alemi" [seems to show
up](http://pi.nersc.gov/cgi-bin/pi.cgi?word=alemi&format=char) at around
digit 3149096356. So in principle, I could send you just an index, and a
length, and you could compute the resulting file. But wait you cry,
isn't computing digits of pi hard, don't people work really hard to
compute pi farther and farther? Hold on I claim, first of all, I'm
imagining a future where computation is cheap. Secondly, there is a
really neat algorithm, the [BBP
algorithm](http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula),
that enables you to compute the kth binary digit of pi without knowing
any of the preceding digits. In other words, in principle if you wanted
to know the 4 billionth digit of pi, you can compute it without having
to first compute the first 4 billion other digits. Cool, this is
beginning to sound like a really good idea. What's the catch? Perhaps
you've already gotten a taste of it. Let's try to estimate just how far
along in pi we would have to look before our message of interest shows
up. Let's assume we have written our file in binary, and are computing
pi in binary e.g.

> 11. 00100100 00111111 01101010 10001000 10000101 10100011 00001000
> 11010011

etc. So, if the sequence is random, there is a 1/2 chance that at any
point we get the right starting bit of our file, and then a 1/2 chance
we get the next one, etc. So the chance that we would create our file if
we were randomly flipping coins would be $$ P = \left( \frac{1}{2}
\right)^N = 2^{-N} $$ if our file was N bits long. So where do we
expect this sequence to first show up in the digits of pi? Well, this
turns out to be a [subtle
problem](http://mathworld.wolfram.com/CoinTossing.html), but we can get
a feel for it by assuming that we compute N digits of pi at a time and
see if its right or not. If its not, we move on to the next group of N
digits, if its right, we're done. If this were the case, we should
expect to have to draw about $$ \frac{1}{P} = 2^N $$ times until we
have a success, and since each trial ate up N digits, we should expect
to see our file show up after about $$ N 2^N $$ digits of pi. Great, so
instead of handing you the file, I could just hand you the index the
file is located. But how many bits would I need to tell you that index.
Well, just like we know that 10^3 takes 4 digits to express in decimal,
and 6 x 10^7 takes 8 digits to express, in general it takes $$ d =
\log_b x + 1 $$ digits to express a number in base b, in this case it
takes $$ d = \log_2 ( N 2^N ) + 1= \log_2 2^N + \log_2 N + 1 = N
+ \log_2 N + 1 $$ digits to express this index in binary. And there's
the rub. Instead of sending you N bits of information contained in the
file, all my genius compression algorithm has manged to do is replace N
bits of information in the file, with a number that takes \( \~ N +
\log_2 N \) bits to express. I've actually managed to make the files
larger not smaller! You may have noticed above, that even for the simple
case of "alemi", all I managed to do was swap the binary message

> alemi -\> 0000101100001010110101001 with the index 3149096356 -\>
> 10111011101100110110010110100100

which is longer in binary! As an aside, you may have felt uncomfortable
with my estimation for how long we have to wait to see our message, and
you would be right. Just because all N digits I draw at a time don't
match up doesn't mean that the second half isn't useful. For instance if
I was looking for 010, lets say some of the digits are 101,010. While
both of those sequences didn't match, if I was looking at every digit at
a time, I would have found a match. And you'd be right. [Smarter people
than I](http://www.cs.elte.hu/~mori/cikkek/Expectation.pdf) have
computed just how long you should have to wait, and end up with the
better estimation $$ \text{wait time} \sim 2^N N \log 2 $$ which is
pretty darn close to our silly estimate.
