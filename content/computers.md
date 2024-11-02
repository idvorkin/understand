# Why not faster computation via evolution and diffracted light

Something I wonder is: what if computation, with today’s technology but done
differently, could be - say - a million times faster? Here’s my thinking.

If there’s a defining feature of what computers are, I would say it’s
_abstraction layers._

You can tap buttons and move windows without thinking about what’s going on
behind the screen. The programmer of that app sets out the instructions to
draw those windows, and how they should behave, all without having to think
about how exactly the instructions will be carried out.

Those instructions are defined in simpler instructions, and so on, and so on.
Eventually there are instructions that tell the chip what to do – but even
that isn’t the end of it. Because, [as I learnt
recently](/home/2021/03/02/microcode), the chip itself turns its instructions
into still more fundamental operations: microcode. Microcode choreographs the
physical building blocks of the machine… registers, adders, flip-flops. And
below _those_ are gates. And below _those_ are transistors.

It is _absurd_ that a finely inscribed piece of silicon, with electricity
running across it - [the pattern on the
stone](https://en.wikipedia.org/wiki/The_Pattern_on_the_Stone) \- can be this
_thing,_ the computer. And yet!

Each abstraction layer hides the complexity beneath, and provides general
purpose flexibility to the layer above.

BUT

Here’s my question. Abstraction means reliability and composability. But
surely each layer comes at a cost? And there are so. many. layers.

Let’s say you just wanted to perform just one task. Say, recognise a face. Or
know whether a number is prime or not. And you didn’t care about flexibility
at all.

Could that task be performed by simply the right set of transistors, at the
hardware level, no matter how insanely arranged?

_What shortcuts could be taken?_

Here’s my evidence that this is a valid question to ask: a paper from 1996 on
the topic of [evolvable
hardware](https://en.wikipedia.org/wiki/Evolvable_hardware).

‘Intrinsic’ Hardware Evolution is the use of artificial evolution – such as a
Genetic Algorithm – to design an electronic circuit automatically, where each
fitness evaluation is the measurement of a circuit ‘s performance when
physically instantiated in a real reconfigurable VLSI chip. This paper makes a
detailed case-study of the first such application of evolution directly to the
configuration of a Field Programmable Gate Array (FPGA). Evolution is allowed
to explore beyond the scope of conventional design methods, resulting in a
highly efficient circuit with a richer structure and dynamics and a greater
respect for the natural properties of the implementation medium than is usual.

I want to unpack that abstract:

This line in the abstract is far too modest: "a greater respect for the
natural properties of the implementation medium than is usual" – because what
happens is - excuse my French - BATSHIT INSANE.

Jumping to _Section 5. Analysis_ in [the
PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.50.9691&rep=rep1&type=pdf):

The evolved circuit is a mess.

So, of that tangle: "Parts of the circuit that could not possibly affect the
output can be pruned away." (By tracing what is connected.)

BUT! It turns out: if these parts of the circuit are prunes, the circuit no
longer performs as well.

It turns out that 20% of the components **cannot be removed** even though
"there is no connected path by which they could influence the output."

What has happened? Thompson has evolved a circuit from "a ‘primordial soup’ of
reconfigurable electronic components" – and he speculates that some of the
components are interacting via the power-supply wiring or electromagnetic
coupling. Not by conventional means.

(The circuit also stops working outside the 10 degrees Celsius range in which
it was trained.)

In 1996, the idea of “training” a computer to perform a task was slightly
absurd – yes, there were expert systems and there was AI, but it was a toy. 25
years later, and computers are fast enough such that machine learning is
standard practice at every tech firm… and we’re still figuring out how far it
can go. If trainable software’s time has come, how about trainable hardware?

Given a single task, such as recognising a few simple words or a face, or
performing protein folding, and so on, would it be possible to _discard_ the
complexity we currently devote to general purpose computing, and _train_ a
primordial soup of transistors to perform only that exact task – taking
advantage of whatever nonlinear local effects and physics is available,
abstraction layers be damned?

Here’s another type of computer that makes use of deep physics: [Artificial
Intelligence Device Identifies Objects at the Speed of
Light](https://www.techbriefs.com/component/content/article/tb/techbriefs/photonics-
optics/33676). It’s called a **diffractive deep neural network.**

The _existing_ way for a camera to recognise an object is for the camera to
convert light to pixel data, then the computer has, in software, a trained
neural network (that’s machine learning again) that runs matrix maths on the
grid of pixels until an object category pops out at the other end. The matrix
math is fearsomely complex, and is trained in a process called machine
learning. The result: It’s a dog! It’s a face! It’s a tree! Etc.

This _new_ way still uses machine learning, but the maths is replaced by a
series of very thin, semi-transparent "8-centimeter-square polymer wafers."
Each wafer diffracts the light that comes through it. And:

A series of pixelated layers functions as an “optical network” that shapes how
incoming light from the object travels through them. The network identifies an
object because the light coming from the object is mostly diffracted toward a
single pixel that is assigned to that type of object.

So you don’t need a camera.

You don’t need software.

You take a stack of FINELY ETCHED TRAINED PLASTIC WAFERS, and you look through
it at an object, like using a monocle. But instead of seeing the object more
clearly in focus, you see a cryptic constellation of glittering pixels. You
look up the constellation in your handbook, and… It’s a dog! It’s a face! It’s
a tree! Etc. Only, at the speed of light. With no power required.

Physics performing computation at the granularity of the universe.

By using the interference of light with itself.

The analogy for me is that you have a swimming pool, the shape of which is
ingeniously and carefully constructed, such that when you throw in an object,
the ripples all bounce around and reflect off the edges and change in speed
given the depth, and all collide in such a way that the shape of the splash
spells a word in the air: the name of the object you threw in.

I can’t help but cross these ideas in my head.

What if we disregarded general purpose computing and abstraction layers in
favour of speed?

What if we could evolve hardware to make use of hidden physics?

What if we used light?

What then?

Perhaps a computer, for a specific task, would be a million times faster. Or
to put it another way, that’s 20 Moore’s Law cycles: 40 years of performance
gain. That’s like saying we could leapfrog from 1981 computers to 2021
computers.

The _speed_ of computers now is what has made machine learning possible.
Advanced statistics, neural networks, etc, all of this was known pretty well
decades before. But it was impossible to run.

So what _today_ is impossible to run?

What if you could make a single-purpose, zero power lens that looks at a
handwritten number and breaks cryptography?

Or sequences a gene?

Or runs a thousand [faster than realtime
simulations](/home/2020/11/26/cerebras) and drives your car for you? Or
predicts behaviour of a person in a negotiation? What about computational
photography that can look around corners by integrating the possibility of
photons, or can brute force prove or disprove any mathematical theorem?

Or understands and can generate natural language just like GPT-3 but a million
times better? Or, [as in that speculation about an AI
overhang](/home/2020/08/24/ai_overhang): "Intel’s expected 2020 revenue is
$73bn. What if they could train a $1bn A.I. to design computer chips that are
100x faster per watt-dollar? (And then use those chips to train an even better
A.I…)"

What is the ultimate limit of computational operations per gram of the cosmos,
and why don’t we have compilers that are targeting _that_ as a substrate? I
would like to know that multiple.

And, a question for computer scientists, what single question would you ask if
you have a dedicated computer that was _[that multiplier]_ faster? Because I
would like to know.

I guess what I’m saying is that it might be possible, with today’s technology,
to make a monocle, perhaps one that you fold down like a pirate’s patch, that
when you look through it with your eye performs - with zero power - a single
massively complex AI computation on whatever you’re looking at, as fast as
computers will run decades in the future.

If I were the US government, I would be pouring _billions_ into this.
