# A problem with my wifi, and wide causal systems

We’ve been having problems with video calls. Sometimes the connection seems to
blink off, just for a fraction of a second, more than just a stutter. It’s
intermittent, and doesn’t happen often, but perhaps slightly more regularly
when there are multiple calls going on.

I found the solution by accident: tidying up some books, I noticed that the
power cable to one of the wifi routers was frayed. Not much, just enough the
expose the shielding near the plug. I swapped the cable. Our video calls have
been stable since.

I can only speculate. Maybe streaming video means that the router works harder
and needs more power. The increased power draw, with the damaged power cable,
created radio interference, so the router automatically amplified the wifi to
get through the noise – further increasing the power draw and therefore the
interference. Then: a cascade upwards until there’s no more power to get, and
the whole thing resets.

There’s a village in Wales that has had [intermittent broadband outages for 18
months](https://www.bbc.co.uk/news/uk-wales-54239180) (BBC News): "It turned
out that at 7am every morning the occupant would switch on their old TV which
would, in turn, knock out broadband for the entire village."

A SHINE event: "The TV was found to be emitting a single high-level impulse
noise (SHINE), which causes electrical interference in other devices."

I have no idea how I would have fixed my calls without

Some thoughts.

How many other people are living with this exact problem, but haven’t solved
it because either they haven’t run across the cause, or don’t have the domain
knowledge to recognise the frayed cable as the cause?

How many easily-solved problems am _I_ living with, because I don’t have the
knowledge to recognise a fixable cause in plain sight?

Can we call this a “wide” system? Video call stability is far removed from
electrical interference. I don’t know what words to use to talk about the
width of a causal system, but there are definitely “closer” potential causes.
(For example: having a old version of Chrome, or our street having
historically unreliable cable internet.)

So maybe it’s interesting to think about some phenomenon and its cause, and
the situations in which they can’t be linked: either because the system is
obscure _(I lack medical knowledge to recognise the cause of a physical
problem, say)_ or perhaps because the causal distance is too great for the
human mind to recognise it.

In a technological world, are causal distances increasing?

What could help?

I think of _House, M.D._

What would an artificial intelligence look like, specialised in technology and
in differential diagnosis, for finding problems in my wide systems?

Could I google _“what’s wrong with my video calls?”_ and get led through a
series of machine-learning-chosen questions to most efficiently subdivide and
traverse the causal graph until the actual fixable cause is found? _(What we
already know:[it’s not lupus](https://knowyourmeme.com/memes/its-not-lupus).)_

You would optimise for questions that were easy to answer. For example, asking
how to set the clock on my oven, I can easily tell you the make and how many
buttons it has but not the model. Though the first question that my
hypothetical _House, M.L._ would ask is _“is this the same oven you had 6
months ago?”_ which would lead to a solution instantly.

I’m reminded of the old 20 questions website [20Q](http://20q.net). It trained
a neural network by asking site visitors “what question would you ask”
whenever it failed to recognise a new animal, vegetable, or mineral. But
interacting with the A.I., especially [embedded in a handheld
device](http://berglondon.com/talks/botworld/?slide=40), is uncanny: it asks
questions and narrows down the domain in a thoroughly out-of-order and inhuman
way.

So train _House M.L._ by starting simple, and handing diagnosis over to a
human expert whenever boundaries are reached. Don’t worry about the efficiency
of the human, just that they find an answer. The machine learning system will
do efficient causal pathfinding later.

I wonder how many questions there are like this. 100,000? A million? Doable.
