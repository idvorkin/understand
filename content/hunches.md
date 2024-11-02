# An AI hardware fantasy, and an IQ erosion attack horror story

_(This is #2 in what it turns out is an ongoing series of highly speculative,
almost entirely unfounded hunches about AI. The first was[about alignment and
microscopes](/home/2023/05/04/hunches).)_

I like to describe AI as a 10 year wormhole into the future ([maths
here](/home/2023/05/04/hunches)).

We can date it to the release of ChatGPT in November 2022 which is when the
technology, UI, and public understanding all came together, but really it was
5 years in the making: the underlying architecture of large language models is
the Transformer model, and the [original
paper](https://arxiv.org/abs/1706.03762) came out of Google Research in 2017.

It took OpenAI to do the engineering to scale it though. OpenAI was founded in 2015. So let’s say an overnight 10 year leap with a 7 year run-up.

But now OpenAI is _going_ for it.

What I love about OpenAI is that they hold nothing back.

There’s no clever MBA-authored strategy like holding a feature till next year
to maximise profits. Just: bang bang bang. Everything they’ve got, as soon as
it’s ready. User-facing in ChatGPT and for developers via the platform APIs.

For instance: here’s [Sam Altman’s opening
keynote](https://www.youtube.com/watch?v=U9mJuUkhUzk) _(YouTube)_ for OpenAI’s
developer day last week. It is 45 minutes and tight af.

[The full list of announcements](https://techcrunch.com/2023/11/06/everything-
announced-at-openais-first-developer-event/) _(TechCrunch)_ includes the
ability to make custom ChatGPTs that can browse the web and use tools on your
behalf, and a app store for them; new APIs for a version of GPT-4 that can see
(so fast that it can interpret video), and also for the new image generation
model DALLE-3; APIs for great speech synthesis (i.e. everything can talk now)
and a bunch more. Like, the Assistants API means it’s easy to build a copilot
for any app and you know [how I feel about
NPCs](https://blog.partykit.io/posts/ai-interactions-with-tldraw).

As a developer, this is exactly what you want from your platform company.

So I am not the only person to make a comparison with Apple keynotes.

Which are slick but omg so long and maybe not as action-packed as they used to
be. I mean, you think about Apple’s [Vision Pro
announcement](https://www.youtube.com/watch?v=GYkq9Rgoj8E) _(YouTube)_ and
it’s part of a 2 hour keynote and oh _so much explaining._

Which I love for the design nerdery and also is necessary to make sure the
media lands right, I know. But you get the impression that Sam Altman would
have come on stage wearing the thing, given a brief demo, shared a link to the
developer documentation, wrapped up, and the whole slap in the face would have
felt like the sonic boom of the future arriving.

Which takes me to a fantasy of combining the Apple and OpenAI approaches.

Apple is a hardware product company. But just suppose it were a hardware
\_platform\_\_ company, a platform for other people’s hardware, OpenAI-style
holding nothing back.

You’d get components that would up-end the supply chain.

Tiny sensors that can do gaze and pointing detection. Microphones with
absolutely perfect AI-powered speech recognition built in, and configurable
semantic understanding such when someone says “turn on” (or anything similar,
while paying attention to it), GPIO pin 1 goes high. Instead of a pseudo-3D
lenticular display just for the Vision Pro, one that whichever OEM can build
around.

Like any platform company, there would be evaluation boards, but building from
the OpenAI playbook, the sensors and components would have plug-and-play
versions for individual developers in the form of Raspberry Pi shields and so
on. So there would be on-ramps and routes to scale.

This is an old fantasy: in my 2020 post [How I would put voice control in
everything](/home/2020/05/26/voice) I set this out…

If I had all the VC money in the world, I would manufacture and sell
standardised components – they would connect and act identically to mechanical
buttons, switches, and dials, only they would work using embedded ML and have
voice, gaze, and pointing detection, for interaction at a distance.

The goal would be to allow manufacturers of every product to upgrade their
physical interfaces (add not replace ideally), no matter how trivial or
industrial, no matter how cheap or premium.

And this is how we would get to [intelligence too cheap to
meter](/home/2023/10/06/ubigpt) and situated, embedded AI. _(There are a bunch
of examples in that post.)_

I want my oven that knows how to cook anything just by looking instead itself
and autonomously googling when it recognises the food! I want my telepathic
light switches!

But we need AI in the hardware supply chain, not vendors who have to own the
whole stack.

Maybe OpenAI will decide to take it on.

Ok. Autumn daydream over.

Shortly after OpenAI released its new tools, ChatGPT went down together with
all the APIs, for several hours.

There was a coding task I was in the middle of that I literally couldn’t
complete. Not because I needed API access to GPT-4, but because without
ChatGPT I was too dumb to deal with it.

I said on X/Twitter that my IQ had dropped 20 points.

_(If you’re a sci-fi fan then it was an experience from Vernor Vinge’s[Zones
of Thought](https://tvtropes.org/pmwiki/pmwiki.php/Literature/ZonesOfThought)
books – living happily in the Beyond and then being engulfed in a Slow Zone
surge.)_

And I wonder what the collective intelligence drop was, that day.

Like, if ChatGPT has 180 million monthly active users, could we say something
like 1% of the population of the US would have wanted to use it over the down-
time?

The US has a population of approx 300 million or, in other units, 30 billion
collective IQ points.

So if you ding that by 3 million people at -20 IQ each, that’s 6E7 out of
3E10, or a 0.2% knock on collective intelligence for that day.

By way of comparison, that’s a decent fraction of the effect of leaded fuel.
(Everyone born before 1990 [has their IQ nerfed by
4.25%](/home/2022/03/11/saeculum).)

And as someone into [weird state-sponsored
exploits](/home/2021/03/25/exploits) I wonder: would it be worth doing this
deliberately?

RELATED TO THIS:

I recently added really smart AI-powered semantic search to my unoffice
archive of _In Our Time_ shows. Go to
[Braggoscope](https://www.braggoscope.com), tap _Search_ in the top nav, and
type "the biggest planet" – the episode about Jupiter comes up. So there’s a
kind of knowledge in the large language model, or whatever you want to call
it, a sort of relatedness that makes it easy to put ideas together.

[Here’s the code on GitHub](https://github.com/genmon/braggoscope-search),
open for your interest: you’ll notice in the Cloudflare worker that this
“knowledge” comes from a model called `baai/bge-base-en-v1.5`.

[Here’s the model on Hugging Face](https://huggingface.co/BAAI/bge-base-
en-v1.5): BAAI, the creator, is the Beijing Academy of Artificial
Intelligence.

Now, I don’t mean to sound paranoid here.

But in Samuel Delaney’s astounding 1966 sci-fi/speculative-linguistics novel
[Babel-17](https://www.amazon.co.uk/Babel-17-S-F-MASTERWORKS-Samuel-
Delany/dp/0575094206/) _(Amazon),_ [SPOILERS] [Babel-17 is a
weapon](https://tvtropes.org/pmwiki/pmwiki.php/Literature/Babel17), an
artificial language constructed such that intuitive leaps about combat
manoeuvres are instantaneous, so it will be adopted virally simply out of
utility, but the language itself omits particular connections making certain
other ideas topologically impossible.

So: would it be possible to release an AI large language model that is
exceptionally good and cheap, maybe, gaining popularity in a target language
(English, or Russian, or Korean, or whatever) but makes it really hard to
reason about certain concepts?

Not so ridiculous! This has happened once before actually, accidentally!

[The argument in Gerovitch’s From Newspeak to
Cyberspeak](/home/2018/01/03/2017_books) is that, when computer science papers
in the 1960s were translated from English to Russian, they were stripped "of
metaphorical yet inspirational ideas like “memory” and “learning”,
constraining the vision of computing to simple calculation." Which is why the
Americans figured out the personal computer, our bicycle for the mind, whereas
the Soviets did not.

Could you popularise an AI that made conceptual leaps around worker-friendly
capitalism much harder? (For example, given that policy makers will be heavy
users of future ChatGPTs, and this trend will slowly lead to social unrest.)

Could you wait until a nation were in an intellectual arms race, like a Space
Race for the 2030s, say, then knock over the intelligence augmentation
infrastructure (i.e. ChatGPT v9) in critical weeks?

I’m not saying that this _is_ what is happening. But any government worth its
salt should have a half dozen people figuring out how to perform an IQ erosion
attack, precision targeted or otherwise, and another half dozen red-teaming
how to respond if one hits.
