# Training my sense of CO2 ppm

I picked up a new home CO2 monitor yesterday. [Here’s a
photo.](https://www.instagram.com/p/Cf9iuIHqdOv/) I went with the [Aranet4
(HOME edition)](https://aranet.com/products/aranet4/) because

I bought mine on Amazon for the same price as buying direct.

**I want to build an intuition for how varying CO2 levels make me feel.**

This second, near my desk, CO2 is 463 ppm (ppm = parts per million).

Atmospheric is approx 420 ppm so it’s higher indoors – and higher still when
I’ve been sitting in the same room all day.

CO2 levels are pretty dynamic, I’m told. An occupied, closed room will get to
1,000 ppm. A meeting room without fresh air, 1,500 ppm. You can hit over 2,000
ppm in a contained space like a train.

High CO2 levels are an indicator of poor ventilation, which isn’t great for
Covid transmission.

But _also_ not good for cognition.

at 1400 ppm, CO2 concentrations may cut our basic decision-making ability by
25 percent, and complex strategic thinking by around 50 percent

Even before that, you start to get drowsy around 1,000 ppm. How much brain fog
is not to do with long Covid but simply because I’m no longer sitting in a
large, well-ventilated office? I’d like to know.

_(Hey so there’s a chance that CO2 levels rise to the point that we all become
too dumb to figure out the climate crisis. Ruh roh /insert Scooby Doo gif.)_

You can train your own sense of the current ppm by keeping an eye on the
sensor read-out and introspecting your personal energy levels. Here’s what my
friend Ben Pawle from [Nord Projects](https://nordprojects.co) told me:

We’ve got one in the studio. Actually been surprisingly helpful. When you
start getting brain fog and feeling sluggish then you glance and see the co2
is 800 you know to open more windows. Then you feel great! We’ve actually got
weirdly good at describing how we feel in terms of energy levels by co2 level

Which is not the first time I’ve heard that!

I’m looking forward to the day when I can walk into a room and say, _huh,
feels like 800 in here,_ and decide to sit somewhere else.

Here’s the referenced paper from the article above.

Karnauskas, K. B., Miller, S. L., & Schapiro, A. C. (2020). [Fossil Fuel
Combustion Is Driving Indoor CO2 Toward Levels Harmful to Human
Cognition.](https://doi.org/10.1029/2019GH000237) _GeoHealth, 4_(5).

**I want to train my mental model for how CO2 levels change over time.**

I have questions like:

To do this I need graphs.

Now I was initially concerned that the Aranet4 sends its logged data only to
its own app. Looking at a 7 day graph in an app is fine, but I’d prefer to do
my own presentation and analysis. I would like to

Also:

**Alerts!** If CO2 hits 800 ppm (for example) I would like to ping my smart
plug to turn on the coloured Christmas lights that hang on the shelves behind
me. That’s not enough to interrupt me if I’m concentrating, but it gives me
peripheral vision that I should increase ventilation and I’ll notice it when
my head comes out of flow. I’m aaaaall about that ambient awareness.

So I don’t want my data trapped in an app. I want the sensor to have an
hardware API. [I wrote about the idea of hardware APIs
here](/home/2021/08/03/phono) _(2021):_

Devices should have a standard hardware API – a couple of pins that publish
events (like: radio re-tuned, or switch pressed, or doorbell motion sensor
activated) and accept commands (like: re-tune to X, or remote activate switch,
or record and send video)

_(It doesn’t need to be copper pins. Wireless is fine too, so long as it’s
open.)_

_(It’s important that this runs locally, without hitting the cloud, because
the privacy concerns of this level of access to my home are considerable.)_

Basically: I want to work with my home gadgets and appliances as easily as I
can set up rules and filters in Gmail.

AND SO I am tentatively happy that there is a [Python library for the Aranet4
sensor](https://github.com/stijnstijn/pyaranet4) (pyaranet4)! Good news.

This means that, in theory, I should be able to connect from my Mac, or the
always-on Raspberry Pi sitting on the bookshelves, and pull data from the
sensor on a regular schedule. And given _that_ I should be able to do all of
the above.

A project!

I was born at 335 ppm. Atmospheric CO2 is 25% higher today.

(See [co2levels.org](https://www.co2levels.org) for a giant historic graph.)

Ok so there’s noticeable cognitive impairment on complex decision making when
CO2 levels are _much_ higher – but is even this 25% atmospheric uplift dinging
my IQ?

Like: lead in fuel, [as previously discussed](/home/2022/03/11/saeculum):
"Leaded fuel reduced the IQ of everyone born before 1990 by ~4.25%."

Which is _wild,_ right? And may explain some elements of boomer politics…

But, being more specific, what lead is dinging isn’t just IQ – I seem to
remember that lead affects impulse control? And CO2 affects _“complex
strategic thinking”_ so that’s an attentional thing, maybe?

I am suuuuuuper out on a limb here, but: _smartphones?_ What if this century’s
rise of short-attention-span casual games, attentional disorders, etc, is not
to do with too much screen-time at all, but is a symptom of growing up under
increased atmospheric CO2?

And so our recently-slightly-diminished inability to hold a coherent thought
for a long span of time is what attention-maximiser apps like infinite-
scrollers (Twitter) and ad-engagement-optimisers (Facebook) and swipe-skinner-
boxes (TikTok, Tinder) are, deep down, all exploiting?
