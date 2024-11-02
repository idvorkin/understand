# Mapping the landscape of gen-AI product user experience

I talk with a lot of clients and startups about their new generative AI-
powered products.

One question is always: how should users use this? Or rather, how _could_ they
use this, because the best design patterns haven’t been invented yet? And what
we want to do is to look at prior art. We can’t look at existing users because
it’s a new product. So what UX challenges can we expect and how have others
approached them?

The problem is that there are _so many_ AI products. Everything overlaps and
it’s all so noisy – which makes it hard to have a conversation about what kind
of product you want to build.

So I’ve been working on mapping the landscape.

As a workshop tool, really.

You’ll recognise the map if you [saw me
speak](https://www.actsnotfacts.com/made/speaking) at _Future Frontend_ in
Helsinki or _UX London._ I’ve also been testing this landscape recently with
clients.

It’s a work in progress, but I think ready to share.

Let me show you…

To start, let’s look at the _first generation_ of AI products that came out
right after large language models got good enough (i.e. GPT-3) with a public
API and sufficient market interest.

So we’re rewinding to around the time of the ChatGPT release in November 2022.

![](/more/2024/07/19/ai-product-map-1st-gen-matt-webb.png)

**What are we looking at?**

A large language model on its own isn’t enough to enable products. We need
additional capabilities beyond the core LLM.

Different product archetypes rely on different capabilities to different
extents. That gives us a way to tease apart the products into a landscape.

To my mind, there are _three_ capabilities that really matter:

_These aren’t purely technical capabilities. Sure, there’s an element of
tuning the models for reliability in various ways. But mainly it’s know-how
and software frameworks. RAG was invented in 2020; the ReAct paper (which
built on chain-of-thought and led to agents) was published only in October 2022. It takes time for ideas to propagate._

I’ve used these capabilities as axes on a ternary diagram ([I love a good
triangle diagram](/home/2024/01/05/triangles)).

Now we can plot the original, common gen-AI use cases… what product
experiences do these capabilities allow?

**What this map is not** is a prescriptive chart of all possible products.
Rather, it’s a way of mapping what we already see emerging, as a way to orient
and perhaps inspire thought.

I’m not thinking about games, and I’m not looking (much) at what’s happening
in the AIUX prototyping space: I’m looking at where there’s a fit between
product and market need.

So this is a map specifically about products and user experience. I don’t
think there would be a 1:1 correspondance if we looking at underlying software
frameworks, for example.

As products lean more or less on different capabilities, I think we see four
broad areas of user experience.

![](/more/2024/07/19/ai-product-map-groups-matt-webb.png)

Users relate to the AI in different ways:

(Note that because I’m mapping out user experience, these are all to do with
collaboration.)

Now let’s break this down.

![](/more/2024/07/19/ai-product-map-archetypes-matt-webb.png)

I’ll give some examples to bring these archetypes to life.

**Tools:**

**Copilots:**

Here we have apps that would work just as well without any AI involved,
usually for working on a distinct document type.

[GitHub Copilot](https://github.com/features/copilot/) is the breakthrough
copilot product. Also see [Sudowrite](https://www.sudowrite.com) which has
multiple ways to collaborate with you when you’re writing prose fiction.

**Agents:**

A broad church!

Pure structured generation gives you data extraction from fuzzy data, like web
scraping or looking at PDFs. But then you have function calling (tool use) and
agents…

**Chat:**

(I have a ton of examples in my notes that I use as references.)

Looking at this landscape, I’m able to see different UX challenges:

The affordances problem is more general, of course. I liked [Willison’s
analogy here](https://x.com/simonw/status/1799455534506283191):

It’s like Excel: getting started with it is easy enough, but truly
understanding it’s strengths and weaknesses and how to most effectively apply
it takes years of accumulated experience.

Which is not necessarily the worst thing in the world! But just as there are
startups which are essentially an Excel sheet with a good UI and a bunch of
integration and workflow, and that’s how value is unlocked, because of the
Excel affordances problem, we may see a proliferation of AI products that
perform very similar functions only in different contexts.

I’ve been using this map to help think around various AI products and how we
might interact with them.

One process to do that is:

That is, it’s a way of focusing a collection of references in order to have a
productive conversation.

But equally another process is:

Generative!

It doesn’t help so much for inventing brand new ways of interacting. That’s
why I hang out with and pay a ton of attention to the amazing and vibrant
[London coding scene](https://www.todepond.com/wikiblogarden/london/). And
that’s why I believe in [acts not facts](https://www.actsnotfacts.com) and
rolling my sleeves up.

So it’s not a tool that gives me _answers,_ it’s not that kind of map.

But it helps me communicate, and it’s a decent lens, and it’s a helpful
framework in a workshop context.

Scaffolding for the imagination.
