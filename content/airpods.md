# AirPods, and the cognitive ergonomics of tools for thought

I’ve been trying out the dynamic head tracking feature of the new AirPods 3,
and it makes me feel like the cognitive ergonomics of computer interfaces is -
still - way too disconnected from everyday design.

The head tracking technology is intriguing.

First there is spatial sound, which arranges sound in a sphere instead of in
stereo. Apple Music now has a a bunch of music remastered spatially and
personally I find it distracting when, say, the vocals are placed to the side
and behind the drums. But anyway, it’s a thing, and spatial sound isn’t just
for music. It’s an enabler.

So then there is _head tracking_ which fixes the sphere in space even as you
move your head.

For example: you walk down the street listening to regular stereo music. You
turn to look to the right briefly, and the left and right channel remain fixed
on the imaginary sphere around your head. The music that was previously
(apparently) ahead of you is now only in your left ear.

It’s awesome.

And weird.

There are some problems with head tracking as a feature.

You can switch between modes, but [check out Apple’s own
documentation](https://support.apple.com/en-
tm/guide/airpods/dev00eb7e0a3/web): you have to long-press the volume on your
phone to find out what options are available.

Then head tracking isn’t available with all devices. My AirPods switch
seamlessly between my devices, but they don’t all have the ultra-wideband chip
that head tracking requires. (UWB is some clever radio magic. Apple call their
chip the U1.) So it’s sometimes available and sometimes not.

Now the UWB chip is what allows for relative positioning with high precision
(mm accuracy last I checked) and low latency (you need it to be low
milliseconds to work well with audio). It is clearly a jigsaw piece for
Apple’s as-yet-unannounced work with augmented reality, so the U1 (and
therefore head tracking) will end up in all their devices. So that
inconsistency gets sorted.

But even so, head tracking gets used in a few different ways and it’s not
clear to me, the user, what’s going on.

For instance: the other day I was working at my Mac and playing music from my
iPad, and it appeared that the music was originating from the iPad itself – it
had been spatialised to be located in the device.

Did I imagine that feature? How did it happen?

So there’s a lot of confusion in the user experience: poor naming, hidden
modes, and so on. The technology is rock solid but with inconsistent
manifestations.

Which is fine! There is a ton of learning going on.

_(You can see Apple releasing jigsaw pieces like head tracking, photogrammetry
with ARKit, and LIDAR in the Pro phones. At a certain point, the supply chain
will be de-risked and the developer community will have devices that can
function as dev kit – and then it will be the moment to land smart glasses,
whatever form they take, and the only “risk” is the consumer experience, and
Apple has nailed how to launch and iterate that. The playbook in action is
astounding to see.)_

OBSERVATION #1

Stereo music usually feels like it is located at the centre of my head, right
between my ears.

Spatialised, these AirPods place the music right in front of my third eye:
about an inch in front of my face, and just above my eye line.

With head tracking, the apparent locus is as steady as a rock.

And it is super bizarre. Like, I can see why Apple has made this decision:
music played from the centre of my head would not move with head tracking at
all. It would be at the centre of the imaginary sphere.

But placed where it is, I go slightly cross-eyed. I end up focusing really
close up and looking up slightly, at an invisible source of sound.

OBSERVATION #2

When the music apparently came from my iPad, while I was working on my desktop
Mac, I found it way easier to focus on my work. Oh!

The background sound was physically separated (not actually, but using head
tracking) from the point of my attention: the on-screen document. That
separation seemed to allow me to concentrate better.

Which is… a fact worth paying attention to, right?

The question for me is this:

What are computers for?

Are they, as the name of Howard Rheinhold’s 1985 book suggests, [tools for
thought](http://www.rheingold.com/texts/tft/)?

If so, how do we understand how to bias interfaces to make it _better thinking
easier_ – and what are the contributing factors to good thinking anyway?

Specifically questions like:

Is it milliseconds faster to respond to a device notification if the sound of
the notification appears to emanate from that device?

Can more be held in working memory (and therefore synthesise information in a
more sophisticated way, faster and smarter) if the documents are distributed -
using sound feedback - over a wide surface, rather than being at a single
point under the thumb? And is that ability to synthesise measurable?

I’ve asked similar questions a couple of times before:

I would generalise this to _cognitive ergonomics:_ how do we make user
interfaces that better match how we think? And by think I mean: synthesise,
create, pattern match, abstract, linearise, and so on.

So much of today’s desktop user interfaces were driven by early psychological
considerations: Fitt’s Law being how quick it is to move a cursor to a target
(and that you can think in the meantime), or the screen itself being a visual
cache for working memory.

I’m sure the HCI community has continued this good work.

I would love to know certain things, in addition to the above. For example, I
have a hunch that the fundamental “tick” of the brain is around 100-150ms –
that how long it takes for a signal to move across the thinking meat, if I
remember right. Interfaces that respond within that time feel fluid, and
outside that time make you feel like you have to wait. Is that true? Does it
have an effect on, say, our ability to do recall or have a novel idea?

Or is parallel thinking possible? Does the time taken to move a mouse cursor
provide the ability to consider what happens next? Does using sound to create
a cognitive map and loading/unloading data from working memory allow for
synthesis which is faster?

My dual wishes are these:

That Apple, Microsoft, Google and so on employ cognitive neuroscientists to
develop quantifiable measures for good tools for thought, study modern
interface approaches against these measures, and publish their research – just
as they publish widely with machine learning or cryptography.

And that front-end code libraries bake in these rules. If 100ms is the
cognitive tick, then that should be a top-level guarantee for any user
interface toolkit. And so on.
