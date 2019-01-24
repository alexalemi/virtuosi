<--
.. title: Calculator Pi
.. date: 2012-03-14 14:16:00
.. tags: 
.. category: old
.. slug: calculator-pi
.. author: Alemi
-->


There is a very fast converging algorithm for computing pi that you can
do on a desktop calculator.

-   Set x = 3
-   Now set x = x + sin(x)
-   Repeat

This converges ridiculously fast, after 1 step you get 4 digits right,
after 2 steps you get 11 correct, in general we find:

  ---------- --------------
  \# steps   Digits right
  1          4
  2          11
  3          33
  4          100
  5          301
  6          903
  7          2708
  8          8124
  ---------- --------------

of course on a pocket calculator, you only need to do 2 steps to have an
accuracy greater than the calculator can display. To make this chart I
had to trick a computer into doing high precision arithmetic, the code
is [here](https://gist.github.com/2038329). Granted, this approximation
is really cheating, since sin is a hard function to compute, and
basically being able to compute sin means you know what pi is already.
Really, this is just [Newton's
method](http://en.wikipedia.org/wiki/Newton's_method) for computing the
root of sin(x) in disguise
