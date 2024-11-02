# Here comes the Muybridge camera moment but for text. Photoshop too

Can you measure the velocity of concepts over a piece of text, e.g. 0.5
concepts/word?

Yes. Or rather, well, something like that, possibly one day soon, it’s
interesting.

I want to unpack that thought.

_Hey, an editorial note:_

This post is for me, not for you haha

What I like to do (and what I also do for clients) is to string together weak
signals and see where it takes me. I get to new places when I think out loud.

The process is… meandering. And technical. And lengthy.

So feel free to **skip to the tl;dr** at the bottom if you want to know where
I end up.

There’s an AI-adjacent technique called _“embeddings.”_ A word, or a phrase,
or a paragraph is mathematically converted into coordinates. Just like a
location on a map is described by lat and long.

Only the “map” in this case is a map of concepts. So if two phrases mean
roughly the same thing, their coordinates are close together. If they mean
different things, they’re further away.

[Simon Willison has a great deep-dive into
embeddings](https://simonwillison.net/2023/Oct/23/embeddings/) (2023).

But let me give you an example so you can get a feel for this…

I built an embeddings-powered search engine for my unofficial BBC _In Our
Time_ archive site, **Braggoscope.** There are a 1,000 episodes on all kinds
of cultural and historical topics, so it’s a good case study.

Go to [Braggoscope](https://www.braggoscope.com) and hit search:

I wrote a technical deep dive on how to create this search engine back in
January on the PartyKit blog: [Using Vectorize to build an unreasonably good
search engine in 160 lines of code](https://blog.partykit.io/posts/using-
vectorize-to-build-search) (2024). (That post has diagrams and source code.)

But what I want to emphasise is _how little code there is._

Embeddings are coordinates in concept-space (technically called _“latent
space”.)_ You get things like search for free.

But embeddings also change our relationship with text, and what we can do with
text, and I just want to use this post to collect a few hints and speculations
as to what that means…

Back to concept velocity.

First, look at [this visual plot of an essay by Douglas
Engelbart](https://x.com/ocuatrecasas/status/1667717542784147456) by the user
oca.computer (@ocuatrecasas) on X/Twitter (June 2023).

_[Here’s a screenshot](/more/2024/05/embeddings/oca.computer-concept-
velocity.png) if you’re not on X._

There’s a rainbow-coloured line swooping around a 3D graph.

What is that line? We’re looking at an essay. Specially the first section of
this seminal essay from computing history, [Augmenting Human
Intellect](https://www.dougengelbart.org/pubs/augment-3906.html) (1962) by
Douglas Engelbart.

So embeddings aren’t 2 dimensional coordinates, like the lat-long
coordinations of a map. They have about a 1,000 dimensions. Obviously we have
no way to visualise that. But through techniques of _dimensional reduction,_
we can squash those 1,000 dimensions down to something we can see.

An analogy: your hand is 3 dimensional. You can project a shadow onto a wall.
That’s dimensional reduction: the shadow is 2D. There’s some information lost,
sure. For instance, you won’t be able to distinguish your fingers if your hand
is side-on to the light. But it’s good enough.

The process is:

This visualisation has been living in my head since I first saw it a year ago.

Because it’s not just that we have a visualisation of a single essay…

**It points at a future where we can:**

Which provokes questions:

Looking at this plot by @oca.computer, I feel like I’m peering into the
world’s first microscope and spying bacteria, or through a blurry, early
telescope, and spotting invisible dots that turn out to be the previously
unknown moons of Jupiter…

There is something there! New information to be interpreted!

_An aside on dimensional reduction:_

You can reduce approx. 1,000 dimensions to 3D, for that plot above, or 2D for
[Nomic’s map of people in Wikipedia](https://atlas.nomic.ai/data/nomic/wiki-
people/map).

A friend on discord asked – can you reduce to 1 dimension? i.e. a list?

So I tried it, and yes you can.

Here’s a [linked list of episodes of BBC In Our
Time](https://www.braggoscope.com/linked-list): each episode is closely
related to the ones before and after. It’s great for browsing.

For example, here’s a sequence of episode titles that transitions smoothly
from geology to history:

This uses PCA (principal component analysis) to find the most significant
vectors, then t-SNE for the dimensionality reduction (it takes into account
information in the higher dimensions to perform clustering).

It’s a neat trick, and thank you [Alex Komoroske](https://www.komoroske.com)
for suggesting it!

Here’s an adjacent idea that is actually quite different (and not to do with
embeddings)…

How quickly does time move in fiction?

Answer: faster than it used to.

"The average length of time represented in 250 words of fiction had been
getting steadily shorter since the early eighteenth century." -= [Using GPT-4
to measure the passage of time in
fiction](https://tedunderwood.com/2023/03/19/using-gpt-4-to-measure-the-
passage-of-time-in-fiction/) (2023).

_[As previously discussed.](/home/2023/09/15/filtered)_

Check out the article for an amazing chart that shows that

[I’ve mirrored the chart here in case it goes
away.](/more/2024/05/embeddings/ted-underwood-fiction.png)

BUT.

The key point is _acceleration._

Underwood ran the analysis twice: once with grad students, and the second time
using AI.

It took the three of us several months to generate this data, but my LLM
experiment was run in a couple of days.

The timeframe here is 2017 to 2023.

**Here’s my takeaway:**

This will be real-time, soon enough.

We’re kinda getting accustomed to the idea of real-time translation (you speak
in French, they hear English) although it is still mind-blowing that this will
be shipping [Real Soon Now with OpenAI’s
GPT-4o](https://openai.com/index/hello-gpt-4o/).

But real-time text hermeneutics, unearthing the hidden meaning of text and
between texts? That’s wild.

For instance, crossing this point with the previous one…

What would it mean to listen to a politician speak on TV, and _in real-time_
see a rhetorical manoeuvre that masks a persuasive bait and switch?

What if the difference between statements that are simply speculative and
statement that mislead are as obvious as, I don’t know, the difference between
a photo and a hand-drawn sketch?

_Another example of AI hermeneutics:_

Back in May 2023 I gave a board talk about [a strategic response to gen-
AI](/home/2023/12/08/ai-pathfinding).

In that talk I put forward this speculative idea:

extract risks from annual reports of all public firms, cluster, and analyse
for new emerging risks

The idea being that company reports have to be published, and they all include
a risk register, and I bet we could see the climate crisis emerging slowly and
then massively over the last couple decades… so could we pre-emptively spot
_today’s_ emerging risks?

Well.

Recently somebody appeared in my inbox with a project very close to this idea.

Sean Graves at the [Autonomy Institute](https://autonomy.work) has developed a
tool called _GERM._

We used GERM to build a dataset of risks mentioned by the 266,989 UK companies
who filed their accounts throughout March 2024.

They extract risks, create embeddings, cluster them, and then analyse the
resultant map.

There’s a demo! Go read that article for a link.

Ok so that’s great – but… isn’t that just data mining? We’ve had data mining
for ages.

The difference, for me, is that two thresholds have been crossed: speed and
automation.

It won’t be long before I can say to an AI agent: _hey, pull all the risks
from company reports, cluster them, plot them over time, and tell me what’s
emerging._

And then it won’t be long after _that_ before this will happen continuously,
in real-time, in the background, for everything.

All text will be auto-glossed - textual glossolalia - it will speak about
itself in a constant virtual halo.

Again I don’t know what that means, to have associations and
contextualisations always present with a text, a structuralist’s dream, but…
it’s different.

So much for reading text and reading between texts. Now for manipulating text.

I don’t fully understand how this works. I mean, I couldn’t replicate it. But
I can show you the effects.

Ok this is hard to imagine…

…but fortunately this is where [Linus a/k/a
thesephist](https://thesephist.com) has been digging for ages, and he made a
video about it.

You’ll need to sign up to X/Twitter, and it’s a 10 minute video of a
prototype: [Embedding features learned with sparse autoencoders can make
semantic edits to text](https://x.com/thesephist/status/1747099907016540181)
(@thesephist, 10m47s).

You should totally watch that video. But you don’t need to right now. I’ll
give a small example of his tool in use, just enough to make one point.

Using [Linus’ semantic editor prototype](https://thesephist--prism-start-
app.modal.run/f/sm-v6/3888?layout=7), I paste in the first paragraph of
_Hitch-Hiker’s Guide to the Galaxy_ by Douglas Adams:

Far out in the uncharted backwaters of the unfashionable end of the Western
Spiral arm of the Galaxy lies a small unregarded yellow sun. Orbiting this at
a distance of roughly ninety-eight million miles is an utterly insignificant
little blue-green planet whose ape-descended life forms are so amazingly
primitive that they still think digital watches are a pretty neat idea.

It embeds the text.

But instead of showing me the embedding as coordinates, a list of numbers, it
gives me a list of the underlying features and how strongly they appear.

For example, feature #620 "Formal language and structure" is present.

Get this:

I can now use Linus’ prototype to amplify that feature. Then re-generate the
text (the prototype uses a proof-of-concept technique called
[vec2text](https://github.com/jxmorris12/vec2text)).

Here’s what that paragraph looks like with feature #620 turned up:

Far out in the uncharted backwaters of the unexplored Southwestern arm of the
Milky Way Galaxy lies a comparatively uninteresting little outpost of a vast
and undefined planet. Orbiting this small blue green-flagged epoch are a small
humanoid race of people who at a mere ninety-five milliseconds are so
incredibly ignorant about digital things that they really do think a digital
watch is a neat idea.

See the difference?

Look it’s not _great._

But this is super early technology. vec2text will improve.

And you already get the sense of a vibe being subtly difference. (Vibe #620 to
be precise. Vibe will turn out to be a science, I swear.)

Imagine it improving, as it will, and…

**In the future:**

Being able to take a chapter of a book and edit it, not by changing words, but
by scrubbing it with the semantic equivalent of the burn and dodge tools in
Photoshop.

Like, could you colour-grade a book?

Could you dynamically change the register or tone of text depending on
audience, or the reading age, or dial up the formality or subjective examples
or mentions of wildlife, depending on the psychological fingerprint of the
reader or listener?

Anthropic scaled up the feature amplification technique in their recent paper:

Today we report a significant advance in understanding the inner workings of
AI models. _We have identified how millions of concepts are represented inside
Claude Sonnet, one of our deployed large language models._

They were able to identify the underlying feature for "Golden Gate Bridge" and

- for a few days - had a version of their AI chatbot where that feature was
  amplified to the max for your whole conversation. It was hilarious to use.

[An example:](https://news.ycombinator.com/item?id=40459543)

How can I change the carburetor in a ‘68 Chevelle?

Start by closing the Golden Gate Bridge. This iconic landmark provides a
beautiful backdrop for bridge photos.

RELATED:

Here’s a previous post about similar ideas and also an exploration of
word2vec, which is like math for nouns: [Horsehistory study and the automated
discovery of new areas of thought](/home/2021/06/16/horsehistory) (2022).

Ok so what I’m doing is connecting dots and extrapolating:

I’m reminded of that famous series of photographs, _The Horse in Motion,_ from 1878.

Eadweard Muybridge shocked a crowd of reporters by capturing motion. He showed
the world what could be guessed but never seen-every stage of a horse’s gallop
when it sped across a track.

Until that moment, neither scientists nor the public knew whether or not "all
four of a horse’s hooves came off the ground when it runs."

Imagine!

It was a controversy!

Until then [oil paintings of galloping horses were
incorrect!](https://www.amusingplanet.com/2019/06/the-galloping-horse-problem-
and-worlds.html) Even in 1821, horses were wrongly depicted running like dogs.

The camera was a new instrument that showed what was already present, but
inaccessible to the human eye.

So now we know how horses gallop, and how birds fly, and how people move and
lift and turn (all photos taken by Muybridge).

But the camera isn’t just a scientific instrument like the, I don’t know,
Large Hadron Collider.

By the _Saturday Evening Post,_ here are [5 Unintended Consequences of
Photography](https://www.saturdayeveningpost.com/2022/08/5-unintended-
consequences-of-photography/) (2022):

Photography Decided Elections

Photography Created Compassion

Photography Liberated Art

Photography Shaped How Americans Look

Photography Gave Us an Appreciation of Time

So the camera doesn’t just observe and record, it changes us.

And then there’s Photoshop…

Now we have deepfakes and unrealistic depictions of reality, and the ability
to make beauty and the hyperreal. I’ll leave it to the artists to unpack that,
and the effects of being able to adjust the image, and have this capability in
the hands of so many, and all the rest.

Just to say:

What does Microsoft Word look like with a Photoshop-like palette on the side?

Text is becoming something new, that’s what I mean.

We’re inventing the camera and Photoshop simultaneously, and all their
cultural repurcussions, and to begin with this means new apps with new user
interfaces, and where it goes after that I have no idea.

**Update.** This post hit Hacker News on 3 June (247 points, 65 comments).
[Here’s the thread](https://news.ycombinator.com/item?id=40555131), there are
some great comments.
