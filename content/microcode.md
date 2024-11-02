# Revolutions and NAND gates, eight cents, wholesale

I recently read Tracy Kidder’s Pulitzer-winning [The Soul of a New
Machine](https://en.wikipedia.org/wiki/The_Soul_of_a_New_Machine) (1981) about
the development of a new minicomputer by Data General.

Here’s a passage about transistors:

Transistors, a family of devices, alter and control the flow of electricity in
circuits; one standard rough analogy compares their action to that of faucets
controlling the flow of water in pipes. Other devices then in existence could
do the same work, but transistors are superior. They are solid. They have no
cogs and wheels, no separate pieces to be soldered together; _it is as if they
are stones performing useful work._

Reading that, it’s so clear that 1981 is closer to 1947 (when the transistor
was invented) than today.

Matter, without movement, can perform useful work! Solid state. This idea is
_insanity_ when you think about it, and Kidder in 1981 was able to call that
out.

Two transistors make a NAND gate, and a NAND gate is both a physical thing and
a mathematical operation and - with many connected together - can store
numbers, add numbers, discriminate between numbers, and so on, numbers being
both data and instructions to perform more operations.

The solution takes the material form of a circuit called a NAND gate, which
reproduces the “not and” function of Boolean algebra. The part costs eight
cents, wholesale.

The latest iPhone has 11.8 billion transistors. So the chip at the heart of
each phone is $1.4 billion in parts, no margin. That’s 1981 prices, 2021 money
[accounting for
inflation](https://www.in2013dollars.com/us/inflation/1981?amount=472000000).

_(Updated 5 March to fix maths/words. Previously claimed $1.5b.)_

The book narrates the journey from standing start to functional computer
hardware.

I’ve done this myself. One of the labs at college took us from semiconductors,
through transistors, then gates, then shift registers, then designing and
seeing for ourselves primitive adders, memory, and commands, and finally
working with a 6502 processor. The 6502 is the chip inside the BBC
Microcomputer, which I grew up with, so it’s sophisticated while also being
simple enough that - having built our own registers etc - you can look at the
schematic and kid yourself that you know what’s going on. And when you poke
binary into the 6502 and program it to add 2 and 3, and execute that operation
and, having ascended that ladder with your own hands, see in your mind’s eye
the shift registers rippling and the gates flipping and the electron in every
transistor collecting and flowing…

A spiritual experience, and a healthy dose of cognitive vertigo.

And then, with consumer hardware, I’m familiar with that weird knot of
bringing up hardware: the bench prototype, firmware, basic interaction, and
the gyre that spirals up as you develop each part – but also the role of
simulators, partial documentation, and internal languages. Developing systems
is hard.

Despite _all_ of that, I hadn’t quite appreciated the role of
[microcode](https://en.wikipedia.org/wiki/Microcode), being: "a layer of
computer organization between the CPU hardware and the programmer-visible
instruction set architecture of the computer."

A programmer will ultimately break their code down into primitives like ADD
and JUMP, but at a certain point those instructions have to be converted into
a series of high/low signals that tell circuits what operations to perform and
where to send their data. It’s where software becomes hardware, where the
rubber hits the road, as it were. It’s the level at which there aren’t any
abstractions anymore.

Microcode is, in this sense, like early Old English, in which there was no
word for fighting and a poet who wished to convey the idea of battle had to
describe one.

I don’t know if that is an Historical Fact about Old English, but I like the
turn of phrase.

Anyway, it’s a terrifically told story mainly about personalities and teams,
and also about computers.

Also a history at this point too. A floppy disk is explained as "like a 45-rpm
record" and few readers in 2021 will have direct experience of either
referent.

So it’s an easy trap to read the story and see it as archaic, but really it’s
archetypical; this is the world we live in now, but slowed down and magnified
so we can see the roles and relations and gaps at something like human speed.

One other quote that caught my eye:

For many years sociologists and others have written of a computer revolution,
impending or in progress. Some enthusiasts have declared that the small
inexpensive computer inaugurated a new phase of this upheaval, which would
make computer instruments of egalitarianism. …

But in the main, computers altered techniques and not intentions and in many
cases served to increase the power of executives on top and to prop up
venerable institutions.

And that’s another observation that could only have been made closer to the
start than today, with the perspective to see the before and after: if it
served to entrench and not upend the existing class system, was the computer
revolution a revolution at all?
