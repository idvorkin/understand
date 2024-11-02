# What about a national packet-switched drone delivery network

Maybe today’s focus on local road-based delivery robots is a dead end, and the
last mile logistics world should be looking at packet-switching drones
instead.

The [Paris pneumatique
poste](https://en.wikipedia.org/wiki/Paris_pneumatic_post) was "a pneumatic
tube message-carrying service that operated in the French capital from 1866."
It peaked at 30 million messages/year, and finally closed in 1984.

Why? There has always been a need to send short, quick messages (anything from
chatting to stock market updates). But the electric telegraph was congested,
and messages sent by road could be caught up in traffic.

_If you want to know more, check out historian[Dr Molly Wright Steenson’s
work](http://www.girlwonder.com/papers-articles). In particular her piece
**Interfacing with the Subterranean** (Cabinet Magazine, 2011): [Read it
here](http://www.girlwonder.com/blog/wp-
content/uploads/2010/04/SteensonM_InterfacingSubterranean_Cabinet_2011.pdf)
(pdf)._

Messages were small cylinders containing special postcard telegrams.

In 1931, _La poste pneumatique_ began to **automatically route** the messages
through the network.

The cylinders are propelled along the tubes pneumatically, ie by air either
compressed or depressed: they are either blown forwards or sucked forwards
from one office to another. The pressures come from compressors feeding groups
of offices; these compressors were originally simple heads of water, then
driven by steam engines, and finally by electrical machines. There are today 7
such installations, supplying pressure to 12 offices in the network.

For a long time the cylinders went from one office to the next where their
contents were sorted for the next stages of their journeys. Much time was
spent in the manual redirection of cylinders but, after experiments in 1931,
_automatic navigation was introduced using apparatus which could accept or
pass on cylinders according to the setting of electrically conducting bands
encircling the cylinders._

(Do read that article. It has some fantastic photographs of the cylinders,
complete with conducting routing bands, in addition to maps of the network.)

Now the idea of store-and-forward networking is not new (that is: take a
message, send it to an intermediate node, and then send it on).

But the introduction of automation in routing is exciting, and the next step
in evolution for this kind of message routing is [packet
switching](https://en.wikipedia.org/wiki/Packet_switching), which is the
foundation for the internet, and _that_ method wasn’t invented till 1966.
(Loosely: Packet switching adds the ability to break a message into parts, and
also “self-healing” routing where packets can adaptively avoid network
congestion.)

So on the one hand the Paris pneumatic post is a redundant technology.

But on the other, maybe it only became redundant because the kind of messages
it carried could be sent be other means. Maybe the underlying logic of a
packet-switched internet for atoms is still sound.

Anyway, here’s the bigger lesson I take:

If the telegraph is congested and the roads are busy, don’t optimise but
instead create new capacity by adding infrastructure.

Here’s an example of new infrastructure:

Way back in 2011, I heard about **Matternet,** a new startup based around
bring packet switching to the delivery world, using drones and smart
recharging stations that double as routes (drones have a relatively short
range). there was a write-up in _The Economist._

The plan is to build a network of autonomously controlled, multi-rotor
unmanned aerial vehicles (UAVs) to carry small packages of a standardised
size. Rather than having a drone carry each package directly from sender to
recipient, which could involve a long journey beyond the drone’s flying range,
the idea is to build a network of base stations, each no more than 10km (6
miles) from the next, with drones carrying packages between them.

After arrival at a station, a drone would swap its depleted battery pack for a
fully charged one before proceeding to the next station. The routing of drones
and the allocation of specific packages to specific drones would all be
handled automatically, and deliveries would thus be possible over a wide area
using a series of hops.

Use cases such as…

hospitals could send urgent medicines to remote clinics more quickly than they
could via roads, and blood samples could be sent and returned within hours. A
farmer could place an order for a new tractor part by text message and pay for
it via mobile money-transfer. A supplier many miles away would then take the
part to the local matternet station for airborne dispatch via drone.

It’s economic where infrastructure is not yet built out: "A case study of the
Maseru district of Lesotho put the cost of a network of 50 base-stations and
150 drones at $900,000, compared with $1m for a 2km, one-lane road."

So I had a look and they’re going strong!

[Matternet](https://mttr.net) has recently announced a partnership with UPS in
the US to deliver prescription medicine. They’ve been building standardised
drones and standardised base stations. It all looks pretty neat.

As Benedict Evans has analysed, [e-commerce has seen a step change over the
pandemic](https://www.ben-evans.com/benedictevans/2021/4/25/step-changes-in-
ecommerce): In the UK, around 30% of relevant retail is now via e-commerce.
It’s _half_ if you exclude groceries. The picture isn’t as strong in the US,
but the trend line is still up and to the right, and the pandemic has
accelerated the shift.

[Another stat from Evans:](https://www.ben-
evans.com/benedictevans/2021/5/29/boxes-trucks-and-bikes) "A third to a half
of US (and UK) restaurant spending was actually ‘off-prem’ even before the
internet."

But the rubber hits the road with e-commerce, so to speak, with **last mile
delivery** ([as I’ve previously
discussed](/home/2020/05/28/grocery_shopping)). How stuff gets to your home.
And the two leading candidates have some not-so-great externalities:

We’re in a situation where the 20-30 year trend is clear, and technology might
give us a few years of rinsing our existing infrastructure, but ultimately I’d
argue that the solutions on the table aren’t up to it.

But maybe… Matternet?

We have the technology, so here’s what I would do, to prepare for 2050 and the
ongoing shift to e-commerce, from a policy perspective.

First: design an interoperable protocol for packet-switched drone delivery in
theory over the entire country. The protocol has to include how a drone from
provider A can recharge and route a parcel by landing at a station from
provider B, but _also_ how end-user billing and network peering fees work.

Second, partner with Matternet to manufacture the initial standardised drones
and routing stations. But make it clear that the cost of this is giving up a
monopoly position. Building out national infrastructure will require many
providers profiting and competing.

Third: allow neighbourhoods and local government to bid to be hooked up. For
roll out, each street needs to give up a single parking place for a delivery
drone routing station. Local houses can pick up parcels there; local shops can
send deliveries there. Existing logistics providers like Amazon can inject
parcels from dedicated stations. If there is network congestion, more stations
can be added. Long distance deliveries can be added in network upgrades and
trunk routing.

I don’t think an effort like this would work if left to the free market. I’m
not saying it should be nationalised, just that the state is a useful tool to
unlock the coordination problems. This would be a good task for the national
innovation agencies.

Deliveries are increasing. Current strategies won’t scale.

Infrastructure builds slow and then fast. ARPANET (and then the internet) was
4 nodes at launch in 1969; 100,000 nodes after 20 years in 1989 when the web
was first proposed; and a billion nodes 20 years after that – an efficient,
interoperating, exponentially-growing network for information.

My take: Now is the time to start work on the equivalent infrastructure for
the physical world.
