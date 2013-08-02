Title: Calculator Pi
Date: 2012-03-14 14:16:00
Tags: 
Category: old
Slug: calculator-pi
Author: Alemi


There is a very fast converging algorithm for computing pi that you can do on a desktop calculator.
<ul><li>Set x = 3</li><li>Now set x = x + sin(x)</li><li>Repeat</li></ul><div>This converges ridiculously fast, after 1 step you get 4 digits right, after 2 steps you get 11 correct, in general we find:

<a name='more'></a>
</div><div>
<center><table border="0"><tbody><tr><td># steps </td><td>Digits right </td></tr><tr><td>1 </td><td>4 </td></tr><tr><td>2 </td><td>11 </td></tr><tr><td>3 </td><td>33 </td></tr><tr><td>4 </td><td>100 </td></tr><tr><td>5 </td><td>301 </td></tr><tr><td>6 </td><td>903  </td></tr><tr><td>7 </td><td>2708 </td></tr><tr><td>8 </td><td>8124</td></tr></tbody></table></center>

of course on a pocket calculator, you only need to do 2 steps to have an accuracy greater than the calculator can display.  To make this chart I had to trick a computer into doing high precision arithmetic, the code is <a href="https://gist.github.com/2038329">here</a>.

Granted, this approximation is really cheating, since sin is a hard function to compute, and basically being able to compute sin means you know what pi is already.  Really, this is just <a href="http://en.wikipedia.org/wiki/Newton's_method">Newton's method</a> for computing the root of sin(x) in disguise</div>
