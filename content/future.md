# Computers that live two seconds in the future

What does it mean that computers can peer a tiny distance into the future? I
have the vaguest of vague senses that a few things I’ve seen recently are
conceptually connected.

EXAMPLE #1

Apple announced its new headset [Vision Pro](https://www.apple.com/apple-
vision-pro/) the other day, and what’s neat is that they’re not framing it as
“augmented reality” but as a _spatial computing_ platform.

I’m into a vision of computing which is room-scale, embodied, and social (see
[this post about Map Rooms](/home/2023/01/20/map_room)) so I’m into this.

What this means:

Ok so there’s a ton of wild technology required to make this work!

And, to highlight one particularly wild point, if you virtual objects to feel
real, then the computer has to PEER INTO OUR (subjective) FUTURE to get ready
to react.

From ex Apple engineer Sterling Crispin on Twitter:

One of the coolest results involved _predicting a user was going to click on
something before they actually did._ That was a ton of work and something I’m
proud of. _Your pupil reacts before you click_ in part because you expect
something will happen after you click. So you can create biofeedback with a
user’s brain by monitoring their eye behavior, and redesigning the UI in real
time to create more of this anticipatory pupil response. It’s a crude brain
computer interface via the eyes, but very cool. And I’d take that over
invasive brain surgery any day.

Other tricks to infer cognitive state involved quickly flashing visuals or
sounds to a user in ways they may not perceive, and then measuring their
reaction to it.

_(Thanks[Ed Leon Klinger](https://twitter.com/edleonklinger) for picking up on
this.)_

Detecting the
[Bereitschaftspotential](https://en.wikipedia.org/wiki/Bereitschaftspotential)!

btw on that biofeedback point, Crispin also says this in their tweet:

Another patent goes into details about using machine learning and signals from
the body and brain to predict how focused, or relaxed you are, or how well you
are learning. And then updating virtual environments to enhance those states.
So, imagine an adaptive immersive environment that helps you learn, or work,
or relax by changing what you’re seeing and hearing in the background.

BUT: let’s go back to talking about the future.

EXAMPLE #2

Unexpected waves are a problem in shipping.

Like, you know when you’re looking at the choppy sea in a harbour? And a big
wave comes from nowhere and a random combination of ripples in a weird corner
makes water leap and splash into the air?

That’s a problem if you’re trying to get cargo across a gangway. "A gangway
crossing takes roughly 30 seconds" – and it’s catastrophic to get a
disconnection halfway through.

Wouldn’t it be great… if you could see… into the future… of the ocean.

WELL.

[Here’s WavePredictor by Next Ocean.](https://nextocean.nl/technology.php)

First they continuously scan the water around the ship with radar.

Then:

WavePredictor propagates the observed waves into the future resulting in a
near future prediction of the waves arriving at the ship and the resulting
ship motions.

It’s not just about avoiding freak big movements. It’s the reverse too:

" Pick the right moment to hook onto the load on deck when motions are
temporarily low."

Faster-than-realtime simulation of ocean waves to anticipate moments of still.

EXAMPLE #3

So [I use GitHub Copilot to write code now](/home/2023/01/27/copilot). It’s an
AI that can autocomplete 20 lines of code at a time.

It’s hard to think of another tool that has because some popular so fast.
GitHub is the main place where people store and share their code, outside big
corps, and [from their own stats back in
February](https://github.blog/2023-02-14-github-copilot-for-business-is-now-
available/): 46% of all new code of GitHub is written using Copilot. (Oh and
75% of developers feel _more fulfilled._)

It’s hard to put my finger on what it feels like, because it doesn’t feel like
using autocomplete in my text messages.

It’s perhaps more like the latter description. Because, when you use Copilot,
you never simply accept the code it gives you.

You write a line or two, then like the Ghost of Christmas Future, Copilot
shows you what might happen next – then you respond to that, changing your
present action, or grabbing it and editing it.

So maybe a better way of conceptualising the Copilot interface is that I’m
simulating possible futures with my prompt then choosing what to actualise.

_(Which makes me realise that I’d like an interface to show me many possible
futures simultaneously – writing code would feel like flying down branching
time tunnels.)_

Look: we cross a threshold when computers can do faster than realtime
simulation.

[I’ve tried to put my finger on this before](/home/2020/11/26/cerebras)
(2020):

I can imagine a wearable device that continuously snapshots the world around
you, runs the simulation in fast forward, and pre-emptively warns you about a
mugging, or a bike going off course. Call it augmented apprehension.

([Or to fly in new edge-of-chaos ways](/home/2022/03/02/wheels) by bumping off
vortices using predictive fluid dynamics.)

And so I’m connecting these three examples because they feel like glimpses of
a different type of computing.

Let’s say that an interactive operating system contains within it a _“world
model”_ that makes it possible for apps to incorporate the world into their
user interface.

i.e.:

And therefore:

What happens when this functionality is baked into the operating system for
all apps to take as a fundamental building block?

I don’t even know. I can’t quite figure it out.
