# Who could write protocol fiction for speculative infrastructure?

Writing protocols for fictional big systems might be a neat way to unlock the
future. But I wonder who you would need in the room to author the spec.

To be more concrete about this, here are two ideas I’ve posted about before.
How could they be bootstrapped, short of being a giant benevolent corporation?

These are both ecosystems that provide infrastructure by harnessing market
forces. Get it right, and the incentives align towards getting cheaper,
better, and more accessible.

So… the internet works? How did that start?

In 1969, the proto-internet ARPANET had four nodes, and it used gateways and
the then-new technology of packet switching to transport data between remote
computers _run by different people._ It was a network built to be extended.
And it was.

The transport protocol was the bottom layer; higher up was the application
protocol: how does software speak to remote software in a standard way. Given
standards, the types of applications can flourish too. _Permissionless
innovation_ we call it now – how can you do new things without hitting
coordination problems.

_Two-Bit History_ has two fantastic articles about ARPANET:

_Lessons:_

Protocols are just agreed ways to communicate. A protocol embodies an
architecture of participation. They’re the lynchpin!

To start with there’s an enabling, base protocol which allows for (a)
cooperation, (b) expansion, and (c) more protocols to be layered on top. For
there it’s an iterative process as the network and its use cases grow.

To bootstrap this, a _“minimum viable network”_ is created by a single
organising body. It was BBN, under contract from ARPA, that built the enabling
gateway computer (the “IMP”), and also developed its software – which included
the first version of the protocol stack.

But before all of that: there’s a vision of what kind of big system is to be
developed. There’s a viewpoint of how the network will grow, and what it will
be used for. I _think_ this viewpoint was developed and espoused (in the form
of funding preferences and memos) by inaugural IPTO director at ARPA
(1962-1964) J. C. R. Licklider. Though to check that assumption first I need
to work my way through M. Mitchell Waldrop’s biography [The Dream
Machine](https://press.stripe.com/the-dream-machine), now published by Stripe
Press, currently glaring at me from my bookshelves.

Applying the lessons:

When I’m thinking about a nationwide drone delivery network, or MRI-enabled
medical screening ecosystem, it’s a coordination problem, right?

It would be in everyone’s interest to have these kind of big systems, but it’s
in no-one’s interest to go first. It wouldn’t - for example - be in Amazon’s
interest to build out a delivery drone network onto which everyone can
piggyback. That’s a catalyst problem.

In broad brushstrokes then, we want a process like this:

The protocol is where the rubber hits the road. It’s a description of the
future, and a proof of the potential economics. If done well then funding the
prototype should be a relatively straightforward public infrastructure
decision – although there may need to be policy whitepapers to communicate the
cost/benefit to government…

INSPIRATION:

In the adjacent world of software, **Robin Sloan** has been considering the
problems of Twitter and social media - everything from the doomscrolling user
experience to the failure modes of centralisation - and has come up with a
vision of something new.

But he hasn’t built software. He has designed a protocol: "What follows is a
narrative description of a protocol that I believe might open up some
interesting new possibilities on the internet."

In depth!

Spring ‘83 is a protocol for the transmission and display of something I am
calling a “board”, which is an HTML fragment, limited to 2217 bytes, unable to
execute JavaScript or load external resources, but otherwise unrestricted.
Boards invite publishers to use all the richness of modern HTML and CSS. Plain
text and blue links are also enthusiastically supported.

(It’s enormously readable. Check it out.)

There’s a draft spec!
[github.com/robinsloan/spring-83](https://github.com/robinsloan/spring-83) –
and, since the ref was first published, various people have created various
implementations, also listed at that link, so you can use it too.

The thing is that, for an ecosystem, you do need many participants.

With the narrative description, Sloan created the catalyst. With the spec, he
solved the coordination problem.

_Let’s pretend_ we wanted to write the protocol for a nationwide,
interoperable, drone-delivery network.

Who would you need in the room to kick off that process?

Thinking out loud, you need expertise in at least these areas:

Anyone else?

(That’s too many people. So perhaps with the right economist, and the right
technologist, etc… You’d want a small group, I think.)

Output: a report with an imagined market, some kind of visualisation, a
designed and documented protocol, a costed approach for the prototype build,
and a wrapper for all of the above to carry it into the right audiences
(public sector; VC; etc).

_Ahead_ of that, you would want probably want to kick off discussions with a
pool of people who are both open-minded and also well-networked in the above
areas, in order to iterate to the right group members.

And _beyond_ the delivery of the above protocol fiction etc by my new
Committee for Actualising Speculative Infrastructure, an organisation to carry
the ball forward.

Back in 2020, I spoke at ThingsCon about wanting to [work at imagining beyond
design fiction](/home/2020/12/11/thingscon):

But we don’t need just design fictions. We need business model fictions,
engineering feasibility study fictions, _interop protocol specification
fictions_ , investment return fictions.

This is what I meant!

Although I seem to have drifted from protocol fiction to committee fiction…

But 50% haha-lol-what-if and 50% seriously: if we got half a dozen people
together in London sometime, who should be in the room?
