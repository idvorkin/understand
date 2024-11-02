# Unpacking Lares: our 2 minute pitch for an AI-powered slightly-smart home

I spent Friday night and Saturday at the **London AI Hackathon** organised by
Sarah Drinkwater and Victoria Stoyanova – they curated an incredible group of
120 builders, and the conversations bounced from AI prompt patterns and
software frameworks, to real-world applications, to what the literal worst
things we could build would be (we came up with an internet-ending super-
plausible concept at about 11pm on Friday…). So mind-expanding.

The point of the hackathon was to explore. [Sarah has her write-up
here](https://sarahdrinkwater.medium.com/how-to-run-a-generative-ai-hackathon-
dc27f8d4fdd0) _(both what happened and also how to run one yourself)._

I buddied up with old colleague [Campbell Orme](https://www.ineedmydevice.com)
and together we built **Lares:** a simulation of a smart home, with working
code for an generative-AI-powered assistant.

It’s pretty cool:

Large language models are capable of multi-step problem solving, if you prompt
them right (I’ve got a novel method to do that), and the overall territory
starts feeling like a new OS for physical space _(that’s my end goal)._ We
condensed our demo to a 2 minute pitch.

It was a blast, the whole event, especially working with Campbell again. 24
hours at an absolute sprint. (Including me getting locked in my own house on
Saturday morning and shredding my hand climbing out of the downstairs window…)

Anyway – **we won!** Twice!

I’m still completely blown away.

We won Best Business from Amazon AWS Activate AND Most Disruptive from
DeepMind, two of the five prizes on offer, out of about two dozen teams. Thank
you, thank you.

**[Watch the Lares pitch video here](https://vimeo.com/820486088)** _(Vimeo, 2
mins)._

Hey so let’s unpack that video…

First the name – the ancient Romans had gods high up on Olympus but they also
had domestic gods. [Lares](https://en.wikipedia.org/wiki/Lares) _(Wikipedia)_
were the household deities, with shrines at home for making offering to your
family _Lar._ We ran across a pic of a shrine with a lucky snake on it, hence
the logo. And a shout out to [Matt Jones](https://petafloptimism.com) for
reminding us all about household deities over many years.

The setup for the demo is this:

In this first demo the goal is: "turn off the lounge light."

The green text on the right shows the internal “thought process” of the large
language model.

It’s using the ReAct pattern, which is straightforward and surprisingly
effective, [as previously discussed](/home/2023/03/16/singularity). This
pattern gets the AI to respond by making statements in a
Thought/Action/PAUSE/Observation loop:

Generally with the ReAct pattern the tools made available to the AI allow it
to query Google, or look up an article in Wikipedia, or do a calculation.
Using tools decreases the risk of hallucination and gives the AI access to
accurate, up-to-date data.

For Lares we made the smart home into a tool. We said: hey here are the rooms,
here are the devices, and here are their commands, do what you want.

**Demo result:**

The LLM identifies the ID of the light in the lounge, and issues the
_“toggle”_ command to turn it off.

Ok: robots.

Conventional voice assistants like Alexa and Siri require you to speak in a
pretty constrained syntax, like a machine yourself. They’ll address that
pretty soon, I’m sure, so let’s get a glimpse of what that might be like. We
can express **multiple commands in natural language.**

So our new goal is: "send robot to the office and turn on the light."

Oh yes and – a (simulated!) robot.

For Lares we asked: what if the tools provided to the large language model
could deal with **acts not facts.** So not just searching Wikipedia but
turning lights on and off and, sure why not, driving a robot around the house.

_(The future is ActGPT not ChatGPT amirite??)_

The “believable future” is this:

The fisheye video in the background of the demo is the **robot POV.**

The video is also simulated: we pre-baked an idle-state video loop for each of
the four rooms, in “lights on” and “lights off” states. The computer vision
rectangles are also simulated; there’s no recognition happening here.

**Demo result:**

The LLM figures out the “move” command for the robot and the required ID of
the destination. It moves the robot, then turns on the lights in that room
(which was ambiguous in the original goal but it handles it fine.)

Problem solving!

The ReAct pattern is great but it’s prone to instruction drift: after a
sequence of actions, the AI loses track of what it’s supposed to be responding
to, and starts hallucinating commands that don’t exist, or gets stuck in a
loop, or losing its formatting. This is incompatible with problem solving.

So I have a variant on ReAct, which is new for this project _(and perhaps new
in the field?)._

So the sim on the phone now takes on another purpose: it shows the actual
**working memory of the AI.**

Look at that simulated app: it has a line for who is present in each room, but
all the rooms are listed as _“UNKNOWN”._ The AI knows the static layout of the
house and can send commands to the devices, but it can’t see – remember, in
this privacy-first smart home, we’re not blanketed with cameras. It will have
to _look._

The ambitious goal set by the user is: "where is my dog?"

It’s brilliant watching the LLM solve this:

And we’re done.

Now there are limitations here: I tried a demo with a goal "turn on all the
lights" and the LLM got confused. It’s overly sensitive to the content of the
example transcripts embedded in the prompt. So we’re operating on the edge of
its capabilities here – but I can see ways to increase robustness, and we gain
a more humane UI and basic problem solving, so it’s worth digging.

I’ve been tinkering with the home sim side of Lares for a while – my interests
right now are in the intersection of AI, multiplayer/small groups, and
embodiment (gestural interfaces, and physical things/devices). So I need a sim
as the basis for a few sketches I have planned.

The LLM work was new for the Hackathon. I’ve been working with a couple of
startups on their product exploration, getting properly hands-on with
programmatic AI and using LLMs in novel applications. It was brilliant to
bring those patterns to life – and I really, really wanted to explore AI tool-
use with a pretend robot.

Technically I had the thing cracked by late night on the Friday. I’ve been
bouncing off this problem in some other contexts for a few weeks, and the
“ReAct + working memory” was something that only just occurred to me. It was
an absolute relief to get that working.

Which meant I got to spend all of Saturday with Campbell on how to make a demo
that told the story that we wanted to get across.

I keep circling the same idea: an operating system for physical space.

My clearest articulation of it (which is not at all clear) is in this post
about a “Map Room” from the 1950s, and how to bring it in the 2020s: [a
physical room size wiki for collaboration](/home/2023/01/20/map_room)…

Consider a room with a projector that shows an overview of your whole “map”. …
We navigate the map with gestures. It shows the same view for everyone. We
don’t all need the identical physical setup – the projector can be large or
small or point at any wall. … the system has gaze detection… it knows where
you’re looking.

… everyone wears earbuds + mic. There’s proximity audio so, if you’re in the
main shared space, you can hear remote people who have their cursors near
where you’re looking.

And I talked about this at the [Future of Coding](https://futureofcoding.org)
meet in London last month: I can imagine some kind of future OS that is
natively multiplayer and hybrid with humans and robots and NPCs and
telepresence; that merges gaze and pointing and voice and peripheral vision;
that allows for programmable apps just as our phones do; that is privacy-first
and builds out of where we are _now_ instead of requiring fully-instrumented
totalising environments; and so on.

Lares isn’t _that_ – but it’s the beginnings of a platform to explore those
ideas. We barely scratched the surface.

Thanks again to the AI Hackathon organisers, hosts, sponsors, judges and other
attendees – it was so exhilarating, and such a great focus for making a run
into this territory. The other pitches were variously mind-bending,
thoughtful, hilarious, and diverse… but I’ll let them do their own write-ups.

And thank you Campbell! So much fun.

If the Lares demo sparks any thoughts for you - or if you have ways to
supercharge this work - do please drop me a note.
