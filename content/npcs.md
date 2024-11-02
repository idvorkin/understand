# I built my first AI NPC teammates and here’s what I learnt

How will we collaborate with AI? Let me try for a quick typology because I
want to zoom in on a particular model…

Some examples of interactive AI:

I’m sure there are more! That’s to give a sense of the breadth.

Anyway, recently I’ve been focusing in on **AI-as-teammate** because, for me,
that’s where the action is.

_Why_ AI-as-teammate?

The pragmatic answer: if we’re asking how to collaborate with AI in software,
then first let’s look at the history of collaborative software generally,
which is long and rich, and treat AI as a special case of that. Why re-invent
the wheel?

I’ve written before about how this could look:

A writer will work in a Google Doc alongside an AI editor making suggestions,
and an AI fact checker and researcher doing the running, and an AI sub doing
the wordsmithing.

When you get into the details, it turns out that the questions you ask about
how to build the interface are the questions you would ask about _any_
multiplayer/collaborative interface:

In a team context, **human/AI collaboration is a degenerate case of
multiplayer collaboration generally.**

Which is why I get so into investigating multiplayer interactions, and [I’ve
written a lot about it](/home/2022/11/09/map): I feel like it’s a pre-
requisite for really good AI interfaces.

BUT… realtime, multiplayer apps aren’t that common. I mean, increasingly they
are, but not until recently.

One of the reasons for that is that (historically) building realtime,
multiplayer apps has been a hard engineering problem. It still it, mostly. So
there’s been less experimentation and exploration than there might have been.

So that sets the scene.

_tl;dr let’s investigate AI-as-teammate in the context of realtime,
multiplayer apps, and see what we learn._

Which brings me to PartyKit.

I’m halfway through my **inventor in residence** project with PartyKit, [which
I talked about here](/home/2023/07/18/work) (at the same time as announcing my
micro product invention studio, _Acts Not Facts)._

What I’ve been doing:

(NPC = _non-player character,_ which is a term from the video-game world.
Think: fake user.)

Let’s hit those in turn.

I gave myself a month just to build toys and learn my waty around.

PartyKit is pretty low-level internet infrastructure.

Like, if you want to have live, multiplayer cursors whizzing around on your
webpage, what you do is you write some code that sends the position of your
cursor to the backend party-server. Then you write a party-server that
basically has one rule, which states: when you get an updated cursor position,
broadcast it to all the other web browsers who are connected to this page.

Then the party-server just… runs… forever. It just spins along in the cloud.

I am simply not used to realtime, multiplayer wiring being simple and
reliable. I wasn’t expecting it to be so simple I could write it myself. The
abstraction level is perfect.

And then you make it as complicated as your imagination allows.

So it feels like being given a new primitive for the internet. Would new
things could you build when relational databases came along? Or location-aware
devices? It’s on that order of novel capability.

**[Here’s my month 1 PartyKit
sketchbook.](/more/2023/partykit/sketchbook.html)**

There are 5 examples there, with short write-ups, and all the code is open on
GitHub so you can see for yourself how to write these party-servers.

_(There’s a pretty multiplayer Voronoi diagram cursor toy, which can now also
be found on the PartyKit homepage, an evolving tiny garden, and a collection
of drop-in web components to bring ambient presence to any website.)_

And I’m not going dig into those examples right here, except to say that it
was _imagination expanding,_ right?, to give myself a month to get familiar
with the material and internalise the possibilities that I didn’t realise were
there on day 1.

You don’t get as _far_ when you make working code vs drawing and writing.
That’s true.

AI-as-teammate, in my imagination, is powerful and elegant and fully-
integrated and bejewelled with clever design detailing.

But the devil is in the details. “Making” is less ambitious and less
imaginative, compared with sitting down with your pens, but what I find is
that I confront the reality of the material in unexpected ways - no matter how
crude my prototype - and that slingshots me off into brand new directions.

_Let me give you an example._

[Here’s my initial sketch of a dolphin cursor on a
webpage.](https://www.instagram.com/p/Cwp4Sg8NhnE/) _(I posted it on
Instagram.)_

What you’ll see there is simple pen and ink: there’s a dolphin cursor that
lives in a little circle, then the user asks it do something (by “chatting”
with it, somehow?). Then the cursor emerges from its home, writes a poem on
the webpage, and returns home again.

And THEN I went round the houses trying to build just that.

I’ve been building using [tldraw](https://www.tldraw.com) which is a really
good multiplayer whiteboard in a webpage. It’s low fidelity which stops you
getting lost in the weeds. (I do all my design work in tldraw, Keynote, or
code.) They offer an open source version you can integrate into your own apps.

But, when I’m running this whiteboard, should my NPC virtual user run its code
inside my web browser? Or run its own web browser in the cloud? Or connect to
the tldraw back-end server itself and attempt to manipulate the document
state? Or…

Architecturally this is interesting. Because if we are going to have AIs
living inside our apps in the future, **apps will need to offer a realtime NPC
API for AIs to join and collaborate** – and that will look very unlike
_today’s_ app APIs. And how will we get the visual training data for AI models
to connect together what the user is seeing and the machine API? Questions for
the future.

Anyway: I want to show you where I ended up.

**[Here’s my dolphin NPC PartyKit
sketchbook.](/more/2023/partykit/npcs.html)**

I posted this just today.

You’ll see three GIFs:

Check out the movies on that page. It’s all working code! I can interact with
these dolphin-cursor-NPCs. Let me tell you, it is uncanny to see a machine-
driven cursor. It doesn’t move right.

Look **yes** it’s ridiculous, and these are woefully simple, toy interactions.

But, but, _**and** ,_ I learnt a ton.

**ASIDE: first, a note about dolphins.**

If we’re going to be living and working alongside AIs, then what’s our theory
of mind for them?

They can speak our language and seemingly understand us too, better than my
smartphone can. (My smartphone understands me jabbing with one finger and
that’s about the limit of it.)

And it is _handy,_ when interacting with AIs, to ascribe it some kind of
personhood. There’s a folk psychology skeuomorphism going on there which is
useful: it means we can map person-like qualities of intent, knowledge,
personality, expertise, and foibles onto these AIs, instead of having to find
other ways to communicate that in other ways in the UI.

But AIs are distinctly not human. Like us, but not like us.

Nonhuman species are a useful metaphor, right? Dolphins are my go-to companion
species - human-equivalent smarts but utterly alien in terms of the chasm
between us.

There’s a whole history of human/dolphin interaction to draw on _([explore my
posts tagged ‘dolphin’](/home/tagged/dolphins))_ but I want to highlight some
work from 1974 by the architects _Ant Farm,_ when they designed the Dolphin
Embassy.

[I have a couple links in this post:](/home/2022/07/12/folktale)

One blueprint shows the deck of a raft on which humans have their media pod,
galley, command station and so on, and in the centre is a circular pool, with
steps going down to it, and the pool is open to the depths, meaning that
dolphins can swim up and appear inside it. So _while the human raft sits on
and is contained by the ocean, the pool is contained by the raft, and there’s
an elegant symmetry to that, a place for a meeting of peers._

That’s why, in my prototype, the dolphin pool is a triangle with a circle in
it, it’s a schematic of that work by Ant Farm. Now you know.

**Cursors are a great way to communicate attention.**

We’ve got this problem with AI-as-chat and AI-as-superpowered-menu-command
that there’s no way to _discover_ what the AI might do for me.

Sit someone down with ChatGPT, even, and they’ll barely scratch the surface of
what’s possible.

So, instead, perhaps the user can go about their regular work, and the AI can
pipe up when it spots an opportunity to be helpful?

Now that’s tricky because how can the AI be certain that it would be useful?
Or maybe the user would change what they were doing if they knew, ahead of
time, that the AI would offer help.

Cursor distance = confidence. When an NPC wants to be proactive, it can hover
nearby. It can be pushy when it _knows_ it can help. (It can remember not to
pipe up again if it is banished.) There’s a lot of resolution to explore here.

**Visual interfaces need a ‘suggestion language’ which is as good as ghosted
text is for autocomplete.**

As handy as cursor distance is, it falls down when it gets to the specifics.
The _ghosted text_ interface you get with suggested autocomplete in GitHub
Copilot is sublime. We’re going to need something just as deft when it comes
to an AI suggesting that it could (for example) automate hunting for an Airbnb
for you.

**An NPC side-channel is necessary - you can’t do it all with cursors.**

As independent and autonomous as my multiplayer dolphin cursors are, I
initially expected I would be able to craft the entire interaction via cursor
chat. Not the case.

Instead I feel like I’m coming back to chat. Now, I’ve been pretty negative on
the whole chat-sidebar thing as a UI element. It seemed dumb to me to have a
great big chat interface down the side of your app, just to talk to your AI
agent. Interact more directly, right?

But this dolphin comms/walkie-talkie block (that you can see in my NPC GIFs)
is taking me back to chat. Or rather, a form of chat which is where I chat
with my human collaborators, but also where my dolphin NPCs can offer more
fine-grained interactions.

I’m thinking I need an OS-wide chat channel that NPCs jump into as I move from
app to app.

ANYWAY: this is getting a little abstract.

Ok, two more quick points:

One thing that strikes me as funny as that cursors are so incredibly useful to
share a locus of attention, and I’m adopting them just as they’re about to
vanish entirely in the computing landscape – there are no cursors on
smartphones, or in Vision Pro augmented reality.

So maybe the future of cursors is this kind of vestigal icon showing attention
and presence, abandoned by humans, but a regular device for our nonhuman AI
brethren.

I’m going to continue to dig into NPCs for a couple weeks. I’ve got some good
foundations now to prototype with infinite canvases (with tldraw) and
autonomous NPCs (using PartyKit), and there’s a lot to figure out in terms of
interaction patterns and also in terms of future software architecture.

I’d love to see what you’re building, if you’re digging in this space too.
