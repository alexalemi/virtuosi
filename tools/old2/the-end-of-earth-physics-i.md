Title: The End of Earth Physics I
Date: 2010-04-17 16:25:00
Tags: scott bakula, end of the earth
Category: old
Slug: the-end-of-earth-physics-i
Author: Corky


I was reading the Wikipedia page for the Hitchhiker's Guide books the
other day and found that it started as a series of radio shows called
"The Ends of Earth." At the end of each episode, the Earth would be
destroyed. Since I feel like this is the best way to end any TV
show/movie/book/news broadcast/Mayan calendar, I will shamelessly steal
the idea.
Since this is the first End of the Earth post, we will start small and
just consider the boiling off of all the world's oceans. To be precise,
we will consider how much energy it would take to turn all the world's
water at 0 degrees Celsius to water vapor at 100 degrees Celsius.
First we need to estimate the mass of all the water on earth. I will
make the assumptions that all water is fresh water and that the oceans
account for all water on earth. These are obviously not exactly true,
but will give the proper order of magnitude. The volume of a spherical
shell is given by
$$ \\text{V} = 4 \\pi R\^{2} \\Delta R $$
Taking the radius of the earth to be 6000 km, the ocean depth to be 1
km, and the fraction of earth covered by water to be 7/10 , we see that
$$ V\_\\text{water} = 4 \\pi {R\_{\\text{earth}}\^{2} \\times
\\text{height} \\times \\text{fraction}$$
$$ V\_\\text{water} = 4 \\pi (6 \\times 10\^{6} \\text{m})\^{2} \\times
10\^{3} \\text{m} \\times (\\frac{7}{10}) = 3 \\times 10\^{17}
\\text{m}\^{3}$$
Now we have the volume of the ocean. Now, since
$$ \\text{Density} = \\frac{Mass}{Volume}$$
we can calculate the mass of the oceans using the density of water to be
1000 kg / m\^3.
$$ \\text{Mass} = (\\rho\_\\text{water})(V\_\\text{water}) = (1000
\\frac{\\text{kg}}{\\text{m}\^{3}})(3 \\times 10\^{17} \\text{m}\^{3}) =
3 \\times 10\^{20} \\text{kg}$$
FUN FACT: The mass of all the water on earth is about 2% the mass of
that celestial punching bag known as Pluto.
Alright, now that we have the mass of the earth, we can start
calculating how much energy it would take to heat it up and boil it
away. The amount of heat Q required to raise the temperature of a given
material is
$$ Q\_\\text{heat} = \\text{mc}\\Delta\\text{T} $$
where m is the mass of the thing we are heating, c is the specific heat
( the amount of energy required to heat our material up 1 degree
Celcius) and delta T is our change in temperature. This equation only
holds when there are no phase transitions, so we can use it to calculate
how much energy is needed to heat up the oceans from 0 degrees to 100
degrees:
$$ Q\_\\text{heat} = (3 \\times 10\^{20} \\text{kg}) \\times (4000
\\frac{\\text{J}}{\\text{kg C}}) \\times (100 \\text{deg C}) = 10\^{26}
\\text{J} $$
where we have used the fact that the specific heat of water is about
4000 J/kg deg C.
So now we know how much energy it takes to bring water to its boiling
point, but this is not the same as boiling it off. To find that, we need
to calculate how much energy we have to add to liquid water at a
constant 100 degrees to turn it into water vapor. This is given by
$$ Q\_{\\text{boil}} = \\text{mL} $$
where m is the mass again and L is the "latent heat of vaporization." It
tells us how much energy we need to add to turn a kilogram of liquid
water at 100 degrees to a kilogram of water vapor at 100 degrees. For
water, L is about 2\*10\^6 J/kg, so
$$ Q\_{\\text{boil}} = ( 3 \\times 10\^{20} \\text{kg} ) \\times (2
\\times 10\^{6} \\frac{\\text{J}}{\\text{kg}}) = 6 \\times 10\^{26}
\\text{J} $$
Comparing this to the energy calculated before, we see that amount of
energy needed to vaporize water at 100 degrees is about six times larger
than the amount of energy needed to heat up the water by 100 degrees!
Now we can calculate the total amount of energy to boil way the oceans:
$$ Q\_{\\text{total}} = Q\_{\\text{heat}} + Q\_{\\text{boil}} = 7
\\times 10\^{26} \\text{J} $$
So how much energy is that really? Well the total power of the sun is
$$ L\_{\\text{sun}} = 4 \\times 10\^{26} \\frac{\\text{J}}{\\text{s}} $$
Thus, it would take the entire energy output of the sun for about 2
seconds to boil away all the earth's oceans.
Now thats a lot of energy. To put this into the conventional unit of
destruction, this is equivalent to 10\^11 Megatons of TNT. Typical
hydrogen bombs are 10 Megatons. So if you want to boil away the oceans
with H-bombs, you'd need about ten billion hydrogen bombs.
Luckily, short of constructing a reflecting Dyson sphere with a hole
that directs all the sun's radiation at the earth, these energies are
unobtainable. So don't panic.
