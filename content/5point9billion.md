# My latest Twitter bot: @5point9billion

**Backstory!** Exactly 12 years ago today, I made a little web toy called
_Light cone._ [It’s still
running:](http://interconnected.org/home/more/lightcone/)

From the moment of my birth, light (that I could have influenced) has been
expanding around the Earth and light (which could influence me, from an
increasing distance of origin) reaching it – this ever-growing sphere of
potential causality is my light cone. Today… My light cone contains 70 stars.
Zeta Doradus will be reached in in 2 months.

Remember RSS for blogs? The idea was you would subscribe to a live feed of
your light cone in your blog reader, and get a notification every time you
reached a new star. Now RSS is no longer the new hotness, but over a decade
later there are still about 500 people subscribed to that old web toy.

I enjoyed it as a tiny, cosmic, lovely thing. I included it in the words I
wrote in the intro to _Mind Hacks_ way back in 2004,
[here:](https://www.instagram.com/p/_RhWO7Kpch/?taken-by=genmon) "p Eridani,
hello!" It’s still great to look back, to see how far I’ve come.

So I figured, let’s drag this thing into the modern age, let’s move this thing
to Twitter. [(I’ve been making Twitter bots
lately.)](http://interconnected.org/home/2015/11/25/like_to_continue)

My new bot is called [@5point9billion](https://twitter.com/5point9billion)
which is the number of miles that light travels in a year. The idea is that
you follow it, tweet it the date of your birth (e.g. [here’s my starter
tweet](https://twitter.com/genmon/status/674333947405447168)), and then it
lets you know whenever you reach Aldebaran or wherever.

You get tweets monthly, and then weekly, and for the last couple of days… and
then you pass the star. It feels neat, don’t ask me why.

_(Aldebaran is about 66.7 light years away, so light reaching it today left
Earth on 1 April, 1949, on the day[Gil Scott-
Heron](https://en.wikipedia.org/wiki/Gil_Scott-Heron) was born. I won’t reach
it for almost another three decades.)_

The bot only tells you about _bright_ stars – stars you could see in the night
sky with the naked eye from rural areas. I figured it would be fun to hear you
were reaching Tau Ceti, and then be able to look for it up there.

_(Tau Ceti is 11.9 light years from Earth, so if you’re almost 12 years old -
born at the end of January 2002 - you’re touching it now. Hey and guess
what,[Tau Ceti has planets!](https://en.wikipedia.org/wiki/Tau_Ceti) I passed
Tau Ceti 25 years ago.)_

So yeah – my new Twitter bot! I’m testing it at the moment so there are rough
edges in the copy, and it might break. But please do give it a go.
[@5point9billion is over here.](https://twitter.com/5point9billion) You’ll
need to talk to it from a public Twitter account.

I haven’t made a habit of project write-ups before, but I’m taking an
increasingly “long now” approach to the tech I make and use. How will I
remember what I made in a decade? By reading this post.

If you just want to use the bot, stop reading now :) If you want to know a bit
about the underlying data, carry on.

My original web toy was based on a list of stars I found at [An Atlas of the
Universe.](http://www.atlasoftheuniverse.com) It was a little haphazard (I’ve
since discovered) but more importantly only went up to 50 light years. That
felt like a lot of headroom when I made the first version of this and I was 25. Now I’m 37 and 50 doesn’t feel so far away.

Better data required!

It turns out there are [dozens of astronomical
catalogues,](https://en.wikipedia.org/wiki/List_of_astronomical_catalogues)
all of them doing slightly different jobs.

In the end I found the [HYG Database](http://www.astronexus.com/hyg) which
combines three sources, it contains "all stars in Hipparcos, Yale Bright Star,
and Gliese catalogs" which is some 120,000 stars in total.

Of particular interest to me is the data from the [Yale Bright Star
Catalog](http://tdc-www.harvard.edu/catalogs/bsc5.html) which concentrates on
naked-eye visible stars. The HYG Database includes and tidies this up.

Then there’s the question of filtering down this huge number of stars.

First, filter by distance: There are some 4,061 stars listed within 100 light
years (well, star systems but we’ll get to that). But this includes objects
invisible to all but the most powerful telescopes.

So I picked a threshold – astronomical brightness is expressed in _apparent
visual magnitude,_ basically not how bright the star or planet or whatever
actually is (we can’t know) but how bright it looks from Earth. And this is a
brightness that peaks around 550nm, right in the middle of the visual range…
some stars are crazy bright in the infra-red but you can’t see them.

(550nm is yellow-green, chartreuse.)

Using [this magnitude chart](http://www.icq.eps.harvard.edu/MagScale.html) I
picked +4.5 as a cut-off (lower is brighter), which is between these two
descriptions:

+4.0: faintest naked-eye stars visible from many smaller cities/(outer)
suburbs +5.0: faintest naked-eye stars visible from “dark” rural areas located
some 40 miles (60 km) from major cities

Filtering by brightness: There are 181 objects in HYG closer than 100 light
years, which are also brighter than magnitude +4.5.

It’s arbitrary but that’s a decent number.

Then, data cleanup.

Our closest star system is Toliman aka Rigel Kent aka [Alpha
Centauri](https://en.wikipedia.org/wiki/Alpha_Centauri). In my filtered-for-
brightness HYG it has two entries: Alpha Centauri A and Alpha Centauri B.
Although Alpha Centauri looks like a single star to the naked eye, these two
stars can be seen separately with a 2 inch telescope, and they were first
spotted in December 1689.

But it turns out there’s also third star – Proxima Centauri. It’s dim, small,
and although 0.2 light years from the other two, it’s gravitationally part of
the same system. I’ve combined these entries.

Actually I’ve gone through all 181 objects listed and:

We’ve been naming stars for thousands of years. So most bright stars have
multiple names, and because Wikipedia is a product of the west, I mainly find
European or Arabic names of stars visible from the northern hemisphere.
Sometimes there are Chinese names given too.

I’ve picked my favourite names.

My pick is _purely_ subjective. I’ve mainly used the expanded version of the
abbreviated, disambiguated name given in HYG. For example, when HYG said
"52Tau Cet", I’ve changed that to Tau Ceti.

With others, I’ve leaned towards traditional names. In HYG: "35Eta Oph."
That’s Eta Ophiuchi, but I’m referring to it as Sabik. Of course there are
multiple traditional names, and to give you an idea of what the Chinese name
is like, [here’s what Wikipedia
says:](https://en.wikipedia.org/wiki/Eta_Ophiuchi)

In Chinese, this star is considered part of … Left Wall of Heavenly Market
Enclosure, which refers to an asterism (pattern of stars) representing eleven
old states in China that mark the left borderline of the enclosure …
Consequently, Eta Ophiuchi itself is known as Tian Shi Zuo Yuan shiyi,
English: the Eleventh Star of Left Wall of Heavenly Market Enclosure,
representing the state Song.

I’ve played silly buggers with the character accents there but you get the
idea.

Now I have to say, "the Eleventh Star of Left Wall of Heavenly Market
Enclosure" is possibly one of the most poetic things I’ve heard, but I’ve
picked “Sadik” as the name simply because it is more likely to crop up in the
books and movies I tend to encounter. As I said, subjective.

But you know what? Cropping up in books matters. I’m a fan of generation ship
novels in science fiction – [I keep a list of starship
names.](http://interconnected.org/home/2014/12/03/filtered) I also keep a list
of destinations…

It’s super neat to think that, when I was almost 12, my light was touching
Procyon, the destination of the ship _Big Dog_ in [Non-
Stop](<https://en.wikipedia.org/wiki/Non-Stop_(novel)>) by Brian Aldiss. [The
Dazzle of the Day](http://machine.supply/books/drewbuttons/92) by Molly Gloss
– _Dusty Miller_ is carrying a community of quakers to Epsilon Eridani. And
[Tau Ceti pops up all over the
place.](https://en.wikipedia.org/wiki/Tau_Ceti_in_fiction#Literature)

So the night sky gets richer with this tapestry.

One speed bump is this bot needs to know your birthday to function – and I’m
asking users to tweet their birthday publicly to start using it. I’ve been
asked a few times about this, isn’t it a crazy privacy problem?

Well I thought about having this configuration happen privately through DM,
but the thing is your birthday will leak anyway… the distance of stars is
public information, so when the bot says “passing Tau Ceti in 2 days,” that’s
a total giveaway. The birthday at the beginning is a hurdle, true, but it
makes people realise that their information will be public anyhow: It prevents
that fact from being a surprise later. I can set this expectation without
explaining anything, it’s implicit in the interaction.

_Actually the truth is my next bot is going to be all about first pets and
your mother’s maiden name, and it’s all a giant scam._

On the topic of setting interaction expectations implicitly:

You stop the messages by unfollowing the bot, and this is barely explained in
the help text. It’s an unusual interaction pattern: Most Twitter bots you can
use by tweeting at them, and they reply with whatever they have to say,
whether you follow them or not.

But this bot is more like a subscription, so I need a way for users to
“unsubscribe” that is intuitive enough so nobody has to guess what to do… I
don’t want people to report the bot to Twitter for spamming and have account
suspended.

I’m trying to build this unconscious understanding by making the bot almost
unusable unless you follow it. Everything steers the user towards following,
hopefully the equation becomes very clear.

@5point9billion is still in beta – on my list: a bit more copy, a couple more
simple features, management tools on the back-end.

Between this and my previous bot [(a poem called
@liketocontinue)](http://interconnected.org/home/2015/11/25/like_to_continue)
I’m gradually creating a system I can use to tell stories on Twitter. So who
knows what I’ll make next - I have a bunch of ideas in my notebook - but I’d
like it to be incrementally more complicated. As the complexity of what I can
do with my tools grows, so my imagination grows too.

Always up for collaborations. Let me know if you have any ideas.

But at the back of my mind is this… My previous version of this project has
run happily with minimal intervention for over a decade. The code that runs my
blog: That’s been running in various incarnations for almost 16 years. My
principle is to keep the code I write simple enough that I can rewrite it in a
day or two. It’s a decent way to future-proof.

The time I keep code running for is longer than the popularity of most
languages, of most “best practice” ways of building for the web, of the
platforms I use – RSS, say. Will Twitter be around in a decade? How about the
web itself? Is this bot simple enough that I could re-write it in a day or
two? No, it’s not. Not yet. It would be cool if it was.

I don’t know where I’m going with this.

Crossing the river by feeling the stones.

Hey, [@auchmill tweeted something
lovely:](https://twitter.com/auchmill/status/676141430767661056) "Funny, isn’t
it? I’ve never been so aware of my age, or made to feel so okay about it"

You can [follow @5point9billion over
here.](https://twitter.com/5point9billion) 198 people are already using it as
I write these words. If any of you are reading, hello!
