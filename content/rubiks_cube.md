# Solving the Rubik’s Cube and other hard-to-recognise problems

A Rubik’s Cube can be solved, from any position, in 20 moves or fewer.

This “worst case” number for the Cube - i.e. the shortest path to solve the
hardest position - is called _God’s Number._ It’s hard to figure out the
hardest position because you have to look at every single configuration (there
are 43,252,003,274,489,856,000) and then, to compare, calculate the shortest
solution for each.

In 1981, mathematicians proved that God’s Number couldn’t be more than 52. By
2008, this was down to 22.

Finally, in 2010, there were just 19,508,428,800 different positions left to
check, in order to prove God’s Number once and for all. Instead of doing it
with equations and theory, it could be brute forced – the solution for _every
one_ of those positions calculated on a computer. BUT this calculation,
running on a good desktop PC, would take **35 years.**

So they worked with Google, who took the calculation away and "complete[d] the
computation in just a few weeks."

Full story (and paper) here: [God’s Number is 20](https://www.cube20.org).

What I’m most impressed by: the realisation that the time for being clever is
over, and it’s possible to throw supercomputers at the problem. Like, that’s
not an easy realisation. 3 years earlier is two Moore’s Law doublings. Running
the calculation in 2007 would have taken, say, 6 months and not “a few weeks”,
and that’s longer but still a darn sight quicker than 35 years: tolerable. So
we can say that the realisation that the problem was solvable, from the moment
that it _was_ solvable, took at least 3 years.

ASIDE: A few years ago, I dropped a note to the mathematicians to ask about
one point, and they were kind enough to reply.

I wanted to know whether the state space of the Rubik’s Cube was 20 moves
“across” – or perhaps was it 40? That would be the case if Distance-20-state-A
was 20 moves from the solved state, and Distance-20-state-B was also 20 moves
from the solved state, but there was otherwise no route between A and B. My
intuition said that, from symmetry, there wasn’t anything special about the
solved state to make the centre, so it should be the former… but I don’t know
any group theory, so I had to ask.

The reply: "our result implies that any state is at most 20 moves from any
other state."

So now you know too.

This feels related to [AI overhangs](/home/2020/08/24/ai_overhang), "when you
have had the ability to build transformative AI for quite some time, but you
haven’t because no-one’s realised it’s possible" – and then artificial
intelligences get 100-1,000x more competent in a matter of months. The blocker
is the realisation.

I wonder how many problems are hidden from us because we unconsciously dismiss
them as 35 year problems.

And I wonder how many of those 35 year problems are actually “a few weeks”
problems, if you have enough compute.

In psychology and design, there’s the concept of the **affordance.** When you
look at a mug, you also see that it “affords” being picked up, because you see
that it has a handle, and that the handle is the right shape for your hand,
and so on. Affordances have an existence in the brain: seeing the handle
primes your hand to get ready to grip it. And a mug that didn’t afford being
picked up wouldn’t even be a mug.

So what I’m saying is that maybe there is a class of problems which lack the
solvability affordance. Because we don’t see them as solvable, we don’t even
recognise them as problems.

Can we methodically find and recognise problems like this, without having to
wait to stumble across them? Maybe we could start by identifying knotty areas
currently solved heuristically, then checking to see whether we can remove the
need for heuristics.

For example, markets are a heuristic method. We “solve” the problem of house
prices, and wages for software engineers, and the price of coffee, etc, with
markets. What if we don’t need markets anymore, and all of these scenarios can
be solved for fairness and efficiency – computationally?

And so on.
