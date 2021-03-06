Title: Visualizing Quantum Mechanics
Date: 2010-09-14 20:06:00
Tags: fun, feynman, quantum mechanics, solar system, movie, bouncing ball
Category: old
Slug: visualizing-quantum-mechanics
Author: Alemi


Or how I learned to stop worrying and love the computer. [Note: There's
a neat video below the fold. ]

### A Confession

I was recently rereading the [Feynman Lectures on
Physics](http://books.google.com/books?id=_6XvAAAAMAAJ&q=Feynman+lectures+on+physics&dq=Feynman+lectures+on+physics&hl=en&ei=6wmQTPzsDIG78gbAp_joDQ&sa=X&oi=book_result&ct=result&resnum=2&ved=0CDgQ6AEwAQ).
If you haven't read them lately, I highly recommend them. Feynman is
always a pleasure to read. As usual, I was surprised. This time the
surprise came in lecture 9, which the way the course was laid out meant
that this was something like the last lecture in the third week that
these students had ever received of university level physics. The
lecture is on Newton's laws of dynamics. The start is of course Newton's
~~first~~ (second) law, $$ F = \frac{d }{dt } (mv ) $$ which, provided
the mass is constant takes the more familiar form $$ F = ma $$ After
discussing the meaning of the equation and how in general it can give
you a set of equations to solve, he naturally uses an example to
illustrate the kinds of problems you can solve. What system does he
choose to use as the first illustration of a dynamical system? The Solar
System. That's right. Let that settle for a second. The sad thing is
that if you caught me off guard before I read the lecture, caught me in
an honest moment and asked me how you would solve the solar system, I
would probably have launched into a discussion of the [N-body
problem](http://en.wikipedia.org/wiki/N-body_problem) and how there is
no closed form solution to newtonian gravity that involves 3 or more
bodies. (Depending on who you are, I might have then mentioned the
[recent caveat](http://adsabs.harvard.edu/abs/1991CeMDA..50...73W),
namely that there is a closed form solution to the N-body problem, but
that it involves a very very very slowly convergent series). Now, how
can Feynman use the Solar System as his first example of solving
Newtonian dynamics and I have told you that it's impossible as my first
words on the subject? Well, the answer of course is that Feynman was
much smarter than I am. Perhaps another way to say it is that in a lot
of ways Feynman was a more contemporary physicist than I am.

### A Realization

Physics education has changed very little in the last 50 years or so.
Now in some ways this isn't a problem. The laws of nature also haven't
changed in the last 50 years. What's unfortunate is that the tools
available to physicists to answer their questions have changed
remarkably. Namely, computers. Computers are great. They permeate daily
life nowadays. They are capable of performing millions of computations
per second. This is great for physics. You see, a lot of the time, as
you all know, the way you achieve answers to specific questions about
the evolution of a system is to do a lot of computation. So what did
physicists do before computers? Well, a lot of time they would have to
do a lot of calculations out by hand, but no one enjoys that, so a lot
of times you would have to make sacrifices, make assumptions that meant
that your analytical investigations were simple enough to yield tiddy
little equations. This is reflected in the kinds of problems we still
solve in our physics classes. I never solved the solar system in my
mechanics class. I never did it because there isn't a closed form
analytical solution to the solar system. But you know what... that
doesn't matter. It doesn't matter in the least. Because while there
doesn't exist a closed form solution to the problem, it is very easy to
come up with a numerical approximation scheme (see [Euler
Method](http://en.wikipedia.org/wiki/Euler_method)). You see, the point
of physics is to get answers to questions. And the fact of the matter is
that those answers don't have to be 'exact', they don't have to be
perfect. They need to be good enough that we can't tell the difference
between them being 'exact' and them being an approximation. To do this
numerically with a pad of paper and a pencil is a heroic task. Do do
this with a computer takes a couple of lines of python code and a couple
seconds.

### An example

As an example of the neat things you can do with a few lines of python
code and a few minutes on your hand, check this out.
[and](http://www.youtube.com/watch?v=J4Wg_b8bVm8)
[there's](http://www.youtube.com/watch?v=idpQOJKOh6Y)
[more](http://www.youtube.com/watch?v=Z9121zwpbBs) This video depicts
time dependent quantum mechanics. I set up a gaussian wavepacket, inside
of a potential that includes a hard wall on the sides and is
proportional to x. That sounds fancy but what it means is that this is
the quantum mechanics equivalent of a bouncing ball. The amplitude of
the wave function corresponds to the probability of finding the particle
at any location. That is, imagine picking one of the colored pixels at
random. If you pick any of the colored pixels at random, and look down
at the x position, that is what measuring the position of the particle
would do. But what are the colors? Quantum mechanical wave functions are
complex. This means you can represent them either with a real and
imaginary part, or with a magnitude and a phase. Here it's the latter.
Like I said the amplitude is shown with the height (actually the
amplitude squared). The color corresponds to the phase, where the phase
is mapped to a location on the color wheel, just like the one that pops
up in Photoshop or GIMP. And theres sound too! The sound is what the
wave function would sound like if it was making noise. Its the real part
of the wave function played as a sound. To that end, in this video it is
very low frequency, because I made the movie slow enough to see the
colors changing well. Its fun to watch the video and listen to the
sound. For this movie the sound correlates nicely to when the 'ball'
reaches its maximum height. Whats also cool is that you can hear the
'ball' delocalize after each bounce. The sound and function start off
being nice and sharp, but after a few bounces it starts to spread out.
You can also see how momentum is encoded in quantum mechanics. Funny
thing is that instead of being something separate that you need to
specify like in classical mechanics, in quantum mechanics the wave
function is a complete description of the evolution of the system. I.e.
if I showed you just one frame of this bouncing ball, you would be able
to recreate the entire movie. If I showed you just one frame of a
classical basketball, you'd have no idea what frame came next since
you'd only know its position, not its velocity. In quantum mechanics the
momentum gets encoded in the wave function, and as you can tell its
encoded as a complex twist. A phase gradient. A crazy rainbow. If you
look closely, you can even see that you can tell the difference between
whether the particle is falling left or right. When it goes left the
rainbow pattern goes (reading left to right) blue red green. When its
moving right it goes blue green red. It twists one way then the other in
the complex plane. The colors are a little hard to see in this one,
they're a little easier to see in this one: This second one I dressed up
a bit, labelling the axes with units, putting a time counter,
superimposing the potential I was talking about, and marking the average
expected position with a tracer black dot on the bottom.

### A Call to Arms

Any student who has taken a first course in quantum mechanics knows
enough physics to make these movies. The physics isn't complicated. But
the movies really neat, right? More than neat. Making these videos
taught me things about quantum mechanics I should have learned a long
time ago. I really think computers are underestimated in physics
education. They can be a great tool. A picture is worth a thousand
words, so a movie must be worth millions*. *: denotes stolen quote
More than just as an illustrative tool, the fact that even students in
the first introductory mechanics physics course can solve for something
like the solar system shouldn't be hidden from them. Classical mechanics
after all is the physics of pretty much every object we can see and
touch, but classics mechanics classes only ever talk about [Atwood
machines](http://en.wikipedia.org/wiki/Atwood_machine) and frictionless
planes. Often the closest they come to realism is in discussing
projectile motion, where the laws you learn in the book (neglecting air
resistance) are very good at describing the trajectories of very dense
large objects (i.e. cannonballs). I can't remember the last time I've
fired a cannon. But air resistance serves little trouble to my computer.
Or [Rhett's](http://www.wired.com/wiredscience/tag/air-resistance/) (of
Dot Physics, which has just moved to Wired). Basically, if you give a
student an intro physics course and an intro programming course,
suddenly you have a human being who is better equipped to answer
questions about natural phenomenon than 99% of human beings that have
ever lived. So lets take a tip from Feynman and teach physics students
how to solve the solar system.

### Code

As per request, here is the python code I used to generate the videos.
Its rather messy, so I apologize in advance.
[schrod.py](https://docs.google.com/leaf?id=0B8Il0b2saix4NzYzMmRhZDUtODFhZS00YTE1LTgzZWYtMzVhODI5YzRhNWJm&hl=en&authkey=CPrk9IUM)
- A general script which finds the eigenvalues and eigenbasis for a 1D
particle with an arbitrary potential.
[qmsolver-bouncy.py](https://docs.google.com/leaf?id=0B8Il0b2saix4ZDYxZmFlNzQtYzdkNC00YTVkLWJhNWMtN2IxM2ZmZDg4Mzg4&hl=en&authkey=CJ3m4ogJ)
- Code to generate the movie. You need to create a directory with the
same name as the name in the script in the save folder as the script.
The last two lines make the sound and the directory full of images. I
used ffmpeg to wrap the two together.
