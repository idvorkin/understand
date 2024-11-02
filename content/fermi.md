# The web3 world computer is at a 1970 level of development

I’ve been hanging out in the web3 space recently. The art and aesthetic
generally is awesome and effervescent. But there are big claims made for the
technology and, [given the high level of scams](https://web3isgoinggreat.com),
I’ve spend a bunch of time considering that.

With any new tech, it’s interesting to ask: does this matter? Is it a weird
blip or does this become part of the technology landscape for decades to come?
If so, how? A change in consumer expectations or wildly disruptive at a
widespread and technical level? Does this tech matter directly, or is it
basically a discovery mechanism for new use cases, acting as inspiration for
new tech that answers that same revealed use case but in a different way?

Most interesting: where are we in computing history?

For e.g.: My take is that [VR is waiting for its Macintosh
moment](/home/2022/04/20/vr) which puts it in the mid 80s and my gut says
that’s about right. Assuming decent smart glasses drop this year or next, then
it’ll take a decade of deployment phase till we’re in the “mid 90s” and VR is
transforming everyday life. At which point we’ll be ready for the big twist,
which for the PC was the arrival of the web, and it took another decade for
PCs to become culturally dominant. Perhaps, v roughly, VR is on the same
curve.

Ok, web3.

So I’ve been poking around in Ethereum which is one of the two big
blockchains. Bitcoin is the other and that’s mostly financial. Ethereum is…
something else.

Reading the smart contract source code that underpins NFTs ([here’s the
spec](https://eips.ethereum.org/EIPS/eip-721) and [here’s some
code](https://github.com/OpenZeppelin/openzeppelin-
contracts/blob/master/contracts/token/ERC721/ERC721.sol)) is super
informative! You can see what it means for a digital item to “exist.” You can
see what it means for one of these items to be “owned.”

I get the same feeling as when I read the source code for the original Unix
operating system, which is basically the ur-OS that either directly or
indirectly (because it established the concepts) underpins this epoch’s
computing environment. [You can see what a process
is!](/home/2005/09/24/what_is_a_process) What is a file is. What a user is.
The feeling is a combination of: oh now I know the fundamental particles; and,
_is that it??_

NFTs don’t “exist” on the Ethereum blockchain. The smart contract that tallies
and tracks ownership for a _class_ of NFTs does exist: it’s code that runs. As
a single instance, this means that NFTs of the same class are forever linked.
By analogy: imagine a print of some art is limited to 100 editions and they
are all sold and now hang in people’s homes all over the world. Now imagine
that they are spookily connected to one-another.

An NFT is a smart contract that achieves _something_ like digital ownership,
but actually it has a subtly different nature. Which is worth knowing.
Opportunities for invention come from knowledge of the deep physics of a
universe.

Long story short, I finally came to understand whey [they call Ethereum the
World Computer.](https://consensys.net/blog/news/programmable-blockchains-in-
context-ethereum-smart-contracts-and-the-world-computer/)

NFTs are one type of smart contract that can run on the world computer. Other
smart contracts can do anything that code can do.

Smart contracts aren’t contracts, that’s a financial or legal framing. Smart
contracts are object instances, in the object-oriented code sense, and the
Ethereum blockchain is a shared object runtime.

Robin Sloan gets it. I didn’t get it when I read his notes last year, but now
I do.

Ifeel like this simple premise is often lost in the haze: _the Ethereum
Virtual Machine, humming heart of Web3, is a computer that charges you many
dollars to execute a very small program very slowly._ It does so in an
environment with special properties, and in some cases, those properties are
worth the expense. In others … it’s like running your website on a TRS-80 with
a coinslot.

(And also read Sloan’s essay from around the same time, [The slab and the
permacomputer](https://www.robinsloan.com/lab/slab/), which is a meditation on
the idea that "‘computers’ might melt into ‘compute’", something more
environmental then physical.)

**There is a picture in my head that the computing environment of the future
is a vast shared substrate where digital ownership is IRL-equivalent.** With
all that ownership implies and requires: identity, economics, object
permanence, a truth grounded deep in the physics.

Maybe achieving that requires tearing up everything way back to… well, when?

Let’s say that the Ethereum virtual machine, the world computer, is indeed the
shared object runtime that we will need. Object-oriented code being the
paradigm invented by Alan Kay such that blobs of code sit together, an object
instance representing (say) an on-screen menu, or a user, or whatever. The
paradigm provides abstraction such that code can reach dizzying complexity,
while also retaining expressiveness to create new things.

_Object runtimes such as…_

_(Yes,[I continue to be obsessed](/home/2022/04/25/kay) with the career
history of Alan Kay.)_

It’s interesting to me that you need both (a) the hardware, and also (b) an
expressive and powerful object runtime such as Smalltalk if you are going to
_invent_ the user interface layer, which allows users to interact with the
machine and also provides a platform for apps.

If I kinda squint… I can kinda imagine how you might bootstrap today’s
Ethereum virtual machine all the way up to a Smalltalk-equivalent. And if you
get to that point, you can ladder your way up to a GUI analogue, and from
there to modern-day computing.

So how far away are we?

How far away is today’s web3 from something as sophisticated as today’s
computer world?

Let’s do some sums.

And _really_ hand wave our way to a [Fermi
estimation](https://en.wikipedia.org/wiki/Fermi_problem).

Executing a function on a smart contract (an object instance) on the Ethereum
virtual machine, updating internal state etc, takes a few minutes.

On a Mac, the overhead to pass a message to an object is measured in
nanoseconds on a modern machine.

So there’s is a 10 orders of magnitude difference: Ethereum needs to be 10
billion times faster.

That’s 33 Moore’s law doublings. 50 years away from being as complex and
fully-expressed as today.

So we’re in the equivalent of 1970 – which feels about right.

Web3 is waiting for minicomputers. Even that’s a long way off from today. In
the minicomputer boom around 1980, in our history, [a single NAND gate cost 8
cents, wholesale](/home/2021/03/02/microcode): In 1981 money, a single iPhone
would cost "$1.4 billion in parts, no margin."

We’re still waiting for our Unix moment, locking down the fundamental
concepts, the system that takes the network and time-sharing for granted,
giving us the native programming language and system calls to bootstrap up to
the next layer of emergent complexity.

We’re pre GUI; direct manipulation and the desktop metaphor has yet to be
figured out. There are no SDKs. Development is still close to the metal.

It gives me a rough handle on the scale of work to be done.

1970 doesn’t mean that web3, this new epoch of computing (if that’s what it
is), is unusable. Far from it. People in the real 1970 were making video
games! The personal computer had already been imagined and prototyped!

This analogy helps me have a view on questions like: are NFTs the final form
of that concept, or do we have some way to go to digital ownership?

I think what NFTs _want_ to be like is the MP3. The Fraunhofer Institute’s
invention of the MP3 (and their licensing approach) unlocked a whole industry
including consumer ownership of digital music, online music stores and
streaming, and digital devices like the iPod (which paved the way to the
iPhone).

But the MP3 file format was invented in 1989 so - if we’re on a similar
trajectory - then NFTs have conceptually the right frame but are 20 years too
early.

The question is: how do we accelerate 50 years to 20 years or to 10 years?

There were multiple generations of computers between 1970 and the networked
smartphone. It wasn’t a steady evolution.

Maybe there would be scope in imagining the next generation of web3, already.
Are there other ways to achieve a global, zero-trust, persistent, shared
object runtime – and can it be built? Perhaps Microsoft or Google have
warehouses of genius engineers doing just that, attempting the generational
leapfrog.

Or maybe it would be worth bullying a Smalltalk-like expressive development
environment into existence, sitting atop today’s Ethereum world computer,
however slowly it run, just to see what could be created with that new clay.

IF REAL! The alternative view is that web3 and all of the above _isn’t_ real.
There will be ways to achieve digital ownership (if that’s even important!)
without baking it into the physics of a future world computer.

It could be that part of the appeal of web3 is that it’s a new glass bead
game.

(Whether it has 1,000 year appeal like THE Glass Bead Game, Hermann Hesse’s
abstract and beautiful fictional game at the heart of [his 1943
novel](https://en.wikipedia.org/wiki/The_Glass_Bead_Game), our descendants
will find out. So let’s lowercase it for now.)

Where else can you manipulate a novel set of symbols and bounce between code,
social dynamics, arts and economics? There are endless permutations.

And perhaps - per Hesse - it’s best left to a caste of esoteric monks revered
yet safely isolated from the rest of society…

I’m not saying there is nothing else there, or that the nerd-sniping joy of
web3 is the only value (I happen to believe there is something real here), but
alongside the gambling drive which comes from the financial component of this
emerging tech stack, I feel like novel symbol manipulation is a big part of
the early appeal for many.

Which is a risk. I kinda vaguely feel like physics burnt a couple decades on a
similar pursuit: string theory. A consumingly absorbing idea for whole
communities, but where did it go?

So perhaps it’s all a mirage. For the sake of argument, let’s assume it’s not.

My hunch and my heuristic metaphor:

If the web3 world computer has only just reached 1970 then, first, don’t
expect too much. There’s real utility to be found but in very prescribed use
cases. But also, second, there are wild and unrecognisable transformations to
come. There is room for imagination and invention.
