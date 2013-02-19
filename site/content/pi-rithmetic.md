Title: Pi-rithmetic
Date: 2012-03-14 11:52:00
Tags: order of magnitude, pi day, approximation, pi-rithmetic
Category: old
Slug: pi-rithmetic
Author: Alemi

<div class="separator" style="clear: both; text-align: center;"></div><div class="separator" style="clear: both; text-align: center;"></div><div class="separator" style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/-7rfL9Iby34A/T2C3LhSj_6I/AAAAAAAAAa0/rXTR30c77bk/s1600/IMAG0200.jpg" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" height="188" src="http://2.bp.blogspot.com/-7rfL9Iby34A/T2C3LhSj_6I/AAAAAAAAAa0/rXTR30c77bk/s320/IMAG0200.jpg" width="320" /></a></div>Fun fact:  pi squared is very close to 10.  How close?  Well, <a href="http://www.wolframalpha.com/input/?i=%2810+-pi%5E2+%29%2Fpi%5E2">Wolfram Alpha</a> tells me that it is only about 1% off.

I first realized this fact when looking at my slide rule, pictured to the left (click to embiggen), just another reason why slide rules are awesome.

It turns out I use this fact all of the time.  How's that you ask?  Well, I use this fast to enable me to do very quick mental arithmetic. 
<a name='more'></a>

It goes like this.  For every number you come across in a calculation, drop all of the information save two parts, first, what's its order of magnitude, that is, how many digits does it have, and second, is it closest to 1, pi, or 10?

The first part amounts to thinking of every number you come across as it looks in scientific notation, so a number like 2342 turns into 2.342 x 10^3, so that I've captured its magnitude in a power of 10.  As for the next part, the rules I usually use are:

<ul><li>If the remaining bit is between 1 and 2, make it 1</li><li>If its between 2 and 6.5 make it pi</li><li>if its bigger than 6.5, make it another 10</li></ul><div>Another way to think of this is to estimate every number to be a power of ten, and then either 1, a few, or 10.  The reason I choose pi is because if I use pi, I know how the rest of the arithmetic should work, namely, I only need to know a few rules, plus when I use this to estimate answers of physics formulae, making a bunch of pis show up tends to help me cancel other natural pis that are in the formulae.</div><div>
</div><div>$$ \pi \times \pi \sim10 \qquad \frac{1}{\pi} \sim \frac{\pi}{10} \qquad \sqrt{10} \sim \pi $$</div><div>Which you might notice is just the same approximation written in 3 different ways.</div><div>
</div><div>Let's work an example</div><div>   $$  \begin{align*}  23 \times 78 / 13 \times 2133  &amp;= ? \\ \pi \times 10 \times 100 / 10 \times \pi \times 10^3 &amp;= ? \\ \pi^2 \times 10^5 &amp;\sim 10^6 \\ \end{align*}$$</div><div>
</div><div>of course the <a href="http://www.wolframalpha.com/input/?i=23+*+78%2F13+*+2133">real answer</a> is 294,354, so you'll notice I got the answer wrong, but I only got it wrong by a factor of 3, which is pretty good for mental arithmetic, and in particular mental arithmetic that takes no time flat.</div><div>
</div><div>In fact, the average error I introduce by using this approximation is just 30% or so for each number, which I've shown below [the script that produced this plot for those interested is <a href="https://gist.github.com/2037431">here</a>].</div><div>
</div><div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/-uwGlV6y_pps/T2C90lPhmQI/AAAAAAAAAbA/k_Hl8H-y2ys/s1600/pierr.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="231" src="http://3.bp.blogspot.com/-uwGlV6y_pps/T2C90lPhmQI/AAAAAAAAAbA/k_Hl8H-y2ys/s320/pierr.png" width="320" /></a></div><div>
</div><div>So, there you go, now you can impress all of your friends with a simple mental arithmetic that gets you within a factor of 3 or so on average.</div>
