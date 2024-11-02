# Protocol Fiction, Desire, and Belief

_I was invited to speak to the cohort of the[Summer of
Protocols](https://www.summerofprotocols.com) research program, and took the
opportunity to build on last year’s essay about **protocol fiction** and think
about adoption and the links with design fiction._

_(Summer of Protocols is an 18 week program to explore, catalyse, and broaden
the discourse around protocols.[Here’s the
cohort.](https://paragraph.xyz/@protocolized/introducing-the-summer-of-
protocols-cohort))_

_The session was a talk, workshop, then afterparty discussion._

_The essay version of my talk follows. I’ve added some notes from the
discussion at the end._

How could you end up with new infrastructure, such as a national drone
delivery network, or an ecosystem of biannual health checks based on MRI and
AI – _without_ being a government or a giant corporation?

One answer is to grow like the internet.

First you imagine a future network of actors with aligned incentives.

Then you define a **protocol** that explains how to work together, even when
the network is tiny, with incentives for non-actors to join the actor network.
(When ARPANET launched it had 4 nodes.)

_(A certain kind of protocol is a technology of cooperation, and I’ll use it
in that sense here.)_

A couple potential benefits of a protocol are

But the challenge is getting started.

So last year I wrote about [protocol fiction for speculative
infrastructure](/home/2022/08/11/casi), and the point of that fiction is to
articulate

Today I want to talk about belief and desire.

I was taken with this cybernetic description of an aircraft factory from sci-
fi author Bob Shaw (in his collection _Tomorrow Lies in Anguish)._

An aircraft factory is a machine for producing aeroplanes and it may be
disastrous to attempt to improve production by piecemeal tinkering with
individual departments - one must seek out in all its ramifications, and
destroy, the machine for stopping the production of aeroplanes, which lurks
like a parasite within the organisation.

It shifted my pov. I can now imagine that a system - a factory, an
organisation, an ecosystem - is autonomous, its own entity, and I am there to
facilitate and to garden.

In the protocol world, one of the best practitioners of ruthlessly rooting out
stop-energy is Dave Winer, creator of both RSS and podcasting – which wasn’t
just protocol design but also community/network bootstrapping.

Winer distilled his lessons into this typically straightforward, classic
essay: [Rules for standards-
makers](http://scripting.com/2017/05/09/rulesForStandardsmakers.html) (2017).

There are 18 rules. I’ll pick out 8.

It’s worth a close read. The first rules are about creating belief: working
code, social proof, etc.

Then the later ones are about reducing friction.

What I think Winer doesn’t say (because he’s so good at it, and therefore
takes it for granted) is that you also have to create _desire_ and a kind of
_gregarious desire_ – people have to easily see the value and want to get
involved! And they have to tell their friends!

The final rule, "praise developers," is a nod to that: positive feedback and
imitation is part of human nature.

So how should we think about desire with specs and protocols?

The practice of Design Fiction (as established by Julian Bleeker) is
responsible for all kinds of very public, charismatic visions of the future.

Design fiction is the deliberate use of diegetic prototypes to suspend
disbelief about change.

Kickstarter videos: they follow the aesthetic tropes of design fiction. _(My
favourite is[Disco Dog from
2015](https://www.kickstarter.com/projects/prtyny/disco-dog-the-smartphone-
controlled-led-dog-vest) – once you see the dog in the context of the street,
it’s so real, it’s so compelling…)_

There’s something about a gorgeously shot prop in its context of use that
makes you trust and want enough to open your wallet.

Of course that’s not all design fiction is. To unpack how it works as a
practice and its wider effects, I recommend Matt Ward’s essay [Design Fiction
as Pedagogic Practice](https://medium.com/@matthewward/design-fiction-as-
pedagogic-practice-9b1fbba7ae2b) (2013). _(I first encountered the deliberate
use of fiction in design because of Ward,[back in
2006](/notes/2006/02/scifi/).)_

To highlight just some of his points:

What I take from this is

Design operates in the market. The ability of artifacts to persuade is what we
want.

A protocol network, same same!

Hence protocol fiction.

I’d like to add something:

Material artifacts have an ability to _enroll and align_ different tribes in a
way that text doesn’t. The goal is to make _“boundary objects”_ \- artifacts
that self-translate for all kinds of different tribes, and allow these actors
to communicate with one another, even when they’re speaking different
languages.

Think of the magical role of self-evident prototypes to align engineering,
designers, users, MBAs, and so on. Like that, but projected into the future.

I should give the origin of these terms I keep using.

At the bottom of internal phenomena, whatever they are, the analysis pushed to
the limit will never discover more than three irreducible notions: belief,
desire, and their point of pure application, pure sense.

– Gabriel Tarde, La croyance et le desire (1880)

I haven’t forgotten them since [I first heard
them](/home/2012/03/08/belief_and_desire).

Steven Shaviro has written about [the sociology of Gabriel
Tarde](http://www.shaviro.com/Blog/?p=203) (2003).

Tarde denies the existence of higher-level entities … There is no such thing
as social laws and regulations, social norms, social impositions. There are
only power relations among individuals. Certain individuals impose on others;
certain individuals are imitated by others. Social coherence is merely the
result of imitation on a mass scale, together with raw power impositions.

And:

By a similar argument, it cannot possibly be the case that all hydrogen atoms
are uniform and interchangeable. _The only explanation for the apparent
uniformity of nature is that one particular hydrogen atom dominated the
others, forced them to obey it, or induced them to imitate it._

And:

_The ultimate motivating forces that move all of the world, whether human
beings in society, thoughts in a single brain, or hydrogen atoms in a gas, are
according to Tarde belief and desire. There’s nothing else._ Rocks and stars,
indeed atoms themselves, believe and desire just as we do. At the other
extreme, things like ideologies and customs and social classes and
bureaucracies can be explained merely as statistical aggregations of
particular beliefs and desires, amplified by mass imitation.

[(Also quoted here.)](/home/2012/04/30/belief_and_desire)

I find this such a brutal and mind-opening lens.

Beyond _thinking through making,_ this is what protocol fiction must achieve.

So I want to show three levels for building belief and desire, at different
scales.

The story of Stripe, the internet payments platform, was told in Businessweek:
[How Two Brothers Turned Seven Lines of Code Into a $9.2 Billion
Startup](https://www.bloomberg.com/news/features/2017-08-01/how-two-brothers-
turned-seven-lines-of-code-into-a-9-2-billion-startup) (2017). The reported
valuation today is $50bn.

I remember those lines: "all a startup had to do was add seven lines of code
to its site to handle payments" – it was neat!

The more jaw-dropping moment, for me, was when they were still called
_“/dev/payments”,_ and half of their page was given over to this:

`curl https: //apa.devpayments.com/api \`  
`-d method=execute_charge card \`  
`-d 'card[number]=4242424242424242*' \`  
`-d 'card[exp_month]=10' \`  
`-d 'card[exp_year]=2011' \`  
`-d amount=300 \`  
`-d currency=usd \`  
`-d identifier='hello world' \`  
`-d key=rNY2NaOyVo75otcS0M72NjscobfRMM`

You pasted it into your Terminal… and immediately received a token for (test)
cash in your account.

Instantly:

So what’s the smallest way to have that kind of experience?

Back in the 1950s that was a belief - or rather a common and unstated
understanding - about humanity’s future in space.

To me, there’s a big role for sci-fi’s established future history, the
Consensus Cosmogony, [summarised here](/home/2015/02/02/consensus_cosmogony):

When people were sent into orbit, and then landed on the Moon, this was
confirmation that we were on the path - if step 1, then steps 2 through 9,
right? And it’s _exciting!_ We _want_ it to happen. That was the role of the
sci-fi stories: propaganda creating desire.

Activities become easy when they align with a social consensus. Once
established, you don’t get stop-energy from doing something that matches this
future.

Then given the Brownian motion of society, we collectively tend towards that
future.

(Think of Moore’s Law as another Schelling point in action.)

There are other social consensus futures: nuclear apocalypse, climate change…
(I wrote in 2022 about [the story becoming
destiny](/home/2022/02/09/apocalypsi).)

It’s interesting that, as wild as the Consensus Cosmogony is, what makes it
work is that there’s a pathway and the Space Race gave it plausibility. Belief
as well as desire. It’s not enough to just imagine and articulate a future,
you have to show there-from-here, at least so evangelists can hand-wave it.

So: how do you give people a picture of the future? And how do you provide a
plausible pathway there – with your protocol (or whatever) becoming a both
required and inevitable step #1?

Another way of looking at this is that you need different types of activity,
and not everyone is specialised at doing all of them.

In Kurt Vonnegut’s _Bluebeard,_ the character Paul Slazinger writes a book:
_“The Only Way to Have a Successful Revolution in Any Field of Human
Activity.”_

Slazinger/Vonnegut puts forward that you need a "mind-opening team" of three
sorts of specialists:

[Full transcript here.](/home/2003/01/22/the_following_is)

It’s not as obviously belief and desire but, I think, it’s a similar light on
these different functions that are required.

Propaganda sounds like a dirty word, as does “advertising” to some people, but
my favourite piece of persuasive design fiction probably _ever_ is this Zurich
tv spot from – well I don’t know exactly but it was uploaded to YouTube 17
years ago.

**WATCH:** [Because Change Happens, Zurich TV ad from
2006](https://www.youtube.com/watch?v=s-ktjF2bXIo) _(Youtube, 1 min)._

It’s a collection of short scenarios made mundane by being shown incidentally
in an entirely believable near future:

(Just as wild, in the minds of the advertisers, is the idea of old people
snowboarding. Only 17 years ago!)

[Here’s a second ad](https://www.youtube.com/watch?v=V5UvMZyQrnY) with
vignettes including auto-inflating fall protection jackets for construction
workers, and people in suits caring about mental well-being.

And I do wonder: would there have been _any other way_ to get salespeople,
management, analysts, and partners thinking about algorithmic insurance for
robot cars (which is now a thing) in the early years of the 2000s?

This is belief, desire, and material artifact as boundary object, all wrapped
up in one. (Though I think we kinda have a growing immunity to video nowadays.
Working code is better.)

So if I could list some challenges for the designers of protocols, it would be
to sit and imagine how to do the following - in ascending level of scale:

Today let’s think about the first challenge only.

Maybe, as an exercise:

Whiteboard these using [tldraw](https://www.tldraw.com) _(go to the menu in
the top left and hit File > New shared project. Then everyone can work on the
same URL)._ And we’ll come back to discuss in 15 minutes.

I’m not going to do a full write-up of the workshop here, except to note a two
ideas that stuck in my head:

Well done to all four groups!

And from the discussion:

Not all design is the same. Some design is about meeting a need or a user
goal. **But some design is normative.** It is design for the world as it
should be, not as it is. Design fiction fits in the world of normative design.

Protocol fiction too.

To riff on Ward’s framing, the _Summer of Protocols_ is inherently ideological
and protocols, as a technology of cooperation, if they are intended to grow,
are evangelical.

So unpacking **desire and belief** , and then manifesting it, will be, I
believe, part of the story of this summer program, if the researcher cohort is
to achieve its goals.

Thank you for inviting me.
