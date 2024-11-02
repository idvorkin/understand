# Golems, smart objects, and the file metaphor

I often wonder what it would be like to have _“Open File”_ and _“Save As”_ for
lightbulbs, online grocery stores, and messaging apps.

It’s hard to explain what files used to be like because they’ve changed so
much.

**Files used to be independent from apps.** The way it used to work was that
you would open a standard file format in an app, say a TIFF (image) or an RTF
(text file) or an MP3, and you would play the file or edit it. And then you
would open the exact same file in a different app for different capabilities.

Nowadays, if an app deals with files at all, you import files into the app and
maybe export versions later, but the working doc itself is sealed in a
library, or in a special format that nothing else can open.

**Files used to be objects you could manipulate.** Nowadays apps take care of
versioning, and sharing, and often organising. But before, you would duplicate
the file object directly, or drag it onto a chat window, or whatever. You
can’t drag a Google Doc; the file isn’t a directly manipulable “file” so much
as the visual depiction of a save point.

The upshot was that you owned your own files. And when a new application came
along, it was exciting because you could try it out by using it with those
exact same files, maybe switching back, maybe not.

So when I talk about files, I mean these

(And yes, I know it was never as clear cut as this, but in an idealised kind
of way.)

What is a file?

**There’s a technical answer.** If you do the archeology and go back to source
code from the 1970s, a file is a handful of properties: an address on disk; a
size (i.e. how long to read the disk for); and some metadata like which owns
these bytes, and do these represent an executable app or a document, and so
on. [Here’s the code.](https://www.instagram.com/p/CKwJzrSpgWO/) It’s less
than a page. (Photo from _Lion’s Commentary on UNIX 6th Edition,_ [as
previously discussed](/home/2005/09/24/what_is_a_process).)

But that’s not a definition that works for “documents” on cloud services,
where a saved Google Doc is more likely to be a bundle of dynamic lookups from
a database, rather than a run of bytes on disk. So…

**There’s the design answer.** A file is what it looks like: an icon. There’s
a fantastic oral history of the hamburger menu _(the three-lined menu button
that you see in the top corner of a ton of websites),_ and it goes all the way
back to the Xerox Star, which was the first commercial computer to actually
_have_ windows, menus, a mouse, etc. The history includes commentary from Dave
Canfield Smith who mentions "icons, which I’d invented at PARC for my thesis."

And he makes the distinction between file icons and the hamburger menu, THUS:

I don’t understand the fascination with the hamburger menu symbol, because
it’s not even an icon–it’s just a symbol. Icons had both visual and machine
semantics, whereas this menu button had only the former. You don’t do anything
with a menu. It just sits there on the screen. You poke at it and a menu pops
up, you move the cursor away and the menu goes away. That’s all it does. **An
icon is an object in a metaphoric world that you can do things with in the
real world,** the world that is being modeled.

That’s the key quality. Files are meaningful to computers, but they are _also_
meaningful to users, and _both_ can manipulate the same object. The two of you
inhabit different worlds, but you’re talking about the same thing.

There’s a great paper from Microsoft Research called, simply, **What is a
File?**

For over 40 years the notion of the file, as devised by pioneers in the field
of computing, has been the subject of much contention. … we suggest that files
continue to act as a cohering concept, something like a ‘boundary object’
between computer engineers and users.

A _boundary object_ is a term from sociology. [From
Wikipedia:](https://en.wikipedia.org/wiki/Boundary_object) boundary objects
"have different meanings in different social worlds but their structure is
common enough to more than one world to make them recognizable, a means of
translation."

The user can tell the computer what to do with a file without having to know
the details of the inode structure or how to program their instructions; the
computer can make a file available to a user without having to anticipate
every single goal that a user may have in mind.

The “boundary object” quality of a file is incredibly empowering, magical
really, one of the great discoveries of the early decades of computing.

The file made sense for desktop computers and bytes stored on disk. What could
the file be now, in the era of the cloud and smart devices?

There’s a clue, I think, in this kids’ toy, the [Yoto
Player](https://www.yotoplay.com/pages/player): "A carefully connected screen-
free speaker. Made for children, controlled with physical cards and playing
only the audio content you want them to listen to."

It’s cute!

It reads bedtime stories!

Kids “program” it by inserting a card!

My niece has one of these. She loves it.

What neat is that you can [make your own
cards](https://www.yotoplay.com/pages/makeyourown). I’m guessing the cards are
just blank playing cards with a RFID tag inside. You program each card using a
phone app. Once programmed, Yoto Player will play the relevant audio or
podcast, and show pixel graphics on the front of the device.

BUT ALSO you can draw on and decorate the card, and you can keep them in a
[snazzy green
wallet](https://www.yotoplay.com/collections/accessories/products/portfolio-
card-holder). So you can match the cards with interests, put educational ones
with your school stuff, fun ones with different toys, private ones with your
diary, keep some back for treats… all that good stuff. And all without Yoto
having to pre-decide what kids might want to do (and having to design an app
to do all of it).

**Yoto Player is a golem.** The [golem](https://en.wikipedia.org/wiki/Golem),
the "animated anthropomorphic being that is created entirely from inanimate
matter" from ancient Jewish folklore. A statue, an ancient robot, but not
autonomous. Specifically:

It was believed that golems could be activated by an ecstatic experience
induced by the ritualistic use of various letters of the Hebrew Alphabet
forming a “shem” (any one of the Names of God), wherein the shem was **written
on a piece of paper and inserted in the mouth** or in the forehead of the
golem.

If you think of apps, or executables, as essentially inanimate clay - code
which is pure potential, and brought to life by the loading of the user’s own
file - then the file is the _shem,_ or rather a generalised kind of shem, not
a divine name as such, but a set of instructions, inserted into the mouth.

_(Now go and read Ted Chiang’s sci-fi short about golems and software[Seventy-
Two
Letters](https://ia802706.us.archive.org/33/items/TedChiangSeventyTwoLetters/Ted_Chiang_72_Letters.pdf).)_

I have 1 (one) smart plug. I used it to control the Christmas tree lights (so
I didn’t have to reach back on the floor twice a day) then nabbed it to
control a lamp across the room from my desk. Currently it has been
requisitioned to monitor the power usage of a water pump: I’m concerned there
is a slow leak and the pump is switching on at odd times in the night. The
plug will confirm this for me.

I would love to encode these configurations, and more, onto cards: the name,
the room, who can use it, maybe some power user features such as where logs
are sent, and how alerts are dispatched, and so on. These cards, physical or
virtual, would live in a stack somewhere (on my bookshelf or in a shared
Dropbox), and I could swap back and forth, and other family members would be
so empowered too.

**What about lightbulbs?** Lighting scenes are a pain to create. A standard
“file” for lights, not just bulbs but whole setups, would allow for

Do I literally mean that the lightbulb needs a little slot like the golem’s
mouth, into which you insert your instructions stamped on microfiche? I’m
tempted but no. But metaphorically.

**What about an online grocery store?** If my preferences and purchase history
were a file, it would make it a ton easier to switch from one store to
another. But that’s just export/import, service portability.

What makes the file, as a metaphor, so magical is that _other, unexpected
software_ can open the same thing.

So what I’m imagining is a _“Let’s Go Vegan”_ app which loads the grocery
file, deletes any meat and dairy from my purchase history (so I don’t get
tempting recommendations) and seeds my shopping basket with a starter pack. Or
a _“Shop Local”_ campaign that looks at my purchases and sets up accounts (and
regular orders) with appropriate neighbourhood stores – or vice versa, if the
supermarket can beat them on price and that’s what I want!

The trick is that these aren’t apps calling an API, because an API is bespoke
to every store, and it’s not a matter of export/import because that misses the
point of the file being a shared object that multiple different apps operate
on simultaneously: a genuine shared file.

_(APIs mean that a healthy ecoystem is a tough N^2 problem: every service
needs to be tested with every other service. Shared files reduce this to an N
problem. Each service needs to be tested with precisely one other thing, the
file spec.)_

I’m afraid this opens up more questions than it answers.

Let’s pretend I somehow got to run my [Orthogonal Technology
Lab](/home/2021/01/21/otl) – this is research programme #1. There’s no new
technology here. Just a series of ideas to explore that seems like they might
unlock a tech ecosystem with good values, and the trick is to chase it down
with small-scale prototypes, to begin with, and then speculative specification
docs, and sketches of business models, etc, publishing it all, and using the
whole activity to demonstrate to both founders and policy-makers that another
future is possible, basically continuing the pile up the whole edifice until
someone decides to come along and do it.
