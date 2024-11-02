# Local streets for local people

I wonder how we can implement the social contract via technology, and how that
can be done democratically.

A case study to explain what I mean…

One of the slow controversies in London over the past year has been the Low
Traffic Neighbourhoods (LTN) programme: closing many residential streets to
road traffic, sending cars onto main roads instead. [There’s some background
here](https://www.centreforlondon.org/blog/low-traffic-neighbourhoods/)
including how it was built out of a schools-focused programme during the first
lockdown (streets outside schools and on regular walking routes were closed to
cars).

LTNs are a joy and a pain.

The future of the city involves fewer cars, we all know that. Walking on these
quiet streets and having coffee in the parklets now built outside cafes is
transformative. BUT the schemes channel cars onto already congested main
roads, and semi-local trips that aren’t well served by buses are made much
more difficult.

Jimmy Tidey’s brilliant research has shown how [LTNs kicked off a culture war
on Twitter](https://jimmytidey.medium.com/how-have-low-traffic-neighbourhoods-
ignited-a-culture-war-on-twitter-676338205084) – though catalysed by a
relatively small number of vocal black cab drivers. There are posters in
almost every local shop against LTNs and they’re often vitriolic. I spotted a
banner headline, "All Streets Matter." Breathtakingly tin-eared.

For me, the root of the vitriol is that two constituencies of people feel it
is _unfair._

The problem is exacerbated by technology. The LTNs are often in effect for
only some of the day, so the street isn’t physical blocked. The closure is
implemented by a road sign, cameras with automatic number plate recognition,
and penalty fines sent through the post. One of my neighbours has been stung
by a series of 65 quid fines, having sailed through computer-closed streets
accidentally a number of times. So, poor software.

But technology is also perhaps part of the solution!

Long term we’ll have self-driving cars. We won’t need to close streets with
bollards and impose fines – the cars can be programmed. The Low Traffic
Neighbourhood policy will be a software point release.

So let’s think about how to bias that future pathfinding algorithm for
_fairness._

Perhaps what we’ve identified is that local people have more “moral right” to
use their neighbourhood roads than people from across town who are using the
street as a shortcut. Those people from across town feel like freeloaders:
they’re taking the benefit of the cut-through but they don’t have to live
here.

(Something similar happened in Los Angeles when Waze became popular. People
went to extraordinary lengths to protect their local streets by fooling the
Waze maps. [As discussed here](/home/2020/12/16/semiotarchy) in December
2020.)

Could we say that fairness means: local streets for local people?

What if we had some way of categorising roads on a spectrum from small (local
and residential) to big (thoroughfares)? If you live within 1 mile of a small
road, it’s free to use. Over a mile, it’s thoroughfares only or you get a
penalty.

The existing Low Traffic Neighbourhoods would see some cars again, but traffic
volumes would be low: the streets would be closed to any car from outside the
local area.

Ok, as a thought experiment that works for the future. NOW we can ask about
how to implement this _without_ waiting for robot cars. Could LTNs be
implemented in software today?

From a product perspective, the answer is yes.

Let’s imagine we have multiple routing modes in Google Maps. Perhaps the
different algorithms are embodied as different characters, just like [each
ghost in Pac-Man embodies a different search
algorithm](/home/2020/09/07/algorithms). (I’m picking on Google Maps but I’m
using this as a stand-in for all routing apps.)

In addition to the “quickest” mode, and the “most fuel efficient” mode, there
would be “social contract mode” – which would be the default. This mode would
avoid residential streets outside a 1 mile radius of your home or 0.5 miles
from your destination. _And it would be the default._

Through legislation, “social contract mode” for map routing would be mandated
for all in-car navigation from 2026.

Sounds plausible. The question then becomes… how could a policy like this get
enacted? Three challenges:

I don’t know the answers to these, but the utility of having a specific case
study such as Low Traffic Neighbourhoods is that we have something concrete to
debate.

London traffic is a specific case of something general and important, which is
how society uses technology to enact its values, and what the mechanisms and
limits on this should be.

Another instance of the general problem is Facebook’s engagement algorithm.
Can society really tell Facebook how to tune its systems for chasing
engagement, given that the ad-supported model requires it? Can we _really_
insist that Facebook puts a cap on engagement, reducing its profit margins, or
even changes its business model to include paid services – which will reduce
accessibility?

I mean, yes we can and should be having that debate. The extremism caused by
Facebook’s algorithms can be seen as a public health problem and, if that
analogy holds, I can point out that we’re perfectly happy to tax the cigarette
companies without outright banning them. ([Paying for externalities is one of
the uses of tax.](/home/2021/02/02/vice_taxes)) So maybe the same approach
should be adopted with Facebook.

But the question is the same: how should the desired social outcome be
expressed _as a technology product requirement,_ and how can it be expressed
in law?

There are social values baked into software already. We need democratic ways
to tune the parameters.
