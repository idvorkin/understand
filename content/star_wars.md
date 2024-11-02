# What wipes in Star Wars teach us about the brain and also interface design

This seven minute video opened my eyes to the sophistication of the editing in
_Star Wars,_ and it connects to some intriguing cognitive quirks that should
be better known by designers.

**Watch on YouTube:** [Film editing psychology - screen wipes in STAR
WARS](https://www.youtube.com/watch?v=8NAhAEQUk8M) by Rob Ager (7 mins 18
secs).

It focuses on the unusual approach that _Star Wars_ has to scene transitions,
often using a "curtain sweeping visual impression" \- as in a cheesy
PowerPoint presentation - rather than a regular cut. Regular cuts work like
this:

Most movies don’t use screen wipes but instead rely on the standard scene
transition editing approach. _As one scene ends, there tends to be a momentary
gap after a section of dialogue or action comes to completion._ The gap
establishes the closure of the scene and then a cut to a new scene is
introduced, which tends to involve an initial introductory gap before dialogue
and action commences again.

That gap! In one quite normal cut: "Note the 6 second gap separating the
dialogue."

But (as the video shows) if you remove the gap, the _easing_ between scenes,
it’s too abrupt.

The gap is not required with a wipe: there is only a "2 second dialogue gap
between these two scenes which uses a fast screen wipe instead of a straight
cut."

It’s not really about saving time. "The maintenance of emotional engagement
from scene to scene is what counts."

Ager’s YouTube video has a ton of examples (there are 23 such wipes in _Star
Wars._ Most movies use… none). In particular, there are shaped wipes.

Straight-edge wipes dominate at the beginning of the movie. Circular wipes -
opening an aperture to the next scene - dominate over the final 30 minutes.

I love one wipe in particular: there’s a scene where the rebel fighters are
being briefed, and the movie move us quickly to the scene of the action:

This circular wipe begins at the part of the screen where the Death Star is
positioned, like the Death Star itself is forcing itself on screen.

I mean, maybe you don’t consciously notice it when you watch the movie.

But my goodness, when you look out for, you can see the effect on your own
attention and sense of story, and that wipe is deft af.

_([Marcia Lucas](https://en.wikipedia.org/wiki/Marcia_Lucas) won the Best Film
Editing Oscar in 1977 for her work on Star Wars.)_

Why do wipes work so successfully? ([More examples of wipes on
Wikipedia.](<https://en.wikipedia.org/wiki/Wipe_(transition)>)) I can’t prove
this, but I have a hunch.

The brain has a limited amount of resources, so it has to choose what’s going
to be regarded and what’s going to be ignored. The feeling of this resource
allocation is what we call _attention._

Attention is the topic of [Mind Hacks](https://mindhacks.com/book/) chapter 3,
and there’s a particular idea I want to pick up on called _object files._ If
you have the book and want to read more, go to _Hack #36: Feel the Presence
and Loss of Attention._ (Here’s a [search for ‘object files’ in Mind
Hacks](https://www.google.co.uk/books/edition/Mind_Hacks/K6bjvFUcedgC?hl=en&gbpv=1&dq=%22mind+hacks%22+object+files&pg=PA122&printsec=frontcover)
at Google Books.)

When you see an object, the brain automatically tracks it, setting up a
_file:_ "a kind of invisible sticky tag on the object."

The benefit? When the object goes behind something, the tag is still attached
– so when it reappears, you know it’s the same object.

What I’m fascinated by is the brain’s **automatic** allocation and
deallocation of these tags.

Because:

So the brain is full of these automatic attention allocation and deallocation
heuristics. Seeing an object shrink to a dot is one such trick.

And it isn’t just individual objects. I wrote last month about the _Doorway
Effect:_ "Your memory resets when you walk through a door." (See: [Clues for
software design in how we sketch maps of cities.](/home/2021/03/31/maps))

When you walk into a new room, your brain automatically deallocates attention
from the previous room, readying you for whatever comes next. Helpful! The
Doorway Effect doesn’t require a physical trigger. It even works on screen,
with a visual representation of a doorway.

Sounds like a _Star Wars_ wipe!

**So here’s what I think is going on:** Without a wipe, the brain needs a
couple of seconds to spin down and spin up, otherwise the shift in scene is
too abrupt. But using a wipe, there is some kind of _cognitive cue_ that
interacts with the brain’s automatic attentional system, efficiently
triggering the process of attention deallocation/allocation, making the whole
transition more efficient.

But the brain’s attentional system is half the story.

My mental model for what is going on is that there is the attentional system
and there is the emotional system.

While the attentional system makes step changes, triggered by heuristics as
discussed above, the emotional system is continuous with no such resets.

But the emotional impact of a visual impression does still decay over time.

With a Star Wars Wipe, the scene transition is 4 seconds quicker – meaning the
emotional state is still fresh, and so there is greater emotional continuity
from scene to scene. Powerful!

As I said – a hunch! But it makes sense to me.

**Interface design.**

I’m thinking about this because I’m thinking about software, and particularly
how we move between contexts: desktops, windows, apps, websites, views within
apps, and so on.

We know that some UIs feel intuitive and satisfying, and others are baffling.

Thinking about the iPhone, there are tiny visual cues all over the place:
tapping on an app will zoom it to fill the screen. Well that must perform
something like the Doorway Effect. Moving around inside an app is often a
matter of scrolling up and down (a transition with no visual edge) and panning
side to side (a transition with a hard visual edge). I don’t know what these
do to the attentional system but I know, simply from introspection, that this
is more “satisfying” than a flash that abruptly updates the display or, say, a
pseudo-3D rotating cube effect.

We’ve gotten to this place of success by modelling user interfaces on the
physical world: the computer desktop, windows with their object permanence,
“Material design” and so on. But my take is that the physical metaphor isn’t
what’s important. It’s that, by adopting the physical metaphor, we also tapped
into the brain’s heuristics for how to structure information.

So I’m curious about the _attentional ergonomics_ (let’s call it that) of user
interfaces.

And, if this is a valid way to think about software, I’d like to start using
this cognitive approach to design software. Don’t take physical metaphors too
seriously, but work directly with the deeper cognitive heuristics. Then,
taking into account the emotional system too, where would that take us? A new
grammar for interfaces?

I’m sure this has been studied by HCI groups for years, so apologies for being
obvious. But this is where my head’s at right now, so if you know the
appropriate keywords for me to read up on the research, please do suggest.
