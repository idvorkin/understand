# Observations on Siri, Apple Intelligence, and hiding in plain sight

Apple launched _“Apple Intelligence”_ yesterday – their take on AI.

I want to zoom in on the new Siri but first here’s my mental model of the
whole thing.

[Here’s the Apple Intelligence marketing page.](https://www.apple.com/apple-
intelligence/) Lots of pics!

[Here’s the Apple Intelligence press
release.](https://www.apple.com/newsroom/2024/06/introducing-apple-
intelligence-for-iphone-ipad-and-mac/) It’s an easy read too.

Apple Intelligence is (a) a platform and (b) a bundle of user-facing features.

The platform is Apple’s take on AI infra to meet their values – on-device
models, private cloud compute, and the rest.

The user-facing features we can put into 5 buckets:

Bucket 1-4 are delivered using Apple’s own models.

Apple’s terminology distinguishes between “personal intelligence,” on-device
and under their control, and “world knowledge,” which is prone to
hallucinations – but is also what consumers _expect_ when they use AI, and
it’s what may replace Google search as the “point of first intent” one day
soon.

It’s wise for them to keep world knowledge separate, behind a very clear gate,
but still engage with it. Protects the brand and hedges their bets.

There are also a couple of early experiments:

A few areas weren’t touched on:

Gotta leave something for iOS 19.

Someone shared the Apple Intelligence high level architecture – I snagged it
went by on the socials but forget who shared, sorry.

[Here’s the architecture slide.](/more/2024/06/Apple-Intelligence-
architecture.jpg)

The boxes I want to point out so I can come back them in a sec:

What’s neat about the Apple Intelligence platform is how clearly buildable it
all is.

Each component is straightforwardly specific (we know what a vector databases
is), improvable over time with obvious gradient descent (you can put an
engineering team on making generation real-time and they’ll manage
themselves), and it’s scalable across the ecosystem and for future features
(it’s obvious how App Intents could be extended to the entire App Store).

A very deft architecture.

And the user-facing features are chosen to minimise hallucination, avoid
prompt injection/data exfiltration, and dodge other risks. Good job.

Siri – the voice assistant that was once terrible and is now, well, looking
pretty good actually.

I’ve been immersed in agents recently.

(Here’s my recent paper: [Lares smart home assistant: A toy AI agent
demonstrating emergent behavior](/more/2024/lares/).)

So I’m seeing everything through that lens. Three observations/speculations.

**1\. Siri is now a runtime for micro agents, programmed in plain English.**

Take another look at the [Apple Intelligence
release](https://www.apple.com/newsroom/2024/06/introducing-apple-
intelligence-for-iphone-ipad-and-mac/) and look at the requests that Siri can
handle now: "Send the photos from the barbecue on Saturday to Malia" (hi you)
or "Add this address to his contact card."

These are multi-step tasks across multiple apps.

The App Intents database (the database of operations that Siri can use in app)
is _almost_ good enough to run this. But my experience is that a GPT-3.5-level
model is not always reliable… especially when there are many possible actions
to choose from…

You know what massively improves reliability? When the prompt includes the
exact steps to perform.

Oh and look at that, Siri now includes a detailed device guide:

Siri can now give users device support everywhere they go, and answer
thousands of questions about how to do something on iPhone, iPad, and Mac.

The example given is "Here’s how to schedule a text message to send later" and
the instructions have four steps.

Handy for users!

BUT.

Look. This is not aimed at humans. These are instructions written to be
consumed by Siri itself, for use in the Orchestration agent runtime.

Given these instructions, even a 3.5-level agent is capable of combining steps
and performing basic reasoning.

It’s a gorgeously clever solution. I love that Apple just wrote 1000s of step-
by-step guides to achieve everything on your phone, which sure you can read if
you ask. But then also: Embed them, RAG the right ones in against a user
request, run the steps via app intents. Such a straightforward approach with
minimal code.

i.e. Siri’s new capabilities are programmed in plain English.

Can I prove it? No. But I’ll eat my hat if it’s not something like that.

**2\. Semantic indexing isn’t enough. You need salience too and we got a
glimpse of that in the Journal app.**

Siri’s instruction manual is an example of how Apple often surfaces technical
capabilities as user-facing features.

Here’s another one I can’t prove: the prototype of the “personal context” in
the semantic index.

It’s not just enough to know that you went to such-and-such location
yesterday, or happened to be in the same room as X and Y, or listened to
whatever podcast. Semantic search isn’t enough.

You also need salience.

Was it _notable_ that you went to such-and-such location? Like, is meeting up
in whatever bookshop with whatever person _unusual and significant?_ Did you
deliberately play whatever podcast, or did it just run on from the one before?

That’s tough to figure out.

Fortunately Apple has been testing this for many months: [Apple launched their
Journal app](https://www.apple.com/uk/newsroom/2023/12/apple-launches-journal-
app-a-new-app-for-reflecting-on-everyday-moments/) in December 2023 as part of
the OS, and it includes "Intelligently curated personalised suggestions" as
daily writing prompts.

Like, you had an outing with someone, that kind of thing, that’s the kind of
suggestion they give you. It’s all exposed by the Journaling Suggestions API.

Imagine the training data that comes from seeing whether people click on the
prompts or not. Valuable for training the salience engine I’m sure. You don’t
need to train with the actual data, just give a signal that the weights are
right.

Again, nothing I can prove. But!

**3\. App Intents? How about Web App Intents?**

AI agents use _tools_ or _functions._

Siri uses “App Intents” which developers declare, as part of their app, and
Siri stores them all in a database. “Intent” is also the term of art on
Android for “a meaningful operation that an app can do.” App Intents aren’t
new for this generation of AI; Apple and Android both laid the groundwork for
this many, many years ago.

Intents == agent tools.

It is useful that there is a language for this now!

The new importance of App Intents to AI-powered Siri provokes a bunch of
follow-up questions:

I unpack a lot of these questions in my post about [search engines for
personal AI agents](/home/2024/03/20/agents) from March earlier this year.
Siri’s new powers make these more relevant.

On a more technical level, in the Speculations section of [my recent agent
paper](/more/2024/lares/#speculations), I suggested that systems will need an
agent-facing API – we can re-frame that now as future Web App Intents.

In that paper, I started sketching out some technical requirements for that
agent-facing API, and now I can add a new one: in addition to an API, any
system (like Google Maps for restaurant booking) will need to publish a large
collection of _instruction cards_ – something that parallels Siri’s device
guides.

Good to know!

I’m impressed with Apple Intelligence.

It will have taken a ton of work to make it so straightforward, and also align
so well with what users want, brand, and strategy.

Let me add one more exceptionally speculative speculation, seeing as I keep on
accusing Apple of hiding the future in plain sight…

Go back to the [Apple Intelligence](https://www.apple.com/apple-intelligence/)
page and check out the way Siri appears now. No longer a glowing orb, it’s an
iridescent ring on the perimeter of the phone screen.

Another perimeter feature: in iOS 18, when you push the volume button [it
pushes in the display
bezel](https://www.threads.net/@ken_isnerdy/post/C8EY7x2M2qg).

I bet the upcoming iPhones have curved screens a la the [Samsung Galaxy S6
Edge](https://www.dezeen.com/2015/03/02/samsung-galaxy-s6-edge-smartphone-
curved-screen-mobile-world-congress-2015/) from 2015.

Or at least it has been strongly considered.

But iPhones with Siri AI should totally have curved glass. Because that would
look sick.
