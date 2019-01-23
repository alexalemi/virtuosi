<--
.. title: Zombpocalypse
.. date: 2010-07-01 23:48:00
.. tags: video, monte carlo, simulation, zombies
.. category: old
.. slug: zombpocalypse
.. author: Matt
-->


Here at the Virtuosi, we're concerned. We are concerned that perhaps the
world is really not ready for a zombie apocalypse. You know, the kind of
zombie apocalypse that you may have seen in such classics as "Night of
the Living Dead", "Shaun of the Dead", or perhaps the even more recent
"Zombieland" (sweet cameo by the way). The kind of zombpocalypse that
could leave major cities void of life and the country plagued with the
undead.
Well, Alemi and I were curious as to how likely such a pandemic was to
occur and what it would look like in the simplest of models. In typical
Virtuosi fashion, we threw some physics at it and this is what we came
up with.
**The Model**:
Taking cues from the epidemiologists, we feel that the spread of
zombie-ism might fall into a [compartmental
model](http://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology)
that is much like the heavily studied SIR model. Here, there are
susceptibles, S, that get infected, I, and can subsequently infect other
susceptibles or recover, R, and not play a part in the disease dynamics
anymore. Our analogous model is the SZR model in which there are
susceptibles, S, once again that can be bitten by a zombie to become
another zombie, Z. However, this is a huge difference - a susceptible
must then kill a zombie (by destroying the brain of cause) to make it
removed, R. Hence, we have the SZR disease model.
Like with the compartmental models, one can write down a set of
differential equations that govern the dynamics of disease in a
population. However, these might not be the best option for simulation
as the population is represented as a continuous variable. After all,
there can't be 1/100th of a zombie roaming around biting ankles causing
a new epidemic after all of this partners have been killed off. To get
around this, we set up a discrete contact network where each node is one
of the three states of the model and there are set probabilities of the
three states interacting when they are neighbors. In particular if there
is a susceptible with a zombie neighbor then there is a probability
**b** that the zombie will bite the susceptible turning the node into a
zombie. In the same time step, there is a probability **k** that the
susceptible will kill the zombie putting it in the removed class. Both
of these actions can happen in one time step of the simulation. However,
the two actions can't happen sequentially to the same node. That is, a
newly bitten susceptible must be a zombie for at least one time step
before it can be removed adding a latent period for the infection.
**Simulations:**
With these rules, we created networks with average connectivity k=8
(probably way too low) with up to N=40,000 susceptibles. Patient zero
was seeded at a random location and the simulation run until there were
no more susceptible - zombie neighbor pairs.
A typical simulation looks something like:
Here, the blue represent the susceptibles and red zombies. More subtly,
the removed are shown in black. You may also notice that the zombies
actually wrap around as they spread due to periodic boundary conditions.
And so we ran many of these simulations for various values of N, b, and
k to see what type of dynamics arise. As the ratio of b/k is increased
and zombies become proportionally better at biting susceptibles than
they are at killing the zombies, we see a transition from little to no
infection to mass pandemic in what appears to be a sort of percolation
transition.
[![image](http://2.bp.blogspot.com/_qY9DSyjj8Ro/TC1xAXdRNKI/AAAAAAAAB04/4_SC8vFPUF0/s320/cp.png)](http://2.bp.blogspot.com/_qY9DSyjj8Ro/TC1xAXdRNKI/AAAAAAAAB04/4_SC8vFPUF0/s1600/cp.png)
In the figure red is the fraction of zombies in the final population and
green is the amount of time that the simulation took to run. The spike
in time around the critical point shows critical slowing down as also
seen in the length of the movie above. Also, the ending configuration of
zombies shows a fractal like structure near the critical point. Using
the
[box-counting](http://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension)
method, we actually calculated the fractal dimension:
[![image](http://3.bp.blogspot.com/_qY9DSyjj8Ro/TC1zP2doE3I/AAAAAAAAB1I/Hfsl9e-TIaI/s320/fractal.png)](http://3.bp.blogspot.com/_qY9DSyjj8Ro/TC1zP2doE3I/AAAAAAAAB1I/Hfsl9e-TIaI/s1600/fractal.png)
This helps us pinpoint the epidemic transition at a ratio of b/k = 1.4.
This means for our particular network type and assumptions on the
infectious nature of zombie-ism that zombies must be 40% better at
biting than we are at lopping heads for an epidemic to take off. Even
then, there must be a much larger ratio of b/k for more than 50% of the
population to become part of the undead.
I trust that we the living would be at least as capable as the undead so
any potential zombie scenario would seem to be stifled in our model. But
then again, what about fast zombies? Now those things are scary.
**Update:**
I had a quick thought that mobile zombies might be a bit more realistic.
I made a quick movie where zombies pursue the closest susceptible while
the susceptibles run away from the zombies at the same speed. You will
see an area clear around the initial infection as the zombies give
chase. By accident, two zombies will collide providing the spark for an
epidemic. An explosion of zombies results. More to follow!
