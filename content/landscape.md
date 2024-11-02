# Presence in VR should show tiny people, not user avatars

Since [picking up a virtual reality headset](/home/2022/04/20/vr) a couple
weeks ago, I’ve been asking myself: how should the future operating system for
apps work?

Like: how do you write docs? How do you collaborate on a deck? How do you
launch your messaging app? Games are easy because they get to be weird. But
for apps you need standard behaviours.

So I’m trying to think through this from first principles and see what comes
to mind…

ALSO keep in mind that I have become obsessed with the overview mode in
[Walkabout Mini Golf](https://www.mightycoconut.com/minigolf). It’s incredible
to have the _“Godzilla’s eye view”_ (as I called it in that post at the top):
gazing over the course with all its trees and ponds, a mountain halfway up my
chest. And then being able to literally kneel on the floor and stick my head
into a cave, examining closely all the intricate objects and furnishing in the
rooms inside.

For me, the key difference between a screen-based user interface and a VR-
based UI comes down to this:

If there is a small icon on my laptop screen, no amount of me moving closer
will magically add resolution. But if there is a small icon in VR, leaning in
will resolve more detail.

Quick maths: let’s say an icon (like a user profile pic) is 1cm across and
apparently 20cm away, and I lean in to halve that distance to 10cm. _The
number of pixels dedicated to that icon increases 4x._

You can pack a ton more information into 4x pixels!

This is crazy fundamental. On our phones, we “see” with our fingers - panning,
swiping - but although you can pinch-zoom on a photo, there’s nothing you can
do that lets you peer closer at an interface element and get more data than is
already there. You can in VR. And compared to tapping or pointing with an
input device, moving your head a small amount is zero cost.

Like, imagine looking at the tiny wi-fi icon in the top bar on your home
screen. Simply lean your head towards it a little (unconsciously) and you are
able to read the name of the current wi-fi network; buttons for commands
appear.

Seeing is an active process. We move our eyes, heads, and bodies to see the
whole time.

This is the topic of J. J. Gibson’s incredible 1979 book [The Ecological
Approach to Visual
Perception](https://www.amazon.co.uk/exec/obidos/ASIN/0898599598) _(Amazon),_
which counters then-conventional psychological research in perception which
strapped the subject’s head in place. Instead: "natural vision depends on the
eyes in the head on a body supported by the ground, the brain being only the
central organ of a complete visual system. When no constraints are put on the
visual system, people look around, walk up to something interesting and move
around it so as to see it from all sides, and go from one vista to another."

Here’s a quote I noted down [last time I read
it](/home/2004/04/13/how_dogs_perceive) (2004):

_This is why to perceive something is also to perceive how to approach it and
what to do about it._ Information in a medium is not propagated as signals are
propagated but is contained. Wherever one goes, one can see, hear, and smell.
Hence, perception in the medium accompanies location in the medium.

(Designers may like to know that Gibson _also_ coined the term
_“affordances,”_ used heavily in HCI and interaction design thanks to Don
Norman, and this book is the underpinning for why visual perception and action
are intimately connected.)

SOME RELATED LINKS:

I tried controlling my desktop cursor with head tracking last year and [it was
tantalising](/home/2021/03/12/pointer_control): "It is _so close_ to being
something I would use in preference to a mouse… or rather, alongside one."

So that’s why I’m a believer that computer interaction can be way more
embodied than it is today.

Another reference point is the [zooming user
interface](https://en.wikipedia.org/wiki/Zooming_user_interface) _(Wikipedia)_
which has been a concept for decades. I’ve built prototypes in the past, and
it’s actually kinda neat to (for example) zoom in from a document icon to edit
the document itself. BUT also frustrating: cognitively it feels like you end
up with too much stuff in your head. Your brain misses the necessary cues to
deallocate information stored from old screens. You need the attentional
ergonomics of the Doorway Effect ([as previously
discussed](/home/2021/04/23/star_wars)) to help with focusing.

My point is that the possibilities of the future user interface are
_wiiiiiide_ open. Building on these kind of ideas is what I have in mind.

If _“natural zooming”_ is a UI primitive for our future OS then another
fundamental is _presence._

VR and multiplayer are intrinsically linked. Virtual reality is a medium that
has emerged in the networked age. _Of course_ apps will be multiplayer and
collaborative. Why would they be otherwise?

The metaverse, right?

A couple years ago, I was speculating on how to retrofit “multiplayer” into
today’s desktop or phone operating system. One idea was _noisy icons:_

Imagine seeing ripples around the Google Docs app as if there were some deep,
distant activity. Open it… and there’s a particular document humming with
comments. You listen at the door, you can tell who’s active, and the frequency
of the interactions, but not what they’re saying precisely… a ping as your
name is mentioned (the notification of which wouldn’t have bubbled all the way
up to your home screen as it’s not important enough, but since you’re here) -
so you enter and join your colleagues.

…and this is kinda hard to imagine actually being implemented today, right?

But with VR, where the OS is being built from scratch, maybe this is the kind
of paradigm that can be there from the get-go.

Long story short: you should be able to see which of your friends are “in” an
app before you launch it, and see who is “around” in the app while you’re
using it. Presence.

Today “presence” means showing a green _I’m Online!_ marker next to a floating
avatar or, at best, Figma-style cursors charging around on screen. It works
but it’s oh so abstract.

**How it works today:**

Meta Quest 2 has a button that brings up a universal menu. It hovers in space.
It doesn’t add more detail if I lean closer (it just looks sharper). It
should!

[You can see the menu in this
review.](https://www.polygon.com/reviews/2020/9/16/21437762/oculus-
quest-2-review-virtual-reality-vr-facebook-oculus-power-resolution-tracking)
_(Search for “The best place to see the changes in the hardware’s displays is
currently in the menus.”)_

The app launcher gives me a grid of images, hanging in space on the same
virtual screen.

**How could it look?**

I want to see apps. I want to see if an app is busy or rather: occupied (to
keep the spatial metaphor). If I peer closer, I want to pick out my friends.
Let’s use that zooming UI possibility and let me discern both crowds and
individuals, both at once.

This doesn’t have to look like a virtual screen hanging in space. Nor does it
have to look like a 3D rendered virtual office (or whatever). That’s
skeumorphically cargo-culting the real world. We use abstractions because
they’re more efficient for certain kinds of thinking.

In my head the app launcher looks like Peter Molyneux’s 1989 video game
[Populous](<https://en.wikipedia.org/wiki/Populous_(video_game)>)
_(Wikipedia)_ which invented the _“god game”_ genre.

In Populous: You look down at an isometric landscape on your desk. You see
people scurrying about. If a building is busy, there are lots of people there.
([This Populous review embeds a gameplay
video.](http://www.indieretronews.com/2019/06/populous-brilliant-strategy-
game.html) Check it out!)

So that’s what my imagined home screen looks like: a landscape of apps,
presence shown by people near the apps. But not mini profile pics. We only
have those because of the limitations of desktop screens. Let’s have teeny
little people instead. When you lean closer, more pixels are dedicated, and
you can recognise the faces of your friends.

Ok this isn’t all you need for a VR-based multiplayer operating system, not by
a long chalk. But I’m into the fact that there are a ton of new interaction
design primitives to use on old problems.

And perhaps this is a neat starting point to open up the design space. With
PCs you have the desktop metaphor. With VR, how about the landscape metaphor?
