<--
.. title: Fun Fact: Lebron James Plays Basketball
.. date: 2011-02-07 12:37:00
.. tags: statistics, basketball, Bohn, lebron james
.. category: old
.. slug: fun-fact-lebron-james-plays-basketball
.. author: Bohn
.. has_math: true
-->


[![image](http://turbo.inquisitr.com/wp-content/2010/07/lebron-james.jpg)](http://turbo.inquisitr.com/wp-content/2010/07/lebron-james.jpg)
Between building airplanes and playfully destroying everyone else in my
apartment at Super Smash Brothers, my roommate Nathan brought up an
interesting recent fact about LeBron James. He told me that LeBron
scored 11 consecutive field goals (not in football... you know who you
are) in one game. Apparently this was a pretty special event, but how
rare is it for a player of LeBron's caliber? TO THE SCIENCE-MOBILE! The
Problem! [ESPN 8, The
Ocho](http://www.youtube.com/watch?v=kHltCzuwlOs&feature=related) tells
me that LeBron's career field goal percentage is 47.5%. Considering the
number of shots he takes, this is a pretty good number. To compare, the
highest field goal percentage for a single season was Wilt Chamberlin
with 72.7%, but eye witness testimony says he was around 10 feet tall
and would wait in the offensive paint all game. Let's see how improbable
this 11 in a row streak is. The generic question we are going to need to
answer is as follows: If a basketball player takes N shots in one game,
with a shooting probability of q, what is the probability that the
player will make AT LEAST k shots in a row? We'll call this probability
P(N) This turns out to be a tricky problem, but let's take a shot (awful
pun... I sincerely apologize). We can take care of simple cases: If N <
k, then P(N) = 0. This tells us you can't have a streak of k if you
don't take k shots! If N = k, P(N) = q^k. This is the probability of
getting k in a row if you take k shots, not too surprising yet. When N
\> k, things get more interesting. Finding the Recurrence Relation Our
goal is to write a relationship that has this form: P(N) = P(N-1) +
blank What's blank? "You don't worry about blank... let me worry about
blank!" We'll need to look at the [inclusion-exclusion
principle](http://en.wikipedia.org/wiki/Inclusion_exclusion_principle).
This principle basically says that when we want to take all DISTINCT
items in two sets, we need to take all of the elements in one set, and
add all elements in the second set which are DISTINCT from the first.
For example, if A = {0, 1, 2, 3, 4} and B = {3, 4, 5, 6, 7, 8}, then the
union of A and B is {0, 1, 2, 3, 4, 5, 6, 7, 8}. Note that I did not
include 3 and 4 twice. Let's take a look at the expertly designed (5
minutes before class) google docs drawing below:
[![image](https://docs.google.com/drawings/pub?id=1Ef34hZJ9mtF-GDUSpmJA4Ke2mS3BAHLsDwAk1GX19Dc&w=1122&h=485)](https://docs.google.com/drawings/pub?id=1Ef34hZJ9mtF-GDUSpmJA4Ke2mS3BAHLsDwAk1GX19Dc&w=1122&h=485)
The entire line represents N shots being taken. Each shot gets its own
little column (not all columns shown). Using the inclusion-exclusion
principle with the following sets will give us the answer. Choose A to
be the first N-1 shots, and B to be all N shots. The principle tells us
first to take everything from A, which is the probability P(N-1) shown
in red. B will be the entire line, but the principle tells us to only
add DISTINCT chances from B. Since the only difference in B is one more
shot than A, the only distinct chance for a streak of k shots will be in
the last k shots, shown in yellow as P(k). This is only distinct if the
(k+1)th to last shot shown in green is missed! Otherwise a streak of k
would have been included in A already. There is one more place for a
streak to be already included in A. If there was a streak in the blue
section, we must not include the B streak so we don't double count.
Phew... Let's put this all together by multiplying the probabilities of
each of those events: P(N) = P(N-1) + (probability of yellow
streak)*(probability we miss green)*(probability of no streak in blue)
$$P(N) = P(N-1) + q^k \times (1-q) \times (1 - P(N-k-1))$$ This gives
us a recurrence relation for the probabilities! This is a general
statement about the probability of at least one streak of length k out
of N chances, given each has a probability q. Since I'm just going to
plug this into Python anyway to handle the data, this equation is good
enough. The expectation value of an event is the probability multiplied
by the number of chances. For example, the expectation value of getting
heads with 2 tosses is just (1/2)*2 = 1. The plan is to compile a list
of his field goal attempts in every game LeBron has played in the NBA,
and sum the expectation values for each N. $$ \mbox{Expectation} =
\sum_i P(i) \times \mbox{(number of games with i shots)} $$ Using
LeBron's actual field goal attempt data for each game (up to February 4,
2011), we find that LeBron is expected number of games with at least a
streak of 11 in a row is 1.128. This is a higher expectation value than
the number of heads in 2 coin flips! So this is MORE expected than the
number of heads we would see with 2 coin flips. This isn't very exciting
given the number of shots he has taken and his shooting percentage. Data
Tables

Consecutive Shots

Expected out of 667

Percent of Games

1

666.9

99.99

2

643.6

96.49

3

489.0

73.32

4

281.8

42.25

5

140.0

21.00

6

65.23

9.780

7

29.55

4.431

8

13.20

1.980

9

5.854

0.8778

10

2.578

0.3866

11

1.128

0.1691

12

0.4898

0.07344

13

0.2110

0.03164

14

0.09011

0.01351

15

0.03807

0.005709

16

0.01592

0.002387

17

0.006560

0.0009839

18

0.002660

0.0003995

19

0.001067

0.0001600

20

0.0004180

6.267E-05

21

0.0001599

2.397E-05

22

6.03E-05

9.033E-06

23

2.22E-05

3.328E-06

24

8.06E-06

1.208E-06

25

2.84E-06

4.259E-07

26

9.98E-07

1.495E-07

27

3.51E-07

5.255E-08

28

1.20E-07

1.797E-08

29

3.92E-08

5.870E-09

30

1.15E-08

1.717E-09

31

3.45E-09

5.171E-10

32

1.06E-09

1.589E-10

33

3.37E-10

5.050E-11

34

7.23E-11

1.083E-11

35

1.70E-11

2.554E-12

36

2.30E-12

3.442E-13

The streak in question is highlighted in red, so it appears we expect it
to happen 0.169% of his games. The Realization Of course I did all of
this before looking up the [actual
article](http://espn.go.com/nba/truehoop/miamiheat/notebook/_/page/heatreaction-110203/miami-heat-orlando-magic).
I'll quote the blurb here:

> LeBron James set a personal record by making his first 11 field goals
> to start the game. His previous career-high was 10 straight field
> goals after tip-off, recorded against Chicago in 2008. After hitting
> his first 11 field goal attempts on Thursday night, James shot
> 6-for-14 thereafter.

Well... this calculation just got a bit easier. He has played 667 games,
and the probability of getting 11 straight off the bat is q^k =
0.475^11 = 0.0002777. Multiply this by 667 games to get the expected
value of 0.185. Sure this is 6 times smaller than our previous
calculation; however it's still not statistically that impressive. How
would LeBron's expected number change if he shot the same percentage
(72.7%) as Wilt for his record breaking season? The expected number of
games with 11 in a row during the game would be 72.38 games!! So this is
incredibly dependent on the shooting percentage. We have a factor of
q^k everywhere! Certainly it's dependent on the number of shots taken
in a game too. The probability P(N) is a monotonically increasing
function! Moral Given LeBron's shooting percentage and high number of
shots per game, we expect that he would have at least 1 of these streak
of 11 games so far in his career. This is certainly not to diminish this
feat though. You still need to take 20 some shots a game in the NBA with
nearly 50% shooting accuracy! We also have a nice formula to apply to
more sports streaks! More to come...
