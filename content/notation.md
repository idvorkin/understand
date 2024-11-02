# Collecting my thoughts about notation and user interfaces

I’m circling something to do with **notation** and **software user
interfaces** and what connects them. And things aren’t quite cohering for me
yet, so this is me just collecting my thoughts…

_(I’m designing user-composable interfaces this week, so long term the goal is
to figure out some principles.)_

A good starting point is _pirate maps,_ those sketched maps with minimal
detail that can none-the-less lead you to the X that marks the spot on the
right treasure island.

Or to be more specific, urbanist Kevin Lynch’s city maps from his 1960 book
_The Image of the City._ [I’ve described his approach here (March 2021)](/home/2021/03/31/maps) _(where I also pick at the possible neurological
underpinnings)_ so to briefly summarise:

Lynch puts forward five primitive elements: paths (e.g. streets); edges (e.g.
uncrossable rivers); districts; nodes (e.g. street corners); landmarks (e.g. a
recognisable building). Each element has an intuitive way to sketch it, as if
on the back of a napkin.

The map of Boston (his first example) is immediately recognisable. Ask a
person to sketch a city, or a route to a place, and they’ll automatically use
something very like Lynch’s system.

So Lynch’s five primitives comprise a **notation.**

It’s **composable.** A small number of simple elements can be combined,
according to their own grammar, for more complex descriptions. There’s no cap
on complexity; this isn’t paint by numbers. The city map can be infinitely
large.

Compositions are **shareable.** And what’s more, they’re **degradable:** a
partial map still functions as a map; one re-drawn from memory on a whiteboard
still carries the gist. So shareable, and pragmatically shareable.

Not only are maps in this notation functional for communication, but it’s
possible to look at a sketched city map and deconstruct it into its primitive
elements (without knowing Lynch’s system) and see how to use those elements to
extend or correct the map, or create a whole new one. So the notation is
**learnable.**

The idea of composability is worth digging into.

A pirate map is a drawing, and drawings are compositions of dots and lines and
textures: "A drawing is simply a line going for a walk" ([Paul
Klee](https://www.paulklee.net/paul-klee-quotes.jsp)). But these would be poor
primitives. Why?

A good, composable notation has primitives which are **semantic.** A line
doesn’t mean anything, it’s too abstract – but a _path_ or an _edge_ (in
Lynch’s system) refer to qualities of things in the real world. I’m also going
to say that a notation must be **grammatical,** which is to say that there are
rules about how primitives can be combined.

There are also _not too many_ primitives. You want a system which is
**efficiently expressive.** Like, you can say complex things with the minimum
of vocabulary. Why? Because then the person using the notation can hold it in
their head.

Adam Wiggins is the co-founder of Heroku, the prescient cloud-based technology
platforms. It was ahead of its time, incredibly simple to use, but powerful –
with an almost toy-like interface _(I say that as a compliment)_ the
complexity of hosting, scaling and managing servers was almost completely
hidden.

Here is Wiggins relating his philosophy:

_The value of a product is the number of problems it can solve divided by the
amount of complexity the user needs to keep in their head to use it._ Consider
an iPhone vs a standard TV remote: an iPhone touchscreen can be used for
countless different functions, but there’s very little to remember about how
it works (tap, drag, swipe, pinch). With a TV remote you have to remember what
every button does; the more things you can use the remote for, the more
buttons it has. We want to create iPhones, not TV remotes.

_(Via Simon Willison[who picked out this
quote](https://simonwillison.net/2020/Dec/3/adam-wiggins-heroku-values/).)_

It matters what you can hold in your head because then the notation becomes a
tool for the imagination. It is **suggestive.** Lego is suggestive. If you sit
down and compose with the bricks, aimlessly, you will come up with _new ideas_
that you wouldn’t have reached otherwise. The studs on the bricks are a
grammar; the shapes are the semantics. You don’t get lost in complexity
because the bricks are right there on the floor, so you play and, o ho!,
there’s a novel kind of house you can build, you hadn’t thought of that.

At this point I’m slip-sliding between notation and interface, and this is
maybe one of the things I’m trying to figure out. Perhaps a notation is
_always_ an interface to _something?_

Think of Feynman diagrams from physics. These are diagrams of particle
interactions, like an electron hits a positron and both disappear while
emitting a photon. [The Wikipedia page shows
examples.](https://en.wikipedia.org/wiki/Feynman_diagram)

But the lines, arrows, and squiggles have a grammar to them. And Feynman
diagrams directly map to the fearsomely complex mathematics of quantum field
theory. Manipulating the diagram _is the same as_ performing the calculations.

So Feynman diagrams, as a notation, exist on the boundary of two realms; the
interface between the scientific model (a representation of physical reality)
and the imagination of the physicist.

Software user interfaces: let me try to draw the parallel.

I’ve been reading Steven Sinofsky’s first-person account of the rise of the
Microsoft and the PC, which is astounding – it’s technology and strategy and
history from someone who was right in the thick of it, at a pivotal time.
Sinofsky is serialising the whole story as [Hardcore
Software](https://hardcoresoftware.learningbyshipping.com/about): _Inside the
Rise and Fall of the PC Revolution._

He has this to say about the complexity of Microsoft Office (the first and
much successful office software suite), and specifically about the "buttons,
menus, and commands," and "every icon, command name, tooltip, menu string, and
keyboard accelerator"…

One of the most significant differences between Office and most other tools is
the sheer breadth and simultaneous depth of features, something that would
become even more apparent as web pages came to the forefront. Each application
had over 1000 commands (buttons, menus, etc.) with something over 2500 unique
commands in Office96.

That was 25 years ago. I can only imagine that complexity has increased since.

Compare with the Xerox Star (1981) which introduced the desktop interface in
the first place, together with the underlying metaphor of _objects._ Like, you
could select a file or a paragraph or a printer and choose what do to with it,
and that’s the ancestral idea behind our graphical user interfaces today.

One way to simplify a computer system is to reduce the number of commands.
Star achieves simplicity without sacrificing functionality by having a small
set of generic commands apply to all types of data: Move, Copy, Open, Delete,
Show Properties, and Same (Copy Properties). Dedicated function keys on Star’s
keyboard invoke these commands.

As an example of this flexibility:

In Star, users simply Copy to a printer icon whatever they want to print.
Similarly, the Move command is used to invoke Send Mail by moving a document
to the out-basket.

…which is powerful! But only works because the user can see, on the desktop,
the icon of a printer and the icon of an out-basket.

I’m stretching the definition of _“notation”_ now, but let’s say that both
Xerox Star and Microsoft Office present the user with a notation to their
internals, made out of commands and also graphical components: windows, icons,
menus, pointers.

There’s a quality to this “notation” which is suggestive, as with Lego bricks,
in that you can experiment with trying different commands.

But I’ll go further as say that there’s a quality which is that the notation
is **intentional** and that is essential to a good notation or a good
interface.

That is, you can imagine a goal (being it printing your document or drawing a
map of Boston), and you know the available primitives, and you can figure out
a sequence or a composition to get from A to B.

Related to all of these points, a notation or an interface must be
**legible.**

It’s no good with a desktop interface, say, if icons are draggable and buttons
are clickable, but the user doesn’t _know_ that these operations are possible.
So we design icons and buttons with _visual affordances:_ they _look_ as if
they are pick-up-able, press-able, and so on.

Legibility, consistency, and affordances: all of these contribute to creating
a _mental model_ of the notation system in the mind of the user, and that
seems like a prerequisite for many of the other qualities above.

Perhaps HTML is a notation? (Or rather, maybe it was in the early days.)

When I wrote about the [original ideas behind files and
icons](/home/2021/02/01/golems) (back in February), it felt important that the
file was a _boundary object:_

Files are meaningful to computers, but they are also meaningful to users, and
_both_ can manipulate the same object. The two of you inhabit different
worlds, but you’re talking about the same thing.

So HTML, the language for making web pages, is a “notation” on an interesting
boundary. It has a small number of primitive elements, and a grammar to
compose with them. And it is…

(Those last points were more true in the early days of the web…)

HTML sits on a boundary between the machine, the creator, and the reader.

To summarise those desirable qualities, a good notation is:

I can’t quite tell whether I’m trying to force together two concepts (notation
and user interface) which are fundamentally different, or whether there is
something fruitful in seeing them as aspects of the same thing.

And I’m still not quite sure whether there are indeed lessons here for
designing a composable user interface, or a design system, or whatever it is
I’m working on.

But since I’m working on something where

Then it seems like this is the right territory to be exploring.

Any recommended reading is appreciated.
