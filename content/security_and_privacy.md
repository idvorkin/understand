# Security and privacy, startups, and the Internet of Things: some thoughts

Upcoming event in London: I’m going to be speaking about _the Internet of
Things, security, and privacy_ with [Sarah Gold, CEO of
IF](https://sarah.gold)at [Machines Room](https://machinesroom.co.uk) (an
awesome east London makerspace), _tomorrow._

**Insecure Futures: Privacy, Security and Connected Devices** (Weds 1 Nov,
6pm): [RSVP here.](https://www.eventbrite.co.uk/e/insecure-futures-privacy-
security-and-connected-devices-tickets-38504445834)

The event is part of a series of panels curated by Machines Room and
**Kickstarter**. Sarah and I will be doing this as a “fireside chat.” Should
be thought-provoking – these are some chewy topics, and Sarah is an expert.
[Her consultancy](https://projectsbyif.com) researches trust, policy and
design for clients with Google and Facebook with output both practical and
speculative.

We’ve each been asked to spend 5-10 minutes at the beginning of the session to
_set out our stand,_ so to speak. So this is my current draft on what I’m
going to say. Comments welcome; I’ll evolve it some before speaking.

**On IoT, security, and privacy. But security first:**

Let me say a few words about security first. Then privacy.

And really, because we’re talking about the Internet of Things, we’re talking
about the security of a device in people’s homes and in businesses, what we’re
talking about is the security of data and other devices on the trusted
networks in those places.

With my investor hat on, a startup that doesn’t take security seriously is
obviously a problem because it’s saving up problems down the road – it will be
harder to acquire, and it has the potential of being part of something
catastrophic.

For me, one _tell_ around this - a technology red flag - is when companies
build their own stack themselves for secure connection of devices to user
accounts (called provisioning), or for performing over-the-air (OTA) updates.
These two are bellwethers: if something isn’t right here, it’s likely that
security hasn’t been considered elsewhere in the stack.

It’s easy to convince yourself, as a startup, that there is no solution out
there that meets your needs for provisioning and updates. But over the last 12
months, the technology stack for connected devices has matured. And honestly,
these stacks come with features that you will never get round to building
yourself. So it’s worth looking for existing solutions.

[resin](https://resin.io) is an interesting example of a useful stack. One of
the things _resin_ makes easy is over-the-air updates for device software. But
because some of their users run this software for drones, they _also_ include
a feature that allows the drone to postpone the software update until it has
safely landed. That’s a useful feature. Let’s say you’re building a cash
register: it would be great to have a feature where it can postpone updates
till after the lunch rush is over. That’s the same thing. But will you get
round to building it yourself? Probably not.

So building your own stack is hard to get right, and more importantly it’s
expensive to keep up to date. Over months, as the technology landscape
evolves, a resource constrained startup may find itself lagging. And that’s
where security problems emerge.

Building your own artisan stack feels like an expensive indulgence in most
cases. The line to keep in mind is Werner Vogal’s maxim - Vogal the CTO of
Amazon - his maxim of "no undifferentiated heavy lifting." That is, don’t put
significant engineering resource into stuff that isn’t your core business.

But security isn’t just technology. It’s design.

It’s what you encourage users to do. A friend of mine in San Francisco had
some smart lighting and smart plugs some years ago. It has this great feature
where if you’re on the same wi-fi network, it automatically associates the
devices with your app so you can control them. And then, even when you’re not
on the network, you can turn the lights on and off. Handy.

So some months after staying with my friend, I discover - from London, while
demoing the app - that I can turn on the lights in his front room. I discover
this because he texts me, after I’ve been doing this for some weeks, to ask if
it’s me turning on and off his lights at 4am. Yes, yes it is.

Of course I reckon with this power I can possibly start a fire. Lights on and
off as quick as possible. No security stack is going to help. But thoughtful
design can.

_However._

The tension for startups is that design for thoughtful design, and therefore
for good security requires you to know what your product and service is doing,
but in the early stages you may have to change the product quite a few times
to get it right.

Now you think I’m going to say that this is a difficult decision, blah blah
blah, that startups should consider security early on, despite this.

I’m not going to say that. I’m going to say that maybe a startup should
_ignore_ security, just a little bit.

What I mean is: if I meet a startup who has spent ages on its security, pre
getting some real customer traction, I am going to be nervous that they have
over-engineered the product, and won’t be able to iterate. The product will be
too brittle or too rigid to wiggle and iterate and achieve fit.

So it’s a balance.

**Privacy:**

One of the reasons that security matters is because it can lead to privacy
being violated. Or rather, let me clarify:

Poor security can mean a startup’s customer gives up privacy in an
_unintended_ way. That’s going to damage sales.

But what’s more of a preoccupation to me is when privacy is reduced in an
_intended_ way. You see this a lot when a startup has figured out how to make
a business work by being not quite straight-up about what they’re doing with
the data they’re collecting.

For example:

You would be surprised how many companies like these I encounter. Or maybe you
wouldn’t be.

I think it should be a point of greater social concern that consumers are
asked to consent to data retention and usage when _even the people collecting
the data_ don’t know what it may be used for down the line. Object recognition
and facial recognition is getting really good – but it wasn’t great or well
known at the point I subscribed to most of the services I now trust with my
data. Can it really be said I consented to this? So we need a better way to
discuss this, in society.

With a more commercial hat on I subscribe to the view that, in most cases,
[big data is not an asset, it is a
liability.](https://www.richie.fi/blog/data-is-a-liability.html) If it’s not
necessary for the business model, then it’s an expense to keep it secure. So
don’t keep incur that expense. For example, you don’t need to keep credit card
numbers to take payments. OIutsource it. You don’t need to move video to the
cloud to data to do image recognition – we have machine learning at the edge
for that now.

But mainly, I think about this: is it _skeevy?_

The tide has turned on privacy, just as it did for sustainability. For ages
being sustainable was something companies did just to feel good about
themselves. Now it’s both consumer expectation and good business.

With privacy? For B2B startups I feel that being privacy conscious is becoming
a differentiator and should be advertised as such. No potential business
customer will want to be associated with the risk of leaks, being hacked, or
potential damage to the brand from revealed “skeevy” behaviour.

It’s not a negative thing. There’s opportunity here too.

I want to end with an example which is [Hoxton
Analytics](https://www.hoxtonanalytics.com), a company I had the privilege of
working with at the [R/GA IoT accelerator](https://www.rgaiot.com) I ran
earlier this year. By the way, we’re running another one, and applications
close on **7 December,** just a few weeks from now. We can talk about that
afterwards.

Hoxton Analytics supply, for their clients, pedestrian footfall intelligence.
They count the number of people walking in and out of your shop.

Historically this has been done with infra-red beam interruption. Well, that
can’t track groups or whether people are going in or out.

So instead you can do it by tracking smartphone signatures. Information-rich
but not everyone has their Bluetooth or wi-fi turned on.

So you can really amp it up and monitor footfall with cameras doing facial
recognition: that doesn’t fly in Europe, it’s personally identifiable
information. Fine elsewhere in the world though.

Hoxton takes a different approach. They have cameras right down low on the
floor, and they use machine learning - on the device - to recognise shoes.

It’s crazy accurate. 95% accurate. It can also count group sizes, and whether
people are going in or out. So it can do capacity.

It also doesn’t store personally identifiable information so it’s good in
Europe.

But get this. Because they’ve built this solution, it means they can also use
it in public places. So you can point the camera out of the window and see how
many people are walking past, versus how many people are walking in. This is
the holy grail, like a conversion funnel, like Google Analytics, but for
physical retail. And they’ve got there by considering privacy not as a product
constraint, but as a product _feature._

**Wrap up:**

That’s where my head’s at regarding security and privacy. I’m going to chew on
these thoughts a bunch before the discussion with Sarah, and I’d welcome your
thoughts – either on my views as laid out above, or on questions to ask her.

I don’t know if there are any tickets left but if there are [do come
along](https://www.eventbrite.co.uk/e/insecure-futures-privacy-security-and-
connected-devices-tickets-38504445834) and if you’re already signed up, then I
look forward to seeing you on Wednesday night.
