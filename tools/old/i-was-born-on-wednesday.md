Title: I was born on Wednesday
Date: 2010-05-26 03:17:00
Tags: odds, fun, cards, probability, birthday, monty hall
Category: old
Slug: i-was-born-on-wednesday
Author: Alemi


Probability is a tricky thing.  There are a lot of nonsensical answers to be had.  I just read <a href="http://www.newscientist.com/article/dn18950-magic-numbers-a-meeting-of-mathemagical-tricksters.html?full=true">an article</a> about the recent <a href="http://www.g4g4.com/">Gathering for Gardner</a> meeting that took place.  Gathering for Gardner is a unique meeting for mathematicians, magicians and puzzle makers where they get together and talk about interesting things.  The meetings were inspired by <a href="http://en.wikipedia.org/wiki/Martin_Gardner">Martin Gardner</a>, one of the awesomest dudes of our time, who unfortunately just passed away.

The question put to the floor was the following:
<blockquote>"I have two children. One is a boy born on a Tuesday. What is the probability I have two boys?"</blockquote>
Think about that for a moment.  Not too hard though.  The answer turns out to be surprising.  Upon reading the question, I thought about it for a long time and managed to confused myself entirely.  Thinking I had gone crazy, I wrote a little python script to test the riddle, which only left me more convinced I had gone insane.  I've spent most of the night thinking about it, and after making it half way to crazy, I've come around and am momentarily convinced the puzzle makes perfect sense.  

I'm going to attempt to convince you it makes perfect sense, but I plan on doing it in steps so as to reduce the bewilderment.

<a name='more'></a>
<div class="separator" style="clear: both; text-align: center;"></div><div style="text-align: auto;">
</div><h3>Playing Cards</h3>
Forget the question.  Lets play a game of cards.  You shuffle a deck and deal me two cards:
<div style="text-align: center;"><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a></div>
I accidentally flip one of them over.
<div style="text-align: center;"><a href="http://2.bp.blogspot.com/_YOjDhtygcuA/S_zCuZ4KiQI/AAAAAAAAALA/cNa3n-rjuTg/s1600/23.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/_YOjDhtygcuA/S_zCuZ4KiQI/AAAAAAAAALA/cNa3n-rjuTg/s320/23.png" /></a><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a></div>
Whats the probability that my other card is red?

Well, that ones easy, its about half.

Sure, its not exactly a half, knowing that the deck is finite and that the draws are done without replacement, knowing that the card showing is a red one means that there are only 52/2 - 1= 26 -1 = 25 red cards out of a deck of 52-1 = 51 cards giving a probability of 49%.  But its basically a half.

Lets do over, deal me two cards:
<div style="text-align: center;"><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a></div>
Darn, I flipped one of them over again:

<div class="separator" style="clear: both; text-align: center;"><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a><a href="http://2.bp.blogspot.com/_YOjDhtygcuA/S_zDlNQLJyI/AAAAAAAAALI/WPBCX9i-Pk0/s1600/5.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/_YOjDhtygcuA/S_zDlNQLJyI/AAAAAAAAALI/WPBCX9i-Pk0/s320/5.png" /></a></div>
Whats the probability that my other card is red?  About a half still.* (*Sure, this time its really 26/51 = 51%).

Nothing mysterious going on.  

Do over again.  Deal me two cards:
<div style="text-align: center;"><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a><a href="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s1600/b2fv.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://3.bp.blogspot.com/_YOjDhtygcuA/S_zCNBPs3KI/AAAAAAAAAK4/WdtzaW_A6pk/s320/b2fv.png" /></a></div>
This time I'll ask a little trickier question.  Whats the probability that both my cards are red?  Ah, well its about 1/2 * 1/2 or about 1/4 = 25%.  (The real answer is 24.5%)

Alright smarty pants.  Whats the probability that I had a red card and a black one?  Well, that ought to be about 1/2 (Real answer 51%).

All in all, I could have a red card, then a black one (RB), or a black one, then a red one (BR), or a red one then a red one (RR) or a black one then a black one (BB).  4 distinct possibilities, each of which are equally likely, so the above two answers make complete sense.  There is only one way in four to get both red cards, but two ways out of four to have both a red and a black.

So far so good.


Lets ask a different question.  Now I'm going to get a bit obtuse.  You deal me two cards.  Now you ask me.
<blockquote>Hey Alemi, do you have a red card?</blockquote>
Meaning, do I have at least one red card.  I respond, "Yes."

Now, go with your gut.  You know I have at least one red card.  What do you reckon the color of the other one is?  

Probably black you say? You'd be correct.  Looking at our breakdown above, I could have gotten RR, RB, BR, or BB as my cards dealt.  Each was equally likely, but now you know something else.  You know that I have at least one red card, so we only have three possibilities left, I either have RR, RB, or BR.  Each of which was equally likely.  So whats the probability that my other card is black?  About 2/3 or 67%.  (Real answer: 67.5%)

Alright, same situation.  You deal me two cards, I reveal that I have at least one red one.  Whats the probability that my other card is red?  Well, obviously 1/3 or 33% (Actually 32.5%) since this is the opposite question to the one directly above, and follows from the same reasoning.

Fine.  No problems.  All of this makes sense.

<h3>Offspring</h3>
Instead of playing cards, lets return to offspring.  Lets first look at a classic probability riddle.

<blockquote>I have exactly two children.  At least one of them is a boy.  What is the probability that the other one is a boy?</blockquote>
If I were to give you this question straightaway, most people would have said the probability would be a 1/2.  Their reasoning being that boys and girls are equally likely.  But having just led you through the playing cards, hopefully now it makes some sense how the true answer to this question is 1/3 or 33%.  Originally my family could have been BB,BG,GB,or GG.  Each of which was equally likely.  Telling you I have at least one boy means now we are dealing with only the situations BB, BG or GB, still all equally likely, making the probability 1/3.

Fine.

Now, lets reexamine the true question at hand:
<blockquote>"I have two children. One is a boy born on a Tuesday. What is the probability I have two boys?"</blockquote>
Is it a half?  Is it 1/3?  What do you reckon?  At first thought, it seems like the Tuesday bit shouldn't enter into it at all, but on second thought, I've just revealed a lot more information than I did in the previous question.  I've told you something specific about one of my children.    This is analogous to when I accidently flipped over one of my cards, revealing not only its color but its count as well.  Hopefully it makes sense that the probability ought to be much closer to a half than to a third.  In fact the answer is 13/27 = 48.1%.  

With a little thought, you should be able to come up with that number yourself.  Otherwise, see <a href="http://www.newscientist.com/article/dn18950-magic-numbers-a-meeting-of-mathemagical-tricksters.html?full=true">the article</a> I mentioned at the beginning of this post.  They have a nice breakdown at the bottom.

Hopefully, at this point if you've read this far, you'd should be wondering why this question was so mysterious to begin with, and if thats the case, I did my job.  If you think the question is obvious, and think it would have been obvious even without the card analogy, try and ask the boy-born-on-a-tuesday question by itself to one of your friends.  I guarantee they'll be bewildered.  Its a fun problem, and one that illustrates just how strange and counterintuitive probability can be.

If you want some other mind twisting mathematical puzzles, try your hand at the <a href="http://en.wikipedia.org/wiki/Two_envelopes_problem">Two envelopes problem</a>, or <a href="http://en.wikipedia.org/wiki/Bertrand's_box_paradox">Bertrands' box paradox</a>, or <a href="http://en.wikipedia.org/wiki/Birthday_problem">the Birthday problem</a>, or everyone's favorite <a href="http://en.wikipedia.org/wiki/Monty_Hall_problem">the Monty Hall problem</a>.  <a href="http://thevirtuosi.blogspot.com/2010/04/some-of-best-advice-youll-ever-receive.html">Remember though</a>, try your hand at the problem before reading the answer.

Super fun bonus homework question:  Lets do cards again.  You deal me two cards, and I reveal that I have a red heart.  Whats the probability that my other card is red?
