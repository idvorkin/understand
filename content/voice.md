# How I would put voice control in everything

Why can’t I point at a lamp and say **“on”“** and the light come on? Or point
at my stove and say **“5 minutes”**? Or just _look_ at it and talk, if my
hands are full.

I speculated about voice-controlled lightbulbs and embedded machine learning
on stage last year at Google’s [People & AI Research
symposium](https://pair.withgoogle.com/events/symposium/) _(there’s a link to
a video on that page)_ and was reminded about it the other day when [George
Buckenham tweeted](https://twitter.com/v21/status/1264893090743058438?s=21)
"as someone who already owns an Alexa, I would buy a device that doesn’t do
any cloud processing, but does allow you to set kitchen timers with your voice
and play songs from Spotify" – which is basically all I do with Siri too, and
this is _kinda_ what I want too…

…only not a single device, I want voice control in everything, but
individually. And really, _really_ basic.

Because it _is_ really appealing to me to turn on a light, set the stove
timer, play music, pause the TV, snooze an alarm etc just by saying something.
What’s _not_ cool is

And all of that aside, voice assistants are still all [more or less
rubbish](https://daringfireball.net/2020/05/what_time_is_it_in_london).

Do less. Do it really well. Reduce cognitive friction.

Make a lightbulb that you can say **“on”** and **“off”** to:

I was struck to learn that the iPhone’s _“Hey Siri”_ feature (that readies it
to accept a voice instruction, even when the screen is turned off) is a
[personalised neural network that runs on the motion
coprocessor](https://machinelearning.apple.com/2017/10/01/hey-siri.html). The
motion coprocessor is the tiny, always-on chip that is mainly responsible for
movement detection, i.e. step counting.

If that chip hears you say “Hey Siri”, _without hitting the cloud,_ it then
wakes up the main processor and sends the rest of what you say up to the
cloud. This is from 2017 by the way, ancient history.

So, commodity components time: here’s the [BelaSigna
R281](https://www.onsemi.com/products/audio-video-assp/audio-dsp-
systems/belasigna-r281), an ultra-low-power (300 micro watts, mic not
included) chip that "is “always listening” and will detect a single, user-
trained trigger phrase, asserting a wake-up signal when this trigger phrase is
detected."

A embeddable wake-word detector! Let’s stick it in a lightbulb! A radio! A
desk fan!

So how would a device with this simple word detector know when to pay
attention? Some wild speculation…

_(Bonus points: do all of this with**energy harvesting,** so no batteries, and
zero power on standby.)_

Look, my point is that this is not beyond the reach of very clever people with
computers. Stick a timer in my stove, a switch in my light bulb, give each a
super limited vocabulary, never connect to the internet, and only act when
somebody is addressing you.

Which, in turn, gets rid of the complicated set-up and addressing interaction
design issues of centralised voice assistants. No more “front room lights:
lamp 1 turn on” because… you just look at it.

And _also_ gets rid of the need to add expensive connectivity (and set-up, and
security patches…) in every stove and light, and the need to convince every
manufacturer to support the latest control protocol because… you just look at
it.

And, _ALSO_ also, by simplifying but spatialising the available grammar, the
voice interface will be easier to learn, more reliable to use, and easier for
normal humans to combine.

And yes, given this leeway, different manufacturers will go in slightly
different directions. But net-net I bet that the overall simplicity is
improved versus the current approach of attempting to make standardised
interfaces for _classes_ of products that have to be tweaked case by case to
properly fit.

It’s a classic [worse is better](https://www.jwz.org/doc/worse-is-better.html)
approach.

And the reason it doesn’t work like that already, and why we’re stuck with
dedicated, centralised voice assistants that need to bounce a signal off a
data centre on the freaking Moon _(not actually the Moon)_ to set a timer?
Well, I can imagine a few possibilities…

I think that last point is probably what’s going on. I get it.

BUT

There’s [that line from John Gall](https://en.wikiquote.org/wiki/John_Gall): "
A complex system that works is invariably found to have evolved from a simple
system that worked."

So let’s get the basics right first, then layer orchestration and all the
advanced stuff etc on top?

If I had all the VC money in the world, I would manufacture and sell
standardised components – they would connect and _act_ identically to
mechanical buttons, switches, and dials, only they would work using embedded
ML and have voice, gaze, and pointing detection, for interaction at a
distance.

The goal would be to allow manufacturers of _every_ product to upgrade their
physical interfaces (add not replace ideally), no matter how trivial or
industrial, no matter how cheap or premium. And, by doing that, discover what
new possibilities are uncovered when when you don’t force every voice
interaction through a single model, that of requiring an internet-connected,
consumer-friendly, device for the home.

Anyway.
