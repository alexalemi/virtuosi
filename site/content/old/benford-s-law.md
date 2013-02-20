Title: Benford's Law
Date: 2010-12-31 14:42:00
Tags: statistics, benford, scott bakula
Category: old
Slug: benford-s-law
Author: Corky


Given a large set of data (bank accounts, river lengths, populations, etc) what is the probability that the first non-zero digit is a one?  My first thought was that it would be 1/9.  There are nine non-zero numbers to choose from and they should be uniformly distributed, right? 

Turns out that for almost all data sets naturally collected, this is not the case.  In most cases, one occurs as the first digit most frequently, then two, then three, etc.  That this seemingly paradoxical result should be the case is the essence of Benford's Law.

<a name='more'></a>Benford's Law [1] states that for most real-life lists of data, the first significant digit in the data is distributed in a specific way, namely:

$$ P(d) = \mbox{log}_{10}\left(1 + \frac{1}{d}\right) $$

The probabilities for leading digits are roughly P(1) = 0.30, P(2) = 0.18, P(3) = 0.12, P(4) = 0.10, P(5) = 0.08, P(6) = 0.07, P(7) = 0.06, P(8) = 0.05, P(9) = 0.04.  So we would expect the first significant digit to be a one almost 30% of the time!

But where would such a distribution come from?  Well, it turns out that it comes from a distribution that is logarithmically uniform.  We can map the interval [1,10) to the interval [0,1) by just taking a logarithm (base ten).  These logarithms are then distributed uniformly on the interval [0,1). 

We can now get some grasp for why one should occur as the first digit more often in a uniform log distribution.  In the figure below, I have plotted 1-10 on a logarithm scale.  In a uniform log distribution, a given point is equally likely to be found anywhere on the line.  So the probability of getting any particular first digit is just its length along that line.  Clearly, the intervals get smaller as the numbers get bigger.
<div class="separator" style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/_fa6AZDCsHnY/TR4s91iaKKI/AAAAAAAAAIU/uxYE4eqknCY/s1600/logscale.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="300" src="http://2.bp.blogspot.com/_fa6AZDCsHnY/TR4s91iaKKI/AAAAAAAAAIU/uxYE4eqknCY/s400/logscale.png" width="400" /></a></div><div class="separator" style="clear: both; text-align: left;">But we can quantify this, too.  For a first digit on the interval [1,10), the probability that the first digit is <i>d</i> is given by:</div>
$$ P(d) = \frac{\mbox{log}_{10}(d+1) -\mbox{log}_{10}(d)}{\mbox{log}_{10}(10) -\mbox{log}_{10}(1)} $$

which is just

$$ P(d) =\mbox{log}_{10}(d+1) -\mbox{log}_{10}(d) $$

or

$$ P(d) = \mbox{log}_{10}\left( 1 + \frac{1}{d} \right) $$

which is the distribution of Benford's Law.

So how well do different data sets follow Benford's Law?  I decided to test it out on a couple easily available data sets: pulsar periods, U.S. city populations, U.S. county sizes and masses of plant genomes.  Let's start first with pulsar periods.  I took 1875 pulsar periods from the ATNF Pulsar Database (found <a href="http://www.atnf.csiro.au/research/pulsar/psrcat/">here</a>).  The results are plotted below.  The bars represent the fraction of numbers that start with a given digit and the red dots are the fractions predicted by Benford's Law. 
<div class="separator" style="clear: both; text-align: center;"><a href="http://4.bp.blogspot.com/_fa6AZDCsHnY/TRpObM6LxrI/AAAAAAAAAH8/tz9WQ98H258/s1600/benford_pulsar.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="300" src="http://4.bp.blogspot.com/_fa6AZDCsHnY/TRpObM6LxrI/AAAAAAAAAH8/tz9WQ98H258/s400/benford_pulsar.png" width="400" /></a></div>From this plot, we see that the pulsar period data shows the general trend of Benford's Law, but not exactly. 

Now let's try U.S. city populations.  This data was taken from the U.S. census bureau from the 2009 census and contains population data for over 81,000 U.S. cities.  We see from the chart below that there is a near exact correspondence between the observed first-digit distribution and Benford's Law.
<div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/_fa6AZDCsHnY/TRpQhzrSFmI/AAAAAAAAAIA/ZP3YTbWiiM4/s1600/benford_uscities09.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="300" src="http://3.bp.blogspot.com/_fa6AZDCsHnY/TRpQhzrSFmI/AAAAAAAAAIA/ZP3YTbWiiM4/s400/benford_uscities09.png" width="400" /></a></div>Also from the U.S. census bureau, I got the data for the land area of over 3000 U.S. counties.  These data also conform fairly well to Benford's Law.
<div class="separator" style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/_fa6AZDCsHnY/TRpSE9pHC1I/AAAAAAAAAII/dqG382dqoCw/s1600/benford_land.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="300" src="http://2.bp.blogspot.com/_fa6AZDCsHnY/TRpSE9pHC1I/AAAAAAAAAII/dqG382dqoCw/s400/benford_land.png" width="400" /></a></div>Finally, I found <a href="http://data.kew.org/cvalues/CvalServlet?querytype=1">this</a> neat website that catalogs the genome masses of over 2000 different species of plants.  I'm not totally sure <i>why</i> they do this, but it provided a ton of easy-to-access data, so why not?
<div class="separator" style="clear: both; text-align: center;"><a href="http://1.bp.blogspot.com/_fa6AZDCsHnY/TRpR82I2X1I/AAAAAAAAAIE/XdFQozbC7eY/s1600/benford_plant.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="300" src="http://1.bp.blogspot.com/_fa6AZDCsHnY/TRpR82I2X1I/AAAAAAAAAIE/XdFQozbC7eY/s400/benford_plant.png" width="400" /></a></div>
Neat, so we see that wide variety of natural data follow Benford's Law (some more examples <a href="http://mathworld.wolfram.com/BenfordsLaw.html">here</a>).  But why should they?  Well, as far as I have gathered, there are a few reasons for this.  The first two come from a paper published by Jeff Boyle [2].  Boyle makes (and proves) two claims about this distribution.

First, he claims that "the log distribution [Benford's Law] is the limiting distribution when random variables are repeatedly multiplied, divided, or raised to integer powers."  Second, he claims that once such a distribution is achieved, it "persists under all further multiplications, divisions and raising to integer powers."     

Since most data we accumulate (scientific, financial, gambling,...) is the result of many mathematical operations, we would expect that they would tend towards the logarithmic distribution as described by Boyle. 

Another reason for why natural data should fit Benford's Law is given by Roger Pinkham (in <a href="http://www.williams.edu/go/math/sjmiller/public_html/BrownClasses/197/benford/Pinkham_FirstDigit.pdf">this paper</a>).  Pinkham proves that<i> "</i>the only distribution for the first significant digits which is invariant under scale change of the underlying distribution" is Benford's Law.  This means that if we have some data, say the lengths of rivers in feet, it will have some distribution in the first digit.  If we require that this distribution remain the same under unit conversion (to meters, yards, cubits, ... ), the only distribution that satisfies this distribution would be the uniform logarithmic distribution of Benford's Law.

This "scale-invariant" rationale for this first digit law is probably the most important when it comes to data that we actually measure.  If we find some distribution for the first digit, we would like it to be the same no matter what units we have used.  But this should also be really easy to test.  The county size data used above was given in square miles, so let's try some new units.  First, we can try square kilometers.
<div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/_fa6AZDCsHnY/TR09Vq1jCAI/AAAAAAAAAIM/1Yz5gp0-7CY/s1600/benford_landkm.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="300" src="http://3.bp.blogspot.com/_fa6AZDCsHnY/TR09Vq1jCAI/AAAAAAAAAIM/1Yz5gp0-7CY/s400/benford_landkm.png" width="400" /></a></div>Slightly different than square miles, but still a very good fit.  Now how about square furlongs?
<div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/_fa6AZDCsHnY/TR093IwIt8I/AAAAAAAAAIQ/ern61I_MJQ0/s1600/benford_landfurlong.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" height="300" src="http://3.bp.blogspot.com/_fa6AZDCsHnY/TR093IwIt8I/AAAAAAAAAIQ/ern61I_MJQ0/s400/benford_landfurlong.png" width="400" /></a></div>Neat!  Seems like the distribution holds true regardless of the units we have used. 

So it seems like a wide range of data satisfy Benford's Law.  But is this useful in any way or is it just a statistical curiosity?  Well, it's mainly just a curiosity.  But people have found some pretty neat applications.  One field in which it has found use is <a href="http://en.wikipedia.org/wiki/Forensic_accounting">Forensic Accounting</a>, which I can only assume is a totally rad bunch of accountants that dramatically remove sunglasses as they go over tax returns.  Since certain types of financial data (for example, see <a href="http://www.uic.edu/classes/actg/actg593/Readings/Auditing/The-Effective-Use-Of-Benford's-Law-To-Assist-In-Detecting-Fraud-In-Accounting-Data.pdf">here</a>) should follow Benford's Law, inconsistencies in financial returns can be found if the data is faked or manipulated in any way. 

Moral of the story:  If you're going to cook the books, remember Benford!

[1]  Benford's Law, in the great tradition of <a href="http://en.wikipedia.org/wiki/Stigler's_law_of_eponymy">Stigler's Law,</a> was discovered by Simon Newcomb.

[2]  Paper can be found <a href="http://www.jstor.org/pss/2975136">here</a>.  Unfortunately, this is only a preview as the full version isn't publicly available without a library license.  The two points that I use from this paper are at least stated in this preview.
