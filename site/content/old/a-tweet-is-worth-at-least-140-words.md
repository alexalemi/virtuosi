Title: A Tweet is Worth (at least) 140 Words
Date: 2011-08-30 23:49:00
Tags: entropy, information theory, python, twitter
Category: old
Slug: a-tweet-is-worth-at-least-140-words
Author: Alemi


[![image](http://2.bp.blogspot.com/-VJ3MBvt13Z4/Tl2Q7Z4J5WI/AAAAAAAAAWw/GG50fsyHvoo/s400/twittercompression.png)](http://2.bp.blogspot.com/-VJ3MBvt13Z4/Tl2Q7Z4J5WI/AAAAAAAAAWw/GG50fsyHvoo/s1600/twittercompression.png)

So, I recently read [An Introduction to Information Theory: Symbols,
Signals and
Noise](http://books.google.com/books?id=fXxde44_0zsC&printsec=frontcover&dq=An+Introduction+to+Information+Theory&hl=en&ei=7opdTrjhMMXrOarHmdIC&sa=X&oi=book_result&ct=result&resnum=1&ved=0CC0Q6AEwAA#v=onepage&q&f=false).
It is a very nice popular introduction to [Information
Theory](http://en.wikipedia.org/wiki/Information_Theory), a modern
scientific pursuit to quantify information started by [Claude
Shannon](http://en.wikipedia.org/wiki/Claude_Shannon) in 1948. This got
me thinking. Increasingly, people try to hold conversations on
[Twitter](http://twitter.com/), where posts are limited to 140
characters. Just how much information could you convey in 140
characters? After some coding and investigation, I created
[this](http://pages.physics.cornell.edu/~aalemi/twitter/), an
experimental twitter English compression algorithm capable of
compressing around 140 words into 140 characters. So, what's the story?
Warning: It's a bit of a story, the juicy bits are at the end. UPDATE:
Tomo in the comments below made [a chrome
extension](http://www.saigonist.com/b/twitter-decoder-ring) for the
algorithm

### Entropy

Ultimately, we need some way to assess how much information is contained
in a signal. What does it mean for a signal to contain information
anyway? Is 'this is a test of twitter compression.' more meaningful than
'歒堙丁顜善咮旮呂'? The first is understandable by any english speaker,
and requires 38 characters. You might think the second is meaningful to
a speaker of chinese, but I'm fairly certain it is gibberish, and takes
8 characters. But, the thing is if you put those 8 characters into [the
bottom form here](http://pages.physics.cornell.edu/~aalemi/twitter/),
you'll recover the first. So, in some sense to the messages are
equivalent. They contain the same amount of information. Shannon tried
to quantify how we could estimate just how much information any message
contains. Of course it would be very hard to try to track down every
intelligent being in the universe and ask them if any particular message
had any meaning to them. Instead, Shannon reserved himself to trying to
quantify how much information was contained in a message produced by a
random source. In this regard, the question of how much information a
message contains becomes a more tractable question: How unlike is a
particular message from all other messages produced by the same random
source? This question might sound a little familiar. It is similar to a
question that comes up a lot in [Statistical
Physics](http://en.wikipedia.org/wiki/Statistical_physics), where we are
interested in just how unlike a particular configuration of a system is
from all possible configurations of a system. In Statistical physics,
the quantity that helps us answer questions like this is the
[Entropy](http://en.wikipedia.org/wiki/Entropy), where the entropy is
defined as $$ S = -\sum_i p_i \log p_i $$ where p_i stands for the
probability of a particular configuration, and we are supposed to sum
over all possible configurations of the system. Similarly, for our
random message source, we can define the entropy in exactly the same
way, but for convenience, let's replace the logarithm with the logarithm
base 2. $$ S = -\sum_i p_i \log_2 p_i $$ At this point, the
[Shannon Entropy, or Information
Entropy](http://en.wikipedia.org/wiki/Shannon_entropy) takes on a real
quantitative meaning. It reflects how many bits of information the
message source produces per character. The result of all of this aligns
quite well with intuition. If we have a source that outputs two symbols
0 or 1 randomly, each with probability 1/2. The shannon entropy comes
out to be 1, meaning each of the symbols of our source is worth one bit,
which we already new. If instead of two symbols, our source can output
16 symbols, 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F say, the shannon entropy
comes out to be 4 bits per symbol, which again we should have suspected
since with four bits we can count up to the number 16 in [base
2](http://en.wikipedia.org/wiki/Binary_numeral_system) (e.g. 0000 - 0,
0001 - 1, 0010 - 2 , etc ). Where it begins to get interesting is when
all of our symbols don't occur with equal probability. To get a sense of
this situation, I'll show 5 example outputs:

    '000001000100000000010000010000'

    '000000000010000000000001000000'

    '010100000000000000000000111000'

    '010100000000000000000000111000'

    '000000000100000000110000000010'

looking at these examples, it begins to become clear that since we have
a lot more zeros than ones, each of these messages contain less
information than the case when 0 and 1 occur with equal probability. In
fact, in this case, if 0 occurs 90% of the time, and 1 occurs 10% of the
time, the shannon entropy comes out to be 0.47. Meaning each symbol is
worth just less than half a bit. We should expect our messages in this
case to have to be about twice as long to encode the same amount of
information. In an extreme example, imagine you were trying to transmit
a message to someone in binary, but for some reason, your device had a
sticky 0 key so that every time you pushed 0, it transmitted 0 10 times
in a row. It should be clear in this case that as far as the receiver is
concerned, this is not a very efficient transmission scheme.

### English

What does this have to do with anything? Well, all of that and I really
only wanted to build up a fact you already know. The fact is, the
English language is not very efficient on a per symbol basis. For
example, I'm sure everyone knows exactly what word will come at the end
of this _______. There you go, I was able to express exactly the
same thought with at least 8 fewer characters. n fct, w cn d _ lt bttr
[in fact, we can do a lot better], using 22 characters to express a
thought that normally takes 31 characters. In fact, Shannon has a [nice
paper](http://languagelog.ldc.upenn.edu/myl/Shannon1950.pdf) where he
attempted to measure the entropy of the english language itself. Using
more sophisticated methods, he concludes that english has an information
entropy of between 0.6 and 1.3 bits per character, let's call it 1 bit
per character. Whereas, if each of the 27 symbols (26 letters + space)
we commonly use each showed up equally frequently, we would have 4.75
bits per character possible. Of course, from a practical communication
standpoint, having redundancies in human language can be a useful thing,
as it allows us to still understand one another even over noisy phone
lines and with very bad handwriting. But, with modern computers and
faithful transmission of information, we really ought to be able to do
better.

### Twitter

This brings me back to [twitter](http://twitter.com/). If you are
unaware, twitter allows users to post short, 140 character messages for
the rest of the world to enjoy. 140 characters is not a lot to go on.
Assuming 4.5 characters per word, this means that in traditionally
written english you're lucky to fit 25 words in a standard tweet. But,
we know now that we can do better. In fact, if we could come up with
some kind of crazy scheme to compress english in such a way as to use
each of the 27 usual characters so that each of those characters
appeared with roughly equal probability, we've seen that we could get
4.75 bits per character, with 140 characters and 5.5 symbols per word,
this would allow us to fit not 25 words in a tweet but 120 words. A
factor of 4.8 improvement. Of course we would have to discover this
miraculous encryption transformation. Which to my knowledge remains
undiscovered. But, we can do better. It turns out that twitter allows
you to use [Unicode](http://en.wikipedia.org/wiki/Unicode) characters in
your tweets. Beyond enabling you to talk about Lagrangians (ℒ) and play
cards (♣), it enables international communication, by including foreign
alphabets. So, in fact we don't need to limit ourselves to the 27
commonly used English symbols. We could use a much larger alphabet,
Chinese say. I choose Chinese because there are over 20,900 Chinese
alphabet symbols in Unicode. Using all of these characters, we could
theoretically encode 14.3 bits of information per character, with 140
characters, and 1 bit per English character, and 5.5 symbols per English
word, we could theoretically fit over 365 English words in a single
tweet. But alas, we would have to discover some magical encoding
algorithm that could map typed English to the Chinese alphabet such that
each of the Chinese symbols occurred with equal probability. I wasn't
able to do that well, but I did make an attempt.

### My Attempt

So, I tried to compress the English language, an design an effective
mapping from written English to the Chinese character set of Unicode. We
know that we aim to have each of these Chinese characters occur with
equal probability, so my algorithm was quite simple. Let's just look at
a bunch of English and see which pair of characters occur with the
highest probability, and map these to the first Chinese character in the
Unicode set. Replace their occurring in the text, rinse, and repeat.
This technique is guaranteed to reduce the probability at which the most
common character occurs at every step, by taking some if its occurrences
and replacing them, so it at least aims to achieve our ultimate goal.
That's it. Of course, I tried to bootstrap the algorithm a little bit by
first mapping the most common 1500 words to their own symbols. For
example, consider the first stanza of the [Raven by Edger Allen
Poe](http://en.wikipedia.org/wiki/The_raven)

    Once upon a midnight dreary, while I pondered, weak and weary,

    Over many a quaint and curious volume of forgotten lore--

    While I nodded, nearly napping, suddenly there came a tapping,

    As of some one gently rapping, rapping at my chamber door.

    "'Tis some visiter," I muttered, "tapping at my chamber door--

                         Only this and nothing more."

The most common character is ' ' (the space). The most common pair is 'e
' (e followed by space), so let's replace 'e ' with the first Chinese
Unicode character '一' we obtain:

    Onc一upon a midnight dreary, whil一I pondered, weak and weary,

    Over many a quaint and curious volum一of forgotten lore--

    Whil一I nodded, nearly napping, suddenly ther一cam一a tapping,

    As of som一on一gently rapping, rapping at my chamber door.

    "'Tis som一visiter," I muttered, "tapping at my chamber door--

                         Only this and nothing more.'

So we've reduced the number of spaces a bit. Doing one more step, now
the most common pair of characters is 'in', which we replace by '丁'
obtaining:

    Onc一upon a midnight dreary, whil一I pondered, weak and weary,

    Over many a qua丁t and curious volum一of forgotten lore--

    Whil一I nodded, nearly napp丁g, suddenly ther一cam一a tapp丁g,

    As of som一on一gently rapp丁g, rapp丁g at my chamber door.

    "'Tis som一visiter," I muttered, "tapp丁g at my chamber door--

                         Only this and noth丁g more.'

etc. The end results of the effort are [demo-ed
here](http://pages.physics.cornell.edu/~aalemi/twitter/). Feel free to
play around with it. For the most part, typing some standard English, I
seem to be able to get compression ratios around 5 or so. Let me know
how it does for you. I'll leave you with this final message:

    儌咹乺悃巄格丌凣亥乄叜

Python code that I used to do the heavy lifting is available as [a
gist](https://gist.github.com/1182747).
