# Spatial interfaces for conversations and software

Zoom**\*** is pretty good for 5 people because it works as a single
conversation, this being the canonical conversation group size with associated
[psycho-physical limits](/home/2003/10/27/actually). And it’s pretty good at
150 because it works like a presentation. But it’s pretty poor for 25.

**\*** _I reckon I’ll start using zoom as a generic for all group video calls,
doing double-duty noun and verb, like hoover for vacuum cleaner/cleaning._

So what about 25 people? I’m excited about this new software
[MakeSpace](https://makespace.fun) because it tackles that problem in a
fundamental way. As a participant, you place yourself on a 2D canvas, and then
the sound is spatialised: if you’re near someone, you’re loud to each other;
you get quieter when you’re further away. This allows for multiple
simultaneous conversations and moving between them.

MakeSpace also has some other powerful primitives like

The website has a ton of examples, clearly illustrated.

MakeSpace isn’t yet open for general access. But if you want to give spatial
interfaces a go as a way to socialise, both [Online
Town](https://theonline.town) and [Rambly](https://rambly.app) are video chat
webapps modeled on top-down old-school computer games with spatial sound.

And don’t forget [spreadsheet parties, as previously
discussed](/home/2020/06/15/hallway_track).

Back in August 2019, John Palmer wrote an illustrated review + concept paper
on this topic: [Spatial
Interfaces](https://darkblueheaven.com/spatialinterfaces/). It is smart, idea
RICH, and worth digging into:

Suppose I work at a company and I want to find out, “Who is everyone at my
company meeting with right now?” With only Google Calendar at my disposal,
this task is a nightmare.

…

Now try to answer the same question with [2D virtual office software]. “Who is
everyone at my company meeting with right now?” All of a sudden, it’s
extremely easy. You just look at the rooms.

Palmer’s follow-up piece, [Spatial
Software](https://darkblueheaven.com/spatialsoftware/), in April 2020 has a
ton of examples of real software. I’m especially intrigued about the spatial
metaphor _not_ as a way to socialise, but as a way of hacking memory and
psychology.

[Nototo](https://www.nototo.app/) is a spatial note-taking app. It lets you
build an ever-expanding, topographical map containing your notes and writing.
The app is designed this way to take advantage of another aspect of spatial
interfaces: our brains remember spaces better than raw information. In this
regard, Nototo is like a software manifestation of a [memory
palace](https://en.wikipedia.org/wiki/Method_of_loci).

The physical world is baked deep into human cognition. It always amazes me
that [passing through doorways genuinely causes a memory
lapse](https://news.nd.edu/news/walking-through-doorways-causes-forgetting-
new-research-shows/) – but it shouldn’t amaze me because of course it does:
"Entering or exiting through a doorway serves as an ‘event boundary’ in the
mind, which separates episodes of activity and files them away."

Which is only natural. Of course your brain wants to be fully prepared to
absorb new information when you enter a new context, so it flushes everything
that came before.

And I mean, why not take advantage of our hard-wired physics of information to
make software easier to use?

ANALOGY FOLLOWS +++ Our brains are similarly hard-wired to assume light comes
from above, which is why shadows “underneath” cause 2D shaded shapes to pop
(see [#20 Fool Yourself into Seeing
3D](https://books.google.co.uk/books?id=K6bjvFUcedgC&pg=PA57&dq=%22mind+hacks%22+%22fool+yourself+into+seeing+3d%22&hl=en&sa=X&ved=2ahUKEwixr6j02ePqAhW8UxUIHdtlAAsQ6AEwAHoECAIQAg#v=onepage&q=%22mind%20hacks%22%20%22fool%20yourself%20into%20seeing%203d%22&f=false)
in _Mind Hacks_). And this is why [Susan Kare’s 3D button design in Windows
3.0](https://www.webdesignerdepot.com/2009/03/operating-system-interface-
design-between-1981-2009/) \- _in 1990! using only 16 colours!_ \- was such
genius. You don’t need to _learn_ that’s a thing you can push. It just _looks_
like a thing you can push!

So yeah. Dunno. Still thinking about space as an interface metaphor.

A PAUSE FOR THE INTROSPECTION SECTION:

I’m intrigued about _personal_ spatial interfaces - like that note-taking app

- but I’m not convinced. I’d like to try it.

I don’t think I’d enjoy organising my notes on a map. I’m a highly associative
thinker, but that doesn’t seem to me to happen visually. I mean – thinking
hard appears to make use of my visual _system:_ when I’m thinking hard about
how to organise an essay, for example, I can’t see what’s right in-front of my
eyes, so the two processes must be rivals for the same underlying grey matter.
But the subjective experience of it isn’t visual.

Generally: I don’t see pictures behind my eyes unless I’m trying hard to
imagine something, in the same way that I don’t have an internal monologue
unless I’m planning how to write a sentence. So I would find an on-screen map-
like organisation of my notes to be an interruption to my thinking somehow.

BUT, I do seem to think spatially in at least some ways. When I’m writing a
talk, I pull a half dozen books from my shelves and stack them next to me on
the table or sofa. I might never consult them, but the _proximity_ creates a
kind of gravity of thought somehow? Maybe a self-imposed psychic style
transfer?

I guess my equiv for this in software is the way I paste loads of notes into
the bottom of a doc before I start writing at the top? Proximity again.
Abstract spatiality.

**Mad Hatter:**

Back to how to have multiple simultaneous conversations and picking up again
on _audio_ – this time only barely spatialised.

I remember running across a paper in 2003 about a prototype which did this
**automatically** for telephone conference calls. In the following, “floor” is
the jargon for a conversational group.

In face-to-face interactions in such social groups, conversational floors
change frequently, e.g., two participants split off to form a new
conversational floor, a participant moves from one conversational floor to
another, etc. To date, audio spaces have provided little support for such
dynamic regroupings of participants, either requiring that the participants
explicitly specify with whom they wish to talk or simply presenting all
participants as though they are in a single floor. **By contrast, the audio
space described here monitors participant behavior to identify conversational
floors as they emerge.**

The _Mad Hatter_ system monitors the speech of all participants:

The result is that multiple conversations can occur in parallel, and
participants can move between them, _on the exact same audio-only telephone
conference call._

It would be intriguing to revisit this work in the light of the popularity
group video calls in 2020.

_Here’s the paper:_

Paul M. Aoki, et al. [The mad hatter’s cocktail party: a social mobile audio
space supporting multiple simultaneous
conversations.](https://www.paulaoki.com/papers/chi03.acm.pdf) CHI ‘03:
Proceedings of the SIGCHI Conference on Human Factors in Computing Systems,
ACM, p425-432 (2003)
