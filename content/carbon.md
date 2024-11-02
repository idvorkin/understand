# What I have to say about carbon accounting in web browsers will shock you

**[Low-Tech Magazine](https://solar.lowtechmagazine.com)** is hosted on a
solar-powered web server. It has a battery backup, but it "will go off-line
during longer periods of bad weather." So there’s a page detailing [both the
battery level and the weather forecast in
Barcelona](https://solar.lowtechmagazine.com/power.html).

I enjoy imaging the physical location of the website! [From the About
page:](https://solar.lowtechmagazine.com/about.html)

Because it uses so little energy, this website can be run on a mini-computer
with the processing power of a mobile phone. It needs 1 to 2.5 watts of power,
which is supplied by a small, off-grid solar PV system on the balcony of the
author’s home.

(Photos are black and white and dithered, which further reduces energy; only
default fonts are used; there have been sensible, low-energy tech decisions on
the back-end.)

Another! **[Solar Protocol](http://solarprotocol.net)** (which cites _Low-Tech
Magazine_ in its library).

Solar Protocol is a web platform hosted across a network of solar-powered
servers set up in different locations around the world. A solar-powered server
is a computer that is powered by a solar panel and a small battery. Each
server can only offer intermittent connectivity that is dependent on available
sunshine, the length of day and local weather conditions. When connected as a
network, _the servers coordinate to serve a website from whichever of them is
enjoying the most sunshine at the time._

One of the collaborators on _Solar Protocol_ is the artist Tega Brain who gave
a wonderful and mind-expanding talk at _The Conference_ in Sweden last week.

It’s a presentation of her own work, a critique of _“systems thinking,”_ and a
probe into both AI and climate.

Watch the video here: [The environment is not a system by Tega
Brain](https://videos.theconference.se/tega-brain-the-environment-is-not) _(40
mins + Q &A)._ Highly recommended.

_Solar Protocol_ is provocative, for me, because the big tech companies will
of course already be behaving like this, shuffling compute around to where
energy is cheapest. (And it’s why Meta has server farms in the Arctic circle,
to take advantage of cheap cooling.)

BUT: for the rest of us? It’s interesting to imagine what underlying tech
would be required to allow for _any_ website to operate like this.

SOME IDEAS:

Could energy accounting be built into internet protocols?

Like: could a database query return, along with the results and the query
time, the joules burnt to produce the answer?

Could that query additionally report the location of its server, and a data
centre report the precise energy mix (% from grid; % from battery; % from
local renewables etc) supplied to that server at the time?

Can an API aggregate the energy spent for all its underlying queries, in the
return object including the total joules – which would also have to include a
calculation based on the CPU time to service the API call? And an amortised
slice of the embedded carbon of the data centre?

Ultimately: could a webpage include, in its HTTP response headers, all of this
data added up, every page returned to your browser with its joules shown
numerically right there in the tab?

Or as carbon footprint? Because that’s the goal, I think: a live view of the
carbon I’ve burnt today with my app swiping and web browsing, in exactly the
same way as I can tap the battery icon in my menu bar on my laptop and see a
list of _Apps Using Significant Energy._

AWS, Google Cloud, etc: do this please?

THERE ARE PEOPLE WORKING ON THIS!

And people to learn from: **[Branch
magazine](https://branch.climateaction.tech),** now 4 issues in.

A couple of favourite articles…

However in Switzerland, this idea of carbon awareness is being built into the
internet protocols themselves with SCION. …

This same flexibility also means that it’s possible to choose routes based on
how green the path to a destination is too - avoiding regions when the cost of
energy is high, and the power is dirty, or where there’s a scarcity of green
energy available.

Aha! A protocol to watch.

This article has some practical pointers for web engineers:

In order to meet the growing demands for reporting and transparency,
developers need a way to measure the carbon emissions associated with the
apps, sites, and software they build. On the server side, _we’re seeing more
providers build carbon reporting into their platforms_. However, on the
application side, it’s largely up to developers themselves to implement
solutions. _That’s where libraries like CO2.js come in handy_ , providing a
set of research-based, standard calculations that enable developers to quickly
add carbon awareness to their products and projects.

Good news on the cloud computing front, then.

_CO2.js_ has some intriguing implications:

In the same way that web developers might set a performance budget for their
site, a carbon budget could also be used. If a website or app exceeds a
threshold for carbon intensity, then an alert can be raised or a new
deployment can be blocked.

(The library comes from _Branch_ sponsors, the [Green Web
Foundation](https://www.thegreenwebfoundation.org).)

Action is the point, right? Acts not facts. We measure for

So measure at the server and protocol level first, and then allow service
developers to change their behaviour… and, eventually, expose the data to end
users?

More practical tips: see [This website is killing the
planet](https://visitmy.website/2020/07/13/this-website-is-killing-the-
planet/) _(Steve Messer, 2020)_ which has a bunch of tools and how-tos in the
_Further Reading_ section.

ALSO:

Not the same but with the same vibe:

[Should I Bake .com](https://shouldibake.com) (single-serving website).
Currently: "We recommend baking when more than a third of Britain’s
electricity is coming from wind, solar and hydro power – right now, between
19:00-19:30, it’s 24%."

_Wonderfully_ there is a multi-day **baking forecast** which shows me that I
shouldn’t bake until, ah, Saturday.

Relies on this new-to-me [Carbon Intensity
API](https://carbonintensity.org.uk):

The Carbon Intensity API uses state-of-the-art Machine Learning and
sophisticated power system modelling to forecast the carbon intensity and
generation mix 96+ hours ahead for each region in Great Britain.

Our OpenAPI allows consumers and smart devices to schedule and minimise CO2
emissions at a local level.

Brilliant.

Build this into my tumble drier!

Seriously. Samsung, Electrolux, etc etc: if current carbon intensity is higher
than average, make it so I have to hold down the Start button for like 2
minutes or something.

Make me work for it! Make me solve a puzzle before running my appliances when
emissions are above average. _Hey I’ve even got a name for that imaginary
feature: Carbon CAPTCHA._

(I should be able to get something working at home with smart plugs and a
Raspberry Pi… hmm…)

This is a temporary scenario!

Or at least, until I can get solar at home, which appears to be pretty much
impossible rn in the UK due to volume of interest.

BECAUSE: solar means energy freedom.

Clive Thompson:

I’ve stopped worrying about electricity use, both economically and ethically.

I no longer walk around finger-wagging at my family members. Want to blast the
AC? Crank away. It’s coming from the sun, and I can’t use all that electricity
even if I try.

The emotional shift: "I went from a feeling of scarcity to a sense of
abundance."

Can’t wait.

ANYWAY, what I really want is a new web browser with a built-in carbon
accounting odometer for all our Twitter doomscrolling (accrued in CO2E kg per
inch).

I want you to feel a sense of relief when you type a common query into Google
and the data comes back from the cache, dodging the expensive database
lookups.

Ask something weird and get a cache miss? YOUR COMPUTER SHOULD ELECTROCUTE
YOU.

Not too much, let’s be clear, just a little zap, a bit like an elastic band
twanging on the tip of your finger. Multitouch screens that can give you an
electric shock would have all kinds of uses for behaviour change I reckon.
