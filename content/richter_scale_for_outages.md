# A Richter scale for outages

[I tweeted this
morning:](https://twitter.com/genmon/status/575928215530835969)

Increasing reliance on invisible centralised software. Recent Apple outage,
recent HSBC/contactless/tube outage. How long before a big one?

And I guess what I mean is that we’re all using these _same_ software systems.
And they interact in ways that are totally emergent. So they go down in
unpredictable ways. I feel like these systems are not resilient… for example,
the credit card system is less resilient than a distributed payment system
like cash.

It got brought to my attention because for, about a day, I couldn’t use my
HSBC contactless card on London tubes or buses – who knows why. I had to top
up my separate Oyster card, and it ended up costing me a couple quid more that
day. Then, yesterday, several of [Apple’s
systems](https://www.apple.com/uk/support/systemstatus/) were down for about
12 hours: Main effect for me, I couldn’t listen to any music in iTunes.
Nothing major.

But as [software eats the
world](http://www.wsj.com/articles/SB10001424053111903480904576512250915629460),and
as the Internet of Things brings more of the physical world into that same
domain, I think it would be helpful to have a language to talk about this.

So I made some notes on the bus.

Like the [Richter magnitude
scale](http://en.wikipedia.org/wiki/Richter_magnitude_scale), each magnitude
is incrementally ten times bigger. So 4.0 is 100x bigger than 2.0. But like
[apparent magnitude](http://en.wikipedia.org/wiki/Apparent_magnitude) it’s
subjective: The scale of the human effect is taken into account.

Here’s what I reckon the scale might look like.

**Less than 2.0.** Not distinguishable from normal network noise, like a call
dropping, webpage not loading, or a computer crash.

**2.0.** Facebook down, Gmail down, Apple App Store down, HSBC contactless
cards not working on London transport. Duration of shorter than a day.
Underlying problem is probably a single component and lack of resilience (e.g.
power outage at a single cloud hosting location). Fixable.

**4.0.** Minor network freeze but can be recovered with a reboot; broad human
inconvenience without threat. e.g. regional ATM network down for a day,
cellular network down for a day for single operator.

**6.0.** Collapse of minor network requiring rebuild. e.g. recent Sony hack
that meant no computers, printers, or existing network infrastructure could be
re-used without manual check of each item.

**8.0.** Major network freeze, can be recovered with time or reboot; major
human impact. Examples include the [2008 credit
crunch](http://www.economist.com/news/schoolsbrief/21584534-effects-financial-
crisis-are-still-being-felt-five-years-article) where bank lending gridlock
precipitated the global financial crisis; power network outage major enough to
require [black start](http://en.wikipedia.org/wiki/Black_start); the
[Icelandic volcano that grounded European flights for 6.5
days](http://en.wikipedia.org/wiki/Air_travel_disruption_after_the_2010_Eyjafjallajokull_eruption).

**10.0.** Major network collapse, global and unrepairable. e.g. Cascading,
emergent fault that wipes Internet routers and shuts down power grids, traffic
and logistics, internet and non-cash payment. Can only be fixed by re-
programming and re-architecting all separate components.

So the questions this makes me asks…

Is there a more objective way to measure system outage magnitude? Can we also
measure resilience, with a language that cuts across different systems? Is
there an equivalent scale for non-software system outages, like would [Gulf
Stream switch-
off](http://en.wikipedia.org/wiki/Shutdown_of_thermohaline_circulation) be a
8.0? Are we really going to see more software-related [black
swans](http://en.wikipedia.org/wiki/Black_swan_theory) over the coming
decades?

How long before the big one?
