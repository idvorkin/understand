# Wireless wires and hardware APIs

The high point of home automation was hi-fi separates in the 80s/90s. (The
concept should be modernised for the 2020s.)

You got an amplifier. Into that you plugged in all the other components: tape
deck, radio, vinyl turntable. Eventually a CD player, maybe the TV is an input
too. Out of the amp came the speakers.

The components were connected with phono cables. Do they still exist? I guess
in some form.

Phono cables come in pairs: the red plug goes into the red socket, the white
plug into the white socket. There’s no orientation hassle like with USB. The
plugs are round and fit securely.

What I’m saying is that the connectivity system was: obvious (once you know
the colour matching trick), scalable (you could keep chaining components),
open to inspection (you can see what’s going on), and standardised.

Being standardised:

I mean, god forbid my smart home should be so simple now.

Yes I can plug a Roku device into the HDMI port on my TV, and sign into my
streaming accounts on that. There’s often a QR code thingy to make the sign-in
flow relatively smooth, if you don’t mind doing that a half dozen times.

And let’s not get into Netflix and iPlayer demanding that I choose a personal
profile to watch TV with, despite the fact that there’s usually two or three
people on the sofa. You would have thought that device-specific profiles would
be supported now.

I own one (1) smart plug which is used to check how often a water pump is
activating. I seem to remember activating that with a QR code too. Shame you
can’t tell whether or not it is connected to an account, and whose, just by
looking at it.

Perhaps a modern phono cable would be a wireless wire.

You’d buy a single object from the shop – a plug with two ends. You’d snap it
in the middle. From then on until forever the two ends would be spookily
joined. So you could plug one side into the back of a light-switch indoors,
and the other into the separately-powered Christmas lights outside, and it
would work.

Or maybe it would look like a pair of Apple Airtags, stuck back to back. You’d
peel them apart and magnetically attach them to the different components.

Part of me wants a streaming media junction box for my home. It would be a box
that I would sign into with all my accounts. It would have a bunch of outputs,
and I would plug one end of my wireless wire into this junction box, and the
other into the TV or the speakers or whatever.

Or I would carry the other end in my pocket to my friend’s house, and we could
watch TV there.

This isn’t just for streaming. Devices should have a standard hardware API - a
couple of pins that publish events (like: radio re-tuned, or switch pressed,
or doorbell motion sensor activated) and accept commands (like: re-tune to X,
or remote activate switch, or record and send video).

Then I would plug half of my wireless wire into the hardware API, and the
other half into a box labeled “cloud” hooked into my wifi router. Then if I
wrote any code online, or wanted to give a service access to it, the events
and commands for that device in my house would be available at a standard URL.

Back in the day (2008) we built a radio called _Olinda_ with a hardware API:

On the side of Olinda is a studded, magnetic connector for plugging in
expansion modules. This is an open, standardised hardware API - with defined
connections and defined protocols for the data. It’s a bit like the expansion
port on an iPod, and this makes the radio modular. It’s a hardware version of
the APIs around websites like Flickr, del.icio.us or Twitter - which, by
virtue of their APIs, are all surrounded by a rich ecosystem of supporting
sites and products.

The ideas of modularity and [adaptive
design](/home/2020/08/26/adaptive_design) were _so_ powerful, and there were
some fascinating ideas being incubated in consumer product back then, but they
got kinda lost in the smartphone tsunami which started growing when the iPhone
was launched in 2007 and the tide never really went out.

I’m not arguing for a return to separate components for everything, just for
the sake of it. The fact we all carry phones, now, that can be soft interfaces
to literally anything – that’s another wrinkle. Then there’s not wanting to
have your data used for adtech, and not wanting to have ways to easily get
stalked, and so on.

And of course our devices are different now: smart speakers, zone heating,
computer peripherals.

But, I don’t know, I hope that Apple or Google or someone has a lab somewhere
which is imagining a kind of alternate future smart home which is as good as
the phono cables of the 80s, and they’ve got the whole thing worked out, and
they’re figuring out how to get there, and when smart specs finally launch,
one of the apps will be the ability to see the smart wiring diagram of my
house overlaid as coloured glowing lines in augmented reality.
