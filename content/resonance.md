# Selective capability impairment via resonant radio of pesky public chatters

I’m imagining a magic ray gun to surgically disrupt computers because I was in
a noisy cafe the other day and I’m still salty about it.

There were six people upstairs in this cafe in St Pancras, including me, and
each of the other five was talking a video call.

Now I feel like headphones in public places are weird anyhow because they suck
the energy: the headphone wearer talks and hammers at their keyboard and
radiates a foreign vibe without being subject to the vibe of the space itself.
They are obstinately there but not there? An anti-ghost. I don’t know how to
describe it. It seems selfish; opting out of the mutuality of co-presence.

I had underestimated _not_ wearing headphones. So one of the five didn’t have
headphones, and had amped up their volume so they can hear their screen, and
was yelling to their on-screen colleagues. Good grief.

I want to jam conference calls in public places.

There used to be this key fob thing called **TV-B-Gone.** It’s a one button
infrared remote control that universal turns off public televisions.

Hey [here’s the official website](https://www.tvbgone.com), you can still buy
it!

_(And it turns out it was invented in 2004 by hacker legend[Mitch
Altman](https://en.wikipedia.org/wiki/Mitch_Altman) who was also a virtual
reality pioneer.)_

And there’s a solid tradition of jammers: cell phone jammers exist but are
[illegal in many
jurisdictions](https://en.wikipedia.org/wiki/Mobile_phone_jammer).

But a cell phone jammer wouldn’t help me block video calls as people would
move to wi-fi. And I don’t want to jam wi-fi as people checking their email is
fine.

Maybe it’s possible to be more targeted.

Could you jam MPEG decoding itself?

Here’s my thinking:

[As previously discussed](/home/2018/01/16/filtered) (2018) it is possible to
make your computer broadcast just by running software:

Computers can now write to memory with a high enough frequency that it’s in
the radio spectrum. Now you’re hitting the RAM fast enough, you can play it
like a xylophone and carve radio waves into the air.

The MacBook Air 2015 demo code broadcasts _“Mary Had a Little Lamb”_ and can
be received by an old-fashioned AM radio tuned to 1580 kHz.

BUT: electrical resonance also works in reverse, right?

In chip design, there’s a phenomenon called _ground bounce_ and you have to be
very aware of lines that are not connected but are nearby.

I used to read _IEEE Computer_ magazine and I always remember this article
from 2003. There’s an analogy about sitting next to a friend on a swing set,
and toppling it by swinging at the same time, and a particular chip in 1985…

For the same reason that you and a friend could swing happily as long as you
were out of phase, these Advanced Schottky octal buffers would meet their
published specs if you sent [10101010] but not [11111111]. And you were doomed
if you tried sending [11111111] and [00000000] in a repeating pattern. …

In electronics education, wires are assumed to be perfect conductors of
electricity. Real-world wires exhibit parasitic capacitance to other wires,
and they also exhibit inductance. Inductance is the propensity of a wire to
create a magnetic field that accompanies any electrical current flowing
through that wire.

Current flow creates magnetic fields, and collapsing magnetic fields induce
current flow.

_(As mentioned in my blog post from 2003[about evolvable
hardware](/home/2003/07/15/creatures_from).)_

AND SO:

Video decoding in the Mac is handled by the [Apple
T2](https://en.wikipedia.org/wiki/Apple_T2) chip.

Would it be possible to

So that when the calculations and the radio resonate, it… jams?

And what exactly would happen? Would ops start failing only in that exact
realtime video process? You wouldn’t be able to detect its existence
otherwise. As humans we aren’t sensitive to EM radiation in the radio range.

Would the computer function as normal except for baffling failures there and
only there, a surgical excision of the machine’s MPEG capabilities?

Look I’m the ideas guy here, I have no idea, if you’re a spy with the relevant
kit then please try it and lmk.
