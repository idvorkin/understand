# I wish my web server were in the corner of my room

Back in college I used to run part of my website from a Linux box in my room.
I made it into a speech synthesiser, and people could connect to the machine
to talk into my flat.

_(Retrospective apologies to my flatmates.)_

This is way back in 2000 so before smartphones, and before texting, and before
always-on internet (college was an exception), and before camera phones or
being able to reliably email photos let alone video. Decent text-to-speech
still felt novel. We had a friend who was travelling in Australia at the time
and he would visit internet cafes and type in messages to talk to us. Of
course there was no way of talking back. It felt impossibly magical.

But what I remember feeling most magical was the idea that there was somebody
_visiting_ that server on my desk. There was somebody coming from a long way
away and going _inside._ An electronic homunculus.

I could hear the hard drive spin up if somebody accessed the machine, and a
little _chug-chug-chug_ while Festival (the open source text-to-speech engine
I’d installed) generated the voice. Like footsteps approaching before the door
opens.

I can have this experience again!

I was chatting with artist **honor ash** the other day.

Their [website](https://hnr.fyi) (and also [blog](https://thoughts.hnr.fyi))
runs on a Raspberry Pi sitting in a corner in their house.

This feels very important.

First there’s the feeling of _“I made that!”_ which leads to the feeling of
_“I can make all kinds of things!”_ You will definitely get that more when you
install the software on the web server yourself, and also when you copy over
your own hand-coded text files. (The web is just text!)

Then there’s the feeling that people are visiting and - the corollary - if
other people’s experience of your website is just in that tiny box, then
_your_ experiences of all _other_ websites are similarly physically located in
boxes too.

If you have a local web server then you can play music into your space.

Karey Helm’s old website, [back in 2015](/home/2015/02/26/coffee_morning):

…the portfolio on her website offers Party Mode. Click the button at the
bottom of the page, and mouse over the various projects - the page becomes an
instrument, it’s like a synth! And then, I swear I heard this right, when you
use Party Mode, there’s an Arduino in her studio that plays the music.

Once again I am desperate to have this for myself.

ALSO: [those solar-powered websites](/home/2022/09/01/carbon). I can totally
visualise the photovoltaics on the website owner’s balcony in Barcelona
whenever I read an article there.

_I will also say that it feels transgressive._

It is boundary-violating, to have a website in the corner of your bedroom.
Websites are meant to be in the cloud. Eternal, somehow, transcendent, like
the voice of code floating down from the sky. But no, there it is. It is real!
I can kick it! _Argumentum ad lapidem._

The discombobulated feeling is not new. Seeing a server felt weird even before
the cloud.

Julian Dibbell’s _My Tiny Life_ was written in 1998 about multiplayer text
adventures - early virtual worlds - and it is one of those books that has
abruptly become insanely relevant. Chapter by chapter it goes through identity
play (and abuse), cybersex, money, community governance, power, doxing, and
the odd existential self-obsessed angst that all online communities seem to
journey through.

The system in which Dibbell is hanging out is called LambdaMOO, and there’s a
passage in which he visits the server.

The_Author looks at The Server.

look server

The Server

You see a box as unremarkable as any other in this room, only more so. Three
feet square by one foot high, some cables slithering out the back, no
flickering lights or any other outward indication of activity within. The box
sits at about knee level, stacked unceremoniously on top of another one just
like it.

The_Author has come 3,000 miles to look at this machine.

(That link leads you to the full text, but you should [buy the
book](https://www.amazon.co.uk/My-Tiny-Life-Passion-Virtual/dp/1841150576/)
_(Amazon)_ and I don’t know just sit by the letterbox until it arrives and
then INHALE it.)

Dibbell is underwhelmed… and yet still holds onto his fantasy:

The_Author realizes now that during all those months he never really doubted
LambdaMOO was in this box, compact, condensed, its rambling landscapes and its
teeming population all somehow shrunk down to the size of The Server’s hard-
disk drive.

I can relate! I can relate!

Seeing your website’s actual server is the virtual equiv of the [Overview
Effect](/home/2021/07/20/overview_effect) and I want to have that feeling the
whole time!

I want to feel like my room is haunted by miniature cyberghosts whenever
someone reads my blog!

I want you to have that feeling too. I think it would change how we think
about the internet, in a grounding and healthy way. I think it would help us
regain a sense of agency and ownership, with which we would be way more
demanding of the sort of internet we want to live with, a sense that is
currently so distant from us that we have forgotten it is possible and can’t
even tell that it is missing.

So… practically: how to achieve this in 2022?

Having a Raspberry Pi serving a website at home is relatively straightforward
with a bit of work, I know.

But I would also like it to be reliable if I kick a cable out of the wall, or
in the unlikely event that I get a bunch of traffic. I’d also like it to be
quick!

Oh, and I don’t want to have my home network hacked.

Perhaps there’s a way to host my website at home, but have the static bits
served by Cloudflare if the Raspberry Pi isn’t available _(using a global CDN
as a UPS),_ and the dynamic bits always visit my home – but there’s a graceful
_“come back later”_ message if the Pi is down?

I’m pretty technically capable but I’m not sure I can be bothered.

There are so many things in the way. Getting a routable IP address at home.
Making it secure. Monitoring it. Gracefully stepping up and down from the CDN.

I would _love_ a turnkey way to home-host.

Here’s the BIG question: even if it works as above, it’s still a bit of a
hacky compromise to have my web server sitting on a shelf. How could it be
easier than a monthly rental fee for cloud hosting? How could it be _extra?_
Sure, ambient beats playing into my home office when somebody visits this
blog… but what else? There’s a project here.

**Update 12 Oct:**

This post made it to the top of Hacker News and stuck around for a bit.
Blimey, hullo! [Here are the
comments](https://news.ycombinator.com/item?id=33165836) (367 right now). Some
lovely anecdotes there. Here’s a favourite:

I had a URL on my website called moo.html that wasn’t indexed. My friends had
it bookmarked, and when they visited it they got a picture of a cow, but it
played a cow mooing in my bedroom. It was a nudge to come online and be
social.

That’s it! Mixing up the boundary between virtual and physical.

I don’t think it’s just nostalgia (that’s something that came up on Hacker
News and also the [replies on
Twitter](https://twitter.com/intrcnnctd/status/1579558673499951105)). It
should be _easy_ to have a publicly accessible webserver at home with a bolt-
on cloud-based load balancer in the event that I get a burst of traffic or my
home internet goes down. And there’s no reason that should be any less
reliable or straightforward than hosting in the cloud. There’s nothing
intrinsically hard about it.

(Clarifying what easy means: easy means straightforward tools that work well
together, and config files that keep the same format for a decade+. Command
line beats GUI because I can keep notes and config in git.)

Why? Because being in the same room as your server will open up new
opportunities. Playful ones at first and then… who knows what? My own
bookshelf Raspberry Pi [has an e-ink clock on
it](https://www.instagram.com/p/B_XYXJOJe3r/) so perhaps I’ll use that as a
little window to show me visitors.

Oh hey, I found my original blog post with the embedded form that spoke words
into my flat. The form doesn’t work now of course, but here it is for
posterity, [way back in May
2000](/home/2000/05/09/im_hearing_voices_in_my_flat).
