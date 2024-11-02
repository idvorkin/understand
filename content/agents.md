# Who will build new search engines for new personal AI agents?

Short version:

For instance you’ll say, "hey go book me a place for drinks tonight in
Peckham, it needs to have food and not be insanely busy".

And the agent will go away and browse the web, checking that spots are
open/not insanely busy/in accordance with my previous preferences, and then
come back to me with a shortlist. "Option 1," I’ll say, and the agent will
book it.

I’m leaving _“you’ll say”_ deliberately vague. It might be via your phone, or
your AirPods, or your weird new comms badge, or a novel hardware handheld. You
interact somehow.

I’ve been hacking on agents this week and omg I have a lot of opinions haha.

Technically, the story above isn’t too hard. Let me summarise how to build
something like this…

The definition of an “agent” is an autonomous AI that has access to “tools”. A
tool is something like a web browser, or a calculator, or integration with a
booking system, anything with an API (a machine interface).

Then you know the way that ChatGPT has a turn-taking interaction, human then
AI, human then AI, etc? Agents are different. You give the AI a goal, then you
tell it to choose for itself which tool to use to get it closer to its goal…

…and then you run it again, in a loop, automatically, until the AI says that
it’s done.

So with our toy example above, the loops might look something like:

It’s wildly effective.

And totally works! With today’s technology! It’s really simple to build.

You can embellish the basic looping pattern. Agents can retain context between
sessions, i.e. the user Matt prefers some types of bars and not others. That’s
part of what makes an agent _personal._

_BTW: I know that AI large language models are merely “next-token predictors”
based on terrific quantities of matrix math and therefore they don’t THINK.
But seeing as I’m content to use the word “memory” for my computer, which
itself was controversial terminology back in the the day, I will use similar
shorthand here._

I first wrote about AI agents exactly a year ago: [The surprising ease and
effectiveness of AI in a loop](/home/2023/03/16/singularity) _(Mar 2023)._

A month later I demo’d a smart home simulator with a problem-solving agent
named _Lares_ and won a couple awards. [Here’s the Lares
vid](https://www.actsnotfacts.com/made/lares) and here’s a bunch of detail:
[Unpacking Lares](/home/2023/04/26/lares) _(Apr 2023)._

There was a TON of excitement about agents at the time. And then… nothing.

What happened? I mean, people went off and raised money and they’re now busy
building, that’s one reason. But what makes agent-based products less _low-
hanging fruit_ than, say, gen-AI for marketing copy, or call centre bots?
(These are based on prompting and RAG - retrieval-augmented generation - two
other fundamental techniques for using LLMs.)

WELL.

Imo (from building Lares back then, and re-building it this week) there are
two challenges with agents:

…and these challenges combine to make any agent-based **products** really hard
to design.

For example: if I want to book a place for drinks in Peckham tonight, and it
turns out that everywhere is busy, _as a human_ I would just choose not to
book, or chat with my friends about what to do.

But an AI agent, lacking common sense but being highly autonomous and
motivated, might email my friends to move to another evening, find I had a
clash, email that clash to cancel it, and so on, loop after loop after loop.

This is entirely plausible! LET ME GIVE YOU A REAL LIFE EXAMPLE:

Agents _have_ started shipping, a year after the original flurry.

[Devin is an AI software engineer](https://www.cognition-labs.com/introducing-
devin) by a startup called Cognition. This is a smart product move: integrate
the AI into the customer’s business by giving it a well-understood job role,
and put it in a domain where its knowledge base and activities are highly
scoped. Like it can talk to people and suggest code changes, but it’s not
going to start messing with the corporate calendar.

Although! [Here’s Ethan Mollick trying Devin for
himself](https://twitter.com/emollick/status/1770128785494700333)
_(X/Twitter):_

I asked the Devin AI agent to go on reddit and start a thread where it will
take website building requests

It did that, solving numerous problems along the way. _It apparently decided
to charge for its work._

Divergent!

Mollick’s takeaway: "Devin has GPT-4 style limitations on what it can
accomplish. I assume that the brains will be upgraded when GPT-5 class models
come out, and there will be many other agents on the market soon. A thing to
watch for."

And that’s roughly my takeaway too:

The market has clear line of sight to technical and economic feasibility now,
so expect a ton of agents over the coming months.

Here’s my tl;dr with personal agents:

But, you know, trust is a solvable issue with sane design:

Boom, done.

And, indeed, we’re beginning to see the first personal AI agents. **Rabbit
r1** is a bright orange hand-held device _(previously discussed in my post
about the[AI hardware landscape](/home/2024/01/26/hardware))_ and there we
have an agent, right there, which could go out and book a bar for me and my
friends tonight.

No the Rabbit r1 agent doesn’t run privately on-device, but the high level of
interest in the device shows cultural anticipation for a future, more highly
trusted agent.

But but but. There’s a problem I haven’t discussed.

Here’s what I mean by tools:

“Restaurant search” is a tool which will be used by future AI agents in
answering a user intent.

But restaurant search tools are not made equal. (The difference is vibe, aka
brand for you marketing types.)

How will the agent decide?

One answer to this is: **the user doesn’t get to choose how a request is
fulfilled.**

Steve Messer has a great post about [Monetising the Rabbit
R1](https://visitmy.website/2024/02/02/monetising-the-rabbit-r1/). In short,
Rabbit-the-device is a one-off purchase with ongoing opex for Rabbit-the-
company. And therefore they need to make up that gap. We can guess how, says
Messer:

Transaction fees

Subscription model

Tip your rabbit

Adverts on the free tier

Special offers from other brands

Taking a percentage of revenue

And this feels like one all-too-plausible future. When I book a restaurant,
it’s based on the kickback that Rabbit will get (or whoever). Ugh.

But what makes an AI agent _personal_ is 50% in its memory about me, and 50%
in how it dispatches its requests.

So a world we might want to shoot for is: **the user gets to choose how every
request is fulfilled** – and now we’re into an interesting challenge! How will
we build that?

Like: how exactly will my preferences be recorded? How will they be matched up
to one of the many, many available restaurant search providers, say? How can
this not be terribly cumbersome?

For an answer, I think we look at BRAND and SEARCH ENGINES.

Let me make the problem one notch more complex, which is to add this: how do
we get to personal AI agents, given that over 4 billion people have
smartphones?

Any answer regarding the future of AI agents must _also_ answer the “there
from here” question. I refuse to believe in a near-term future where AI agents
somehow _displace_ my iPhone, or require me to have another device in my
pocket.

Wonderfully, this additional constraint provides a way through the conundrum:

The AI agent chooses to search for a restaurant using [The
Infatution](https://www.theinfatuation.com) rather than Yelp because _I have
that app installed._

My personal preferences are expressed, not as a questionnaire given to me
piecemeal by the agent, but simply by looking at my existing home screen.

**Here’s the AI agent future I envisage:**

This collapses the whole “how do I choose what tool to use,” “how are new
tools developed,” “how do I trust my AI tools” and “how do I discover new
tools” into well-established patterns: I choose a vibe and build trust based
on brand; I discover new tools just like I discover new apps today, via apps
and search.

_Hang on, search?_

Why not? If my query is something like: “turn on the lights in this Airbnb”
and the AI agent on my phone needs to find an app to control the lights,
obviously I won’t have that app already, and so _of course_ it’s going to
search for it.

So now we need a AI tool search engine for use by AI agents.

And, to be a great search engine, the tools will be ranked by location, what
tools have been used previously at this location, which of several tools are
preferred by my friends, and so on.

This is exactly what the Google search engine has done for documents for like
_forever._

We already have search engines for nouns aimed at humans, now we need search
engines for verbs aimed at AIs.

Oh haha I forgot to say this is not a new idea.

I want to bring in a project I did with the Android group at Google back in 2016. I can’t talk about most of my consultancy work but I can talk about this
specific part of this one project because it resulted in a patent with my name
on it:

**[Shared experiences](https://patents.google.com/patent/WO2018164781A1/)**
(WO2018164781A1, filed January 2018).

_(I won’t say anything that isn’t explicitly in this patent.)_

Download the PDF and look at the very first image. (It’s also the hero image
on the [project write-up](https://www.mwie.com/special-projects/google) over
on my old consultancy site).

You’ll see a Venn diagram with three overlapping circles:

In the overlap at the centre: "Matching assistants."

i.e. in 2024 language, this is how an interactive AI agent finds its tools.

There is a _lot_ of detail about the possible signals in the patent text. The
fact that an app is “installed” is merely the strongest signal, but not the
only one.

Also, a twist! **Assistants should be pro-active.**

If I’m chatting with a friend about going out for a drink (using WhatsApp,
say) an AI should be able to jump in and say it can help.

_(You’ll find an illustration of that concept on my project write-up page,
also taken from the patent PDF: it’s a conversational user interface showing a
“Contact Request” dialog from an AI assistant.)_

An installed app/agent may simply join the conversation. An agent with less
confidence might metaphorically “knock at the door.”

So this answers the other challenge with AI agents which is how users discover
what they’re useful for.

In the app world, designers deal with feature discovery by building in
affordances – visual representations of available functionality. But, as I
said in my [explorations of human-AI
interaction](https://blog.partykit.io/posts/ai-interactions-with-tldraw/)
_(PartyKit blog):_ "[ChatGPT] has no affordance that points the way at exactly
how it can help."

AI agents need to be able to jump in, that’s what I’m saying. Agents, or
tools, need to be able to put their hand up and say, hey, pick me!

And this is especially important in the first few years where agent-facing
tools aren’t already installed (or approved) on my phone. Discovery will be
key.

I’m speculating ahead several steps here:

Despite the long chain of speculation, I kinda feel like this is probably how
it’ll play out?

I don’t have a conclusion here other than to draw out the future landscape as
I see it.

**Someone ought to start on that index of tools for AI agents, with novel
query and ranking technologies.** That’s a key enabler.

Other than that, oh my goodness there’s a lot to build and a lot to figure
out.
