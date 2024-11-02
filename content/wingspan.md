# Playing board games, thinking about Excel: Wingspan Edition

I’ve been playing pandemic-breakout-hit board game _Wingspan_ recently.

I kinda sorta wanna to see this gorgeous and hand-drawn ecology-fostering
approach baked into financial modeling software, such as Microsoft Excel.

Your job in _Wingspan_ to populate your wildlife refuge with birds (each a
beautifully illustrated playing card). Birds cost food and an increasing
number of eggs. You can gather food and lay eggs, the quantities of which are
dependent on your population of birds.

Wingspan is what’s known among serious gamers as an “engine-building game,”
which means that as the game goes on, the combination of birds you play
becomes more and more efficient at generating points each turn, like an engine
running faster and faster. Your cuckoo lays eggs, and the eggs not only give
you points but make it possible to play more birds, which also give you more
points but have their own powers that generate points in other ways.

An **engine builder.** As opposed to “roll-and-move” and other mechanics.

And: "Activating the cascading effects of these healthy interconnections is
the greatest pleasure of playing Wingspan."

The precise goals vary each game, for added fun, and there are a _ton_ of
birds, which all bring something different to the table. Like: bird such-and-
such wins you 7 points and costs 3 of these particular foods and can fit 4
eggs in its nest and has a special power in that it encourages other birds to
lay extra eggs too under whatever particular conditions.

Getting this right is why the game works, and it was hard work: "It’s those
interconnections that [Elizabeth] Hargrave began mapping out in a ginormous
spreadsheet once she decided she really did want to design a board game."

([Here are some good Wingspan strategies.](https://catsanddice.com/wingspan-
strategy-tips-guide/))

What I don’t enjoy about _Wingspan_ is that there are a ton of rules.

The cards and tokens (food, eggs) are merely indexes into the real game board,
which exists only virtually, in rulespace.

Hargrave’s fearsome Excel spreadsheet is ever-present, hidden behind the
curtain.

Compare with say Chess or Go. There are rules, sure, but they are relatively
minimal. The state of the game is told more by the physicality of the pieces
on the table.

_(Game theorists must have mathematics to describe this different. I would
like to know!)_

So I would like to play another version of _Wingspan_ in which the rules are
somehow implicit in the physical geography of the pieces, instead of being
written down on the cards and in the rulebook. I don’t know what that would
look like.

You get a sense of acceleration in playing an engine builder!

Here’s a great article from a game design perspective – how to harness the
acceleration… but also how to slow it down: [Engine Building
(2019)](http://makethemplay.com/index.php/2019/06/10/engine-building/) on
_Make Them Play: Learning About Board Game Design._

e.g.:

The challenge is much more in balancing your engine. One major problem with an
engine is that it can “run away”: If you can turn resources into _more_
resources then whomever has a minor head start can quickly leave all other
players behind without hopes of catching up.

It’s a very 21st century genre, right?

For example: building a startup is never about building the product. It’s
about building a machine that knows how to ship product and how to sell it and
how to use feedback to iterate it. And that knows how to grow itself as an
organisation.

Like, consider the Business Model Canvas ([as previously
discussed](/home/2021/08/18/frameworks)) – as a way of describing a startup on
a single sheet of paper, it’s practically already a circuit diagram.

Also think about community development: how do you build a community which
goes out and attract more community.

An engine that simply accelerates is entertaining to experience, but the joy
is in the meta design – how do you create conditions such that player builds
engines that _don’t_ blow up?

How do you create a startup or a community which grows in depth and
complexifies, but doesn’t churn out or ossify? Wiring up the feedback loops,
balancing the world. How do you make an ecology which expands when appropriate
and renews yet remains heterogeneous and manageable?

And ecosystems truly are a 21st century preoccupation. With the climate crisis
and its runaway feedback loops, and pandemics with their exponentials, and
social media with its virality, this isn’t like the old days of the industrial
revolution where the plumbing was steam and electricity – relatively
manageable stock and flow. No, we’re trying to manage circuits and networks of
lashed-together exponentials; unstable equilibria all round, if you get it
wrong then systems explode or die before you blink. Tread either carefully or
really, really fast.

Hobbies in this _Wingspan_ world are things like bonsai and terrariums – games
of [ecopoiesis](http://www.users.globalnet.co.uk/~mfogg/haynes.htm): "a new
word which means ‘the making of an abode for life’," said biologist Robert
Haynes in 1993.

I wondered before about [giving out bonsai trees at business
school](/home/2021/03/26/poker) to see what mindset they impart – and I’m
wondering more directly now: what is Microsoft Office but designed on
terrarium principles? What would it be like to work in _Excel: Wingspan
Edition?_

I’ve been looking at liquid computing recently, specifically the MONIAC
(Monetary National Income Analogue Computer) a.k.a. the Phillips Hydraulic
Computer a.k.a. the Financephalograph, invented by Bill Phillips in 1949.
They’ve got one in the London Science Museum:

The MONIAC is a model of the British economy built as a two-meter tall machine
with a water tank at the top and equations modeled "using pipes, valves, tanks
and pumps."

Bill Phillips used water to represent money as it flowed around the economic
system. Valves could be opened or closed to represent variable effects, such
as the rate of interest on savings or investment.

Graphical curves, describing things such as the way interest rates varied over
time, could be cut into plastic sheets and physically ‘read’ by the machine as
it operated.

(There’s a great video at that link too.)

As a liquid computer, it was an empirical way to solve the equations to arrive
at something balanced, i.e. where you don’t end up with an empty or
overflowing treasury tank.

And so: "When a set of parameters resulted in a viable economy the model would
stabilise and the results could be read from scales." _([From
Wikipedia.](https://en.wikipedia.org/wiki/MONIAC))_

ALL OF WHICH MAKES ME ASK:

Isn’t the lesson of MONIAC that it is interesting to build financial models
that are seeking balance (or at least, are evolving slowly enough that they
can be managed) not necessarily ones that are trying to go perpetually up and
to the right?

What would it means to have a version of Excel that was always iterating in
the background, always running the engine, giving you a readout of whether
your model would blow up over time, or whether you were tuning it towards
balance?

So, imagining this: every sheet would automatically come with an infinite
stack of sheets of how it evolves over time. Every non-formula cell would
default go to zero unless you declared an external conduit, a value which
would be added or subtracted per tick of the clock. Constant numbers would be
banned: everything has to come from somewhere.

A special function would colour-code a cell according to whether it diverged
to infinity, converged to zero, or remained stable over time.

You get to write only onto the `t=0` initial conditions top sheet.

Elizabeth Hargrave repurposed Excel to design an engine-builder that doesn’t
lead to runaway inequality between players and doesn’t rapaciously consume the
game board, yet leads to collaboration and complexity over time. What if we
built the ideal version of Excel for _her,_ and gave _that_ to MBAs to build
their companies?
