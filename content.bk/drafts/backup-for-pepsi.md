Title: BACKUP FOR PEPSI
Date: 2010-06-08 00:48:00
Tags: 
Category: old
Slug: backup-for-pepsi
Author: Corky
Status: draft

I found it easier to find the probability that I will not win after a
given number of caps. In order to not win the game, we can have at most
two caps of the same team from a pool of thirty possible teams. So let's
first define a few terms.
$$ n = \\text{Total Number of Caps} $$
$$ n\_{half} = \\text{ Half of n, Rounded Down} $$
$$ g\_{2} = \\text{Number of Repeated Teams} $$
$$ g = \\text{Total Number of Unique Teams} $$
From these terms we can also see that the number of unique teams, g, is
just the number of repeated teams plus the number of unrepeated teams,
or:
$$ g = (n - 2g\_{2}) + g\_{2} = n - g\_{2} .$$
Now we need to find all the combinations of ways that we can lose for a
given number of caps n. This is just a sum over all the ways we can pick
out n caps where we choose a given team no more than two times. This
turns out to be
$$ \\displaystyle\\sum\\limits\_{g\_{2}=0}\^{n\_{half}} \\binom{30}{g}
\\left( \\frac{n!}{ \\left(2!\\right)\^g\_{2} \\left(1!
\\right)\^{g-g\_{2}}} \\right) \\binom{g}{g\_{2}} $$
where
$$ \\binom{30}{g} = \\frac{30!}{g! (30-g)!} $$
is the number of ways to choose g unique teams out of thirty possible
teams,
$$ \\left( \\frac{n!}{ \\left(2!\\right)\^g\_{2} \\left(1!
\\right)\^{g-g\_{2}}} \\right) $$
is the number of unique ways of permuting n caps of g unique teams and
g\_2 groups of repeated teams, and
$$ \\binom{g}{g\_{2}} = \\frac{g!}{g\_{2}! (g-g\_{2})!} $$
is the number of ways of g groups where g\_2 are groups of two and the
rest are groups of one.
To get a probability, all we have to do now is divide the total number
of ways of losing by the total number of orderings of any kind, which
for n caps is just
$$ N = 30\^n . $$
So our probability of losing after n caps is
$$ P\_{loss} = \\left(\\frac{1}{30} \\right)\^n
\\displaystyle\\sum\\limits\_{i=0}\^{n\_{half}} \\binom{30}{g} \\left(
\\frac{n!}{ \\left(2!\\right)\^g\_{2} \\left(1! \\right)\^{g-g\_{2}}}
\\right) \\binom{g}{g\_{2}}, $$
where I can do the sum by making the substitution for g in terms of g\_2
as given above.
Thus the probability of winning AT LEAST once is given by
$$ P\_{win} = 1 - P\_{loss}. $$
Since this would be a pain to calculate out by hand, I just wrote
another program to calculate these sums for each value of n.
