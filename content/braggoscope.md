# New thing! Browse the BBC In Our Time archive by Dewey decimal code

I love listening to _In Our Time_ with Melvyn Bragg and guests ([official site
here](https://www.bbc.co.uk/programmes/b006qykl)). It’s the best radio.

There are almost 1,000 episodes (it has been broadcasting on Radio 4 since 1998) and when I want to learn about, like, Ancient Greek tragedies, or the
evolution of teeth, this show is where I turn first. All the audio is online,
which is amazing! Thank you BBC!

But actually trawling through the back catalogue is hard.

So I made a _very unofficial_ website to find old episodes to listen to.

**[Braggoscope](https://genmon.github.io/braggoscope/)** lets you explore the
_In Our Time_ archive. Check it out!

There are multiple ways to explore:

Each episode links through to the BBC website so you can listen. The full show
description and reading list are included too.

I guess I would call this _pre-pre-alpha…_ there’s no real design yet, and
there are surely some bugs with the data.

HOWEVER: I’m using it to discover new episodes already.

For example. I loved learning about the late Devonian extinction recently.
[Here’s the episode
page.](https://genmon.github.io/braggoscope/2021/03/11/the-late-devonian-
extinction.html) Now I can go down the reading list to find books, and find my
way to similar episodes about the Permian-Triassic Boundary, the Cambrian
Period, the fish-tetrapod transition and so on. Like I said, surprisingly
good.

And browsing the Directory is super fun.

(Oh and hi to anyone from the Beeb who is reading this! I’ll take this project
private if you need me to, or share the approach.)

HEY: you can stop reading here unless you want all the stuff about how it
works and my opinions about AI.

_For posterity… in the event that Braggoscope changes URL or disappears, I
want to remember what it looked like in years to come. So here are a couple of
screenshots:[the Directory](/more/2023/02/braggoscope-directory.png); [an
episode page](/more/2023/02/braggoscope-episode.png)._

I wrote up the tools I use in Braggoscope on the
[About](https://genmon.github.io/braggoscope/about) page, but as a quick
overview.

The process:

I’m a casual coder but the above is pretty straightforward.

Except the **extract** step. This is tedious. It’s a few days of writing
fiddly code to catch all the different ways that guests might be listed, or
how show notes might be written.

OR:

It occurred to me… why not just give this to OpenAI’s GPT-3?

So that’s what I did. It took 20 minutes to write the integration, then I left
the code running overnight. It costs me pennies per inference so I’ve replaced
a few days of boring graft with $30 on my credit card.

And this is _interesting_ right?

I’ve been used to thinking about generative AI and LLMs (language models) as
smart autocomplete.

But this is more like a universal coupling.

I set temperature=0 – this is a parameter that governs creativity, so by doing
this I was asking GPT-3 to be pretty deterministic.

In the prompt, I specified that GPT-3 should return structured data as JSON (a
data interchange format based on Javascript objects) and provided a type
definition.

It doesn’t _always_ return valid JSON. I have some wrapper code that fixes it
up.

It was while I was getting structured data back for the synopsis that I
thought: I wonder if I could get GPT-3 to classify this? How about using Dewey
decimal classification…?

And sure enough, it works! It’s not perfect but it’s preeeeetty good.

_(Now I read down the[list of Dewey Decimals
classes](https://en.wikipedia.org/wiki/List_of_Dewey_Decimal_classes) with
some considerable side-eye. It has, uh, a particular perspective. And it turns
out that Melvil Dewey was [a seriously bigoted and unpleasant
guy](https://en.wikipedia.org/wiki/Melvil_Dewey). But it’s a well-known
hierarchy that is small enough to wrap your arms around, and it makes topics
findable. So… I would love an alternative but that’s for another day.)_

The _“Similar episodes”_ list also uses OpenAI – each show synopsis is
translated into an “embedding,” a ten thousand parameter vector representing
its position in the “meaning space” of the language model. Then similar
episodes are simply _nearest neighbours_ (calculated with cosine similarity).

Again - this is surprisingly good! While I was developing Braggoscope I tried
using tags too but honestly, for finding related shows, this embedding
approach is way better.

This is pretty technical but you can explore the whole space yourself: here
are [all the episode embeddings in a single chart](/more/2023/02/in_our_time-
PCA-plot.html) (hover over each dot for the title). This uses PCA (principal
component analysis) on the embeddings, then the top two components (being the
most significant vectors of variability) are the x and y axes. It’s code that
OpenAI provides but will be pretty easy to customise - PCA is a ton easier
than when I used it back in undergrad! - so I’m thinking about what to use
this for.

I feel like this programmatic use of LLMs is where AI gets really interesting.

There’s the experience of it…

Using GitHub Copilot to write code ([as previously
discussed](/home/2023/01/27/copilot)) and calling out to GPT-3
programmatically to dodge days of graft actually brought tears to my eyes.
I’ve coded, mostly as a hobby, my whole life – it’s a big creative outlet
alongside writing – it’s so rarely felt like this. It feels like flying.

But the actual literal engineering of it too…

Sure [Google is all-in on AI in
products](https://blog.google/technology/ai/bard-google-ai-search-updates/),
announcing chatbots to compete with ChatGPT, and synthesised text in the
search engine. BUT.

Using GPT-3 as a function call.

Using GPT-3 as a universal coupling.

It brings a lot within reach.

I think the magnitude of this shift… I would say it’s on the order of the web
from the mid 90s? There was a radical simplification and democratisation of
software (architecture, development, deployment, use) that took decades to
really unfold.

There is so much tooling to build around temperature=0 language model calls.
There’s a startup or nine just in that.

I would like to see frameworks and programming languages that have first class
support for this as a pattern.

Anyway!

Hey, some trivia: [I was involved](/home/2017/12/21/filtered) in setting up
the _In Our Time_ podcast, way back in 2004. It was the first podcast by the
BBC, and the BBC was the first national broadcaster to do any podcasting at
all. I hand wrote the first XML files that were uploaded to the servers! Still
a fan.
