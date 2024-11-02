# Rooms, voice, gestures, and why Apple HomePod hasn’t quite clicked for me

I’ve been thinking about gestures and rooms as some of the primitives for
situated computing, and how acts like pointing and gestures could be braided
together.

I recently have an Apple HomePod mini in my home office for _reasons._ It’s
the only smart speaker in the house – I’ve always been cautious about privacy,
and anyway my use of voice (via my watch) has never stretched beyond setting
the timer for cooking and finding out how old celebrities are.

That said, I now call to the HomePod to play music and it is 70% ok and 30%
frustrating as hell.

For instance: it didn’t understand what track I wanted so I kept saying _Hey
Siri…_ followed by various incantations. Then I fell back to playing the album
and using my phone to skip to the right track. But the UI to select the device
from the Music app is buried on the Now Playing screen and in totally the
wrong place in the user flow. Or should I be accessing this via the Home app?
And, and…

So I started making notes about how it could be better. Like:

…and so on.

But when I imagine this it feels convoluted and piecemeal. It may be “logical”
but it would be hard for users (me!) to build their own mental model; it would
still be hard for designers to reason about.

This is the same place I ended up when trying to [reinvent 1950s collaborative
map rooms](/home/2023/01/20/map_room) – the conceptual framework is all wrong.

(Naturally the correct response to being momentarily grumpy about the UX of
playing a song is to write up a demand for 5 years of work as a blog post…)

I don’t know quite where this will land but I have just a hunch, just the
outlines of a conceptual framework.

We’ve got a couple competing models already:

So those don’t work, and clash besides.

Instead I’d like a conceptual framework that starts with a few principles:

Then the way we break this down is to focus on phases of interaction, not mode
(voice, keyboard, etc), and ensure that what we’re doing is humane (familiar,
intuitive, call it what you will).

For example: the micro-interaction of focus.

There is always a moment where a user _selects_ an object to talk to; to grant
focus for subsequent commands. Right now I do that by using a wake word: _Hey
Siri._

But now I’m thinking of acts I realise that, sure, I could use a wake word,
but it could also be _gestural wake:_ pointing or glancing or unambiguously
stepping closer.

I talked about this before: [How I would put voice control in
everything](/home/2020/05/26/voice) (2020).

Why can’t I point at a lamp and say **“on”** and the light come on? Or point
at my stove and say **“5 minutes”**? Or just _look_ at it and talk, if my
hands are full.

Then there’s the micro-interaction of issuing a command.

Sure you might point and speak. But then we might _also_ say that anyone in
the room can hold up their phone and see that action occurring on the object’s
soft interface, an app screen, so they can clarify either by talking or
tapping… a kind of “lean closer” moment.

Aside from interaction design, there are broader questions:

A broader question: how does this play with telepresence, connected spaces, or
overlaying virtual and physical space? I feel like the answer to how to access
devices remotely is downstream of this bigger framing.

Last, I think the _scope_ of what is in a room has to increase. A projector, a
TV, a spare screen, and other devices are as much part of this computing
environment as speakers and gadgets.

I know it’s simple. But I find this conceptual framework easier to work with,
and more generative for ideas, than considering devices in an isolated
fashion? I guess what I’m after is something as straightforward to grasp, as
achievable, and as profound as the desktop metaphor itself, only for situated
computing.

In a initial sense I would like to have interactions that are simply:

But also I would like to be have that [multiplayer map
room](/home/2023/01/20/map_room) with projectors and shared displays and
personal displays and proximity audio for hybrid presence, and be able to
clearly set out the technology Lego bricks to achieve this.

Or imagine doing something like writing on a piece of paper and holding it up
to a webcam as a natural step in a conversation, and knowing how that would be
integrated in the interactions.

I’m talking about rooms and homes here, but [Just Walk Out by
Amazon](https://justwalkout.com) is _also_ a situated interface… it’s a
computer with cameras and sensors (and the ability to take payment from credit
carts), situated in a shared environment, and how can _that_ fit in our same
conceptual framework?

Anyway. Room as distributed computer that we stand in. Objects have state.
Interaction-first not mode-first.

Then you figure out how it actually works by building and trying. I’ve started
experimenting (just on my own) with hysteresis curves for focus with pointing-
based interactions. It’s intriguing to play with gestures. But that’s another
story.

**Update 27 Jan.** Steven Smith stopped by to let me know Handoff in iOS which
does indeed pop open the remote control pane for HomePod when I hold my phone
a couple inches away! So let’s take that as a mini thought experiment because
it’s a neat capability: from a micro-interaction perspective, I would want
this capability to meet an _“increase engagement”_ moment in a conversation,
and to be available and afforded at that moment. While the pane itself is
good, the current gesture is an _“initiating”_ micro-interaction. So this pane
should be peeping on my phone _whenever_ I’m in a conversation with that
HomePod using Siri, in the same language as the remote controls for the
current room (currently buried in Control Center).

BUT this also feels a bit like getting lost in the weeds – step one is the
framework. What’s the UI for a room?
