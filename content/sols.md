# A meander through Martian minutes and the meaning of local time

The Martian day is called a _sol_ and is approx 39.5 minutes longer than an
Earth day.

How will time work on Mars?

**You can keep the Earth system with more minutes in the day.**

In _Red Mars_ ([mentioned the other day](/home/2022/01/12/winter)), Kim
Stanley Robinson calls the extra minutes the _timeslip_ and makes it into
blank time after midnight: "Nadia had a sense that there was time for things
even though she was always busy, and the extra thirty-nine and half minutes
per day was probably the most important component of this feeling."

That strange pause on the digital clocks, when at midnight the figures hit
12:00:00 and suddenly stopped, and the unmarked time passed, passed, passed,
sometimes it seemed for a very long time indeed; and then snapped on to
12:00:01, and began its usual inexorable flicker; well, the martian timeslip
was something special.

But, to me, this is going to make cross-timezone Zoom calls really complex.

The top of the hour won’t be the same for everyone in the meeting.

So if you adopt Earth minutes then everyone has to use the same clock:
_Martian Coordinated Time._

But according to Wikipedia, lander missions don’t use this. They use
timezones.

Instead:

Each successful lander mission so far has used its own “time zone”,
corresponding to some defined version of local solar time at the landing site
location. Of the nine successful Mars landers to date, eight employed offsets
from local mean solar time (LMST) for the lander site while the ninth (Mars
Pathfinder) used local true solar time (LTST).

Because it’s handy to know something about the context of a lander or a
person, right?

If it is “8 am” for a person you automatically know something about their
context. It’s morning, it’s the beginning of their day, and so on. Without
timezones you lose that context.

But having the timeslip ultimately means having no timezones, so we need a
different solution.

**Mars hours, Mars minutes, and Mars seconds.**

From that same Wikipedia article, NASA stretches the units such that a Martian
day is 24 Martian hours long:

A convention used by spacecraft lander projects to date has been to enumerate
local solar time using a 24-hour “Mars clock” on which the hours, minutes and
seconds are 2.75% longer than their standard (Earth) durations.

Tricky for scientists living on Mars who need SI units. A future problem.

Makes sense if you’re on Mars itself, even for present-day landers.

But hard for the rover teams here on Earth. It makes calculating their shift
times complicated.

They know they’re on-shift at - say - 6am Mars time daily, but it’s hard to
tell what that is in Earth time.

Every day, team members are reporting to work 39 minutes later than the
previous day.

That’s from this article from the NASA Jet Propulsion Laboratory about the
Spirit rover: [Watchmaker With Time to Lose
(2004)](https://mars.nasa.gov/mer/spotlight/spirit/a3_20040108.html).

The solution: they made mechanical watches for the NASA rover team that
deliberately lost 39.5 minutes per day, so that the team could always know
Martian time without having to do mental calculations. People would wear two
watches.

_(Here’s another watch that shows Martian time, the utterly gorgeous[Mars
Conquerer MK1 by Konstantin Chaykin](https://chaykin.ru/en/historical-
masterpieces/marsconquerormark/).)_

That article found in this paper (which I can’t find online, sorry):

Seaborne, T. (2021) _Astronaut Watches for Mars: Personal Timekeeping on the
Red Planet,_ Journal of the British Interplanetary Society, 74(12), pp.
434-442.

…which also goes deep into the horology. Like, thermal and dust problems for
mechanical watches.

Anyway – even for something as distant as Mars, where the rover controllers
are sitting on Earth, it turns out that it’s super useful to know the local
time of the rover, and that’s important enough to make a whole new run of
custom watches. I hadn’t expected that.

We use time a little bit like available/busy/offline statuses in Slack or
WhatsApp. It’s a super quick way to get a first approximation view of
somebody’s context. Computers can take care of coordination and calendars, but
there’s no substitute for knowing someone’s local time.

When I’m on busy Zoom calls, I often wish there was a world map in the corner
displaying where everyone is located. Not (just) as a fun illustration, but to
give me a read on whether it’s late in the day and this person is doing us all
a massive favour by staying up, or it’s first thing in the morning and they’re
full of beans. Or - better! - somehow we could have a live read of how
caffeinated everybody is.

We should make a bigger deal, in email and Twitter and so on, about the local
time a message was sent, now we have global remote teams spread across
timezones. Was this a random late night idea, or a mid-morning considered
suggestion?

When you work with artificial intelligences [like
GPT-3](/home/2020/09/04/idea_machine) there is the concept of _temperature._

[Here’s a brief explanation of
temperature](https://ai.stackexchange.com/questions/32477/what-is-the-
temperature-in-the-gpt-models) in token generation _(Stack Overflow):_

If the temperature is low … the model will probably output the most correct
text, but rather boring, with small variation.

If the temperature is high … The generated text will be more diverse, but
there is a higher possibility of grammar mistakes and generation of nonsense.

So temperature is _kind of_ like creativity, but also like randomness, and
also like how much effort was put into searching outside the local maximum.

We’re going to be working more and more with AIs, which will be generating
text for us, or images, or solving problems (like: “design a webpage according
to this description”), and it would be useful to have the _temperature_ tagged
in standard metadata to every piece of generated content.

Seeing it would help me assess the intention! Like, is this just a proposed
solution, or is it a random whatever?

Temperature for AIs is like local time for humans.

Local time as empathy and provenance. A tiny bit of context that gets carried
with the message. So much of what we do online gets disconnected from its
origins and floats free – and then we get [context
collapse](https://www.rewire.org/context-collapse-online/) and all the
awfulness that goes with it.

Perhaps a single digit context number should be attached to every single file,
interpretation up to the user, and should always have been from the dawn of
computing, as intrinsic as the owner user ID, or the filename, or the last
modified time. But keep the times in the local timezone, not UTC.

_local time = 19:43_

_temperature = 4_
