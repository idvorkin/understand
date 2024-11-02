# New app! A compass that points to the centre of the galaxy

Hey I made an app! It’s a green floating arrow that always points to the
middle of the Milky Way.

i.e. 26,000 light years towards the supermassive central black hole,
Sagittarius A\*.

You can have it too!

**[Download Galactic Compass from the App
Store.](https://apps.apple.com/gb/app/galactic-compass/id6451314440)**

BUT: I don’t know how to write apps.

And yet here we are!

Let me explain.

![](/home/static/content/2024/02/15/galactic-compass.jpg)

It’s remarkably grounding?

Once upon a time I trained myself to always know where to look, and the centre
of the galaxy moves of course over the day and the year: "So I would end up
pointing through the pavement, or down a street, and thinking, huh, that’s
where it is."

It is a worthwhile super-sense:

Eventually then I had this picture of myself, and the Earth, and the solar
system, and the centre of the galaxy which had initially been whirling round
me, and now it had flipped, _I was turning around it._

It was wildly situating.

I’ve lost the intuition now, sadly.

The above description is from [my 2021 writeup](/home/2021/06/30/galaxy) which
I conclude by saying:

In my imagination I see an iPhone app which displays a 3D model, connected to
the gyroscope and the compass and the GPS. …

_But there are slightly too many things I would need to learn_

So I couldn’t build it.

EXCEPT.

_Now there is ChatGPT._

I can’t write Swift (the language used to code iOS apps).

But what I am able to do is break up large problems into smaller, expressible
problems, and then sequence them.

**I’ll be detailed about this.** When I’ve walking folks through this, they’re
often interested so it is (perhaps) non-obvious?

_If you’re not interested in the detail, skip to the next section._

I started by installing Xcode and setting up a git repo. I know how to do
that. (GitHub Copilot doesn’t work in Xcode by the way.)

To get going, I said to ChatGPT 4 something like:

Then I followed the instructions.

There was lots of interaction like: _okay I’ve done step 1. I’m on step 2 but
I can’t see the X, or I have the error Y, what should I do?_

I know, from other coding, that I want to have my build working as early as
possible.

My next question to ChatGPT was something like:

Ok, now I’ve got a setup which means I can develop and I can test.

Now putting together the app itself is _not_ about describing the overall app.
I don’t want ChatGPT to be overfaced.

I worked in steps at this kind of resolution, making sure each step was
complete before moving to the next:

The workflow consisted of me copy and pasting code from ChatGPT into Xcode.
When there were errors, I would paste the error text into chat and say “this
error appears on the line about such-and-such,” and work with it on
corrections.

Often I would start each stage by saying to ChatGPT: _ok here’s the current
code,_ and then paste in the entire ContentView file.

The generated code is not obscure to me. I’m not asking ChatGPT for huge goals
with multiple steps and pasting in code unseen – that wouldn’t work. The
experience is more like very, very good autocomplete, or very, very good
spellcheck: I can understand the output even if I couldn’t get there on my
own.

Next I found a Swift-compatible library to translate between galactic
coordinates and relative coordinates. (Ultimately I need altitude and azimuth,
a way of pointing at a position in the sky, based on the current time and
location.) I’m using [SwiftAA](https://github.com/onekiloparsec/SwiftAA).

I retained the Debug tab in the shipped app so you can see.

So that’s all the astronomical stuff done.

You never want to give ChatGPT big goals where it has to figure out the way on
its own. Then both of you will be confused. Intermediate stepping stones and
being sure of your boots with each stride, that’s the way.

Now we build the rotating arrow:

This now became pretty tricky because I had to learn about how to combine
rotations. I barely know anything about quaternions, so there was a bunch to
learn here.

ChatGPT, being a large language model but lacking embodiment, is awful at 3D
maths and reference frames.

Finally I…

Galactic Compass is still pretty janky, to be sure.

But it ain’t bad for a collaboration between someone who can’t build apps and
an AI that is barely a year old.

Ethan Mollick and a team of social scientists studied a group of management
consultants using AI.

[The headline is that, yes, AI results in better
work.](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)

The fascinating buried result is that the biggest effect is felt by the
_bottom-half skilled participants._

i.e. if you’re sub-skilled then you can use AI to drag you up to median.

Now, none of us have just one skill. Like most people, I have a mix.

But now I’m a reasonable engineer, an amateur designer, an ok systems thinker,
ok at having ideas, and now a midwit _everything_ when it comes to all the
actual skilled tasks.

And the combination means I can bring ideas to life that simply wouldn’t be
possible if I had to persuade a designer or engineer buddy to help me out.
Being able to bring ideas to life means I can scaffold up to other ideas… and
others…

Like this galactic compass.

Back in 2020, Robin Sloan said that [an app can be a home-cooked
meal](https://www.robinsloan.com/notes/home-cooked-app/). It’s such a
memorable perspective, and what we should aspire to from our software.

Now I’ve cooked a meal that anyone with an iPhone can download. Probably only
a couple dozen people will want it, but I want it in my pocket, and I want to
share it with my friends, and here we are.

And I can’t even cook!

But I know where the centre of the galaxy is, even so.

[Download from the App Store.](https://apps.apple.com/gb/app/galactic-
compass/id6451314440)

[Project page on Acts Not Facts.](https://www.actsnotfacts.com/made/galactic-
compass)

_**Update 16 Feb.**_ Huh this did numbers! My [post on
X/Twitter](https://x.com/genmon/status/1758198836109938837?s=20) currently has
~~7.2K likes and 1.3M views~~ 12K likes and 6.1M views. A post that quotes
mine has ~~35K likes~~ 161K likes! Whoa.

Here’s a lovely post on BoingBoing in which Mark Frauenfelder includes [a
photo of Galactic Compass with his
cat](https://boingboing.net/2024/02/15/iphone-app-that-finds-the-milky-ways-
heart.html).

My post on Hacker News kicked off a brilliant, friendly conversation (150
points, 57 comments): [Show HN: Galactic
Compass](https://news.ycombinator.com/item?id=39389858).

I’m glad y’all like it. Thank you.

_Two additional asks while you’re here:_

Ad astra!

_**Update 21 Feb.**_ Galactic Compass peaked at #87 in the Travel chart for
the US App Store!

I spoke with Ars Technica about the whole story: [New app always points to the
supermassive black hole at the center of our
galaxy](https://arstechnica.com/gadgets/2024/02/new-app-always-points-to-the-
supermassive-black-hole-at-the-center-of-our-galaxy/).

It ends with a pretty cosmic quote from me:

“Once you can follow it, you start to see the galactic center as the true
fixed point, and we’re the ones whizzing and spinning. There it remains, the
supermassive black hole at the center of our galaxy, Sagittarius A\*, steady as
a rock, eternal. We go about our days; it’s always there.”

It’s been a wild week.
