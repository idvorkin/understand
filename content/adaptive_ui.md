# Apps are too complex so maybe features should be ownable and tradable

Software is too complicated. User interfaces have too many commands. Perhaps
the answer is an in-app free market economy.

I subscribe to the excellent [Hardcore
Software](https://hardcoresoftware.learningbyshipping.com) newsletter which
narrates the evolution of the PC and desktop software. It’s by Steven Sinofsky
who was at Microsoft from 1989, oversaw development of multiple versions of
Microsoft Office as it was created and scaled, and ended up as president of
the Windows devision.

With Office 2003, Microsoft was able to see the actual commands used for the
first time.

Nobody used all the features, but everyone used a different set.

At a deeper level, most in a company might not use a feature such as Track
Changes (or Redlining) in Word. But their lawyer would. And contracts or legal
letters might arrive via email for review. _Rarely used features became part
of the work of others._ This network of usage was a key advantage of Office.

What to do?

I’m into **Adaptive Menus** as an approach.

The first new mechanism, called “Adaptive Menus” or, later, “Personalized
Menus” were an attempt to make the top-level menus appear shorter by showing
the most popular items first. After a few seconds (or after pushing a chevron
at the bottom of the menu) the menu expanded to show the full contents. _As
you used the menus, items you used often were promoted_ to the “short” menu
and items you never used were demoted to the “long” menu.

It’s like frequently-used light switches in your house magically getting
bigger.

But it didn’t help for Microsoft’s core problem which was _discoverability._
Users kept on requesting features which were already in the product.

(The eventually solution was to replace menus with visible commands and icons,
making it easier to explore: the Ribbon.)

_Kai’s Power Tools,_ in the mid 1990s, was known for providing awesome
Photoshop effects and also for wild experiments with the UI.

[Here’s a deep dive into the interface of
KPT.](https://www.mprove.de/script/99/kai/index.html)

Magic lenses! Single-purpose rooms! A dedicated tool "meant to create
collections of special looking orbs."

Also, _“Unfolding Functionality.”_

This deep dive describes this philosophy as fading out commands when not
needed.

But [the KPT Wikipedia
page](https://en.wikipedia.org/wiki/Kai%27s_Power_Tools) is more specific:

The program interface features a reward-based function in which a bonus
function is revealed as the user moves towards more complex aspects of the
tool.

This is more how I remember it.

I _think_ what would happen is that you would use a particular feature or
filter or parameter, and as you used it you would accumulate stars. At a
certain number of stars, more advanced features would unlock.

Which is another way to deal with clutter, right? It’s progressive disclosure:
the user and interface grow in sophistication together.

Neither Office’s Adaptive Menus nor KPT’s Unfolding Functionality is quite
right. (Discovering new features is hard. A feature, when you want to go back
to it, might be a different place.)

BUT what they both do is they atomise functionality.

Once functions and commands exist as atoms, the user interface can be
displayed according to some kind of logic - unfolded with use; reorganised by
context, etc.

_Feature flags_ are a super common engineering pattern for turning feature
“atoms” on and off dynamically.

For example: you have an app with a button that you only want to show to
people inside the company, because the feature is still being tested. So you
set a flag for that feature for all the users who you want to see the button,
and they see it, and for everyone else it’s like the feature isn’t even there.

Unpacking this… [Feature Toggles (aka Feature
Flags)](https://martinfowler.com/articles/feature-toggles.html) (Pete Hodgson)
gives four categories of feature flags:

Kai’s Power Tools, through the lens of feature flags, makes up a fifth
category: adaptive toggles.

I’m calling them adaptive in the spirit of the [lost Adaptive Design
movement](/home/2020/08/26/adaptive_design) from the early 2000s: software is
“adaptive” if it is co-created by design and user, and conforms to individual
user behaviour.

A sixth category might be _pick-your-own toggles:_ feature flags where the
user is in control of what features are off and what features are on.

**BUILD #1: Pick-your-own feature flags**

This is 50% of an idea.

Imagine Microsoft Word but it comes as a plain text editor. No
bold/italic/etc. The only commands are open, save, copy, and paste.

You get used to it. Then one day you decide you’d like to style some text… or,
better, you receive a doc by email that uses big text, small text, bold text,
underlined text, the lot.

_What the hey?_ you say.

There’s a notification at the top of the document. It says: _Get the Styles
palette to edit styled text here, and create your own doc with styles._

You tap on the notification and it takes you to the Pick-Your-Own Feature Flag
Store (name TBC). You pick the “Styles palette” feature and toggle it ON.

So far this is pretty much like the [browser flags in
Chrome](https://developer.chrome.com/blog/browser-flags/) – experimental
features in the web browser are hidden behind toggles which are user opt-in.

BUT the difference is that the features aren’t experimental. They are fully-
rounded, user-facing, feature “package.”

So the user builds up the capabilities of the app as they go.

The downside? It’s still really hard to _discover_ features. How do you know
that text styles (or drawing, or collaboration, or any other feature
“package”) is available, unless you go hunting? And why would you go hunting
if you don’t already know the feature exists.

That’s why it’s only half an idea.

**BUILD #2: Multiplayer, purchasable, tradable, giftable feature flags**

The thing is, we’re not in Microsoft Word, we’re in Google Docs – and it’s
multiplayer.

I’ve been tracking the [emerging multiplayer
web](/home/2021/09/27/multiplayer) for a while. The fact that our day-to-day
work apps, like Slack, Notion, Figma, and Google Docs _all_ have a sense of
live presence of colleagues is a big deal. Pretty soon we’ll be able to take
it for granted in any app. Presence and collaboration will also be part of any
future-VR-based operating system – I’m convinced of that [after recent VR
headset mucking around](/home/2022/04/20/vr).

So what if you’re collaborating with your lawyer in Google Docs, and you can
see from their avatar that they have the “Track Changes” feature flag
activated?

Because you’re in the same doc, you can use it together.

And maybe if you want to use it again, they can just… gift it to you?

Could app feature flags be tradable and giftable? That would answer the
discovery problem and the “store” problem.

What we’re talking about is feature flag _ownership:_ a user _owns_ their
feature flags, and they carry features with them in a multiplayer space, and
can use them together with other people.

Which… kinda parallels the physical world, right?

Like: if you’re having a workshop in a meeting room, then it’s generally one
person who brings the post-its and the pens. It’s part of their job.

It should be the same on a Zoom call. You shouldn’t sit on a call waiting for
a host. You should sit on the call waiting for the person who has the screen
share feature flag, and the annotate screen feature flag, and so on.

What I’m talking about here is a marketplace: maybe a bunch of features in
Zoom are free, but you pay $10 for the screen share feature flag, or $100 if
you want the “make my webcam look pretty” filter. You can gift it to another
user later if you want.

**BUILD #3: ok yeah NFTs**

I continue to keep a close eye on web3, [as I said in
January](/home/2022/01/14/stake_patronage):

Here and there are glimpses of new ways of storing files, new ways of owning
and providing access to data, new ways of asserting identity, new forms of
payments …

I keep a personal running list of what I find interesting in the Web3 gold
rush, in the hope of spotting something useful in its fundamentals that has
immediate applicability.

And maybe here’s one?

NFTs _(non-fungible tokens)_ are basically database primary keys that can be
bought and sold, outside the originating platform.

What’s key about a NFT is that it is _owned_ by a user.

Primary keys can point to anything, and mostly right now they point to jpegs
of cartoon apes, pixellated portraits, blobs of text, and some very cool art
made by excellent artists (also some terrible art). There are a ton of scams
in this space, so you have to squint a little to see through.

There is also an idea called **Functional NFTs** which is when the primary key
is meaningful to a particular app or service, and it unlocks feature.

_Look, what I’m saying is: why not NFT-backed tradable feature flags?_

With NFTs you get a whole ecosystem of ownership, marketplaces, dynamic
pricing, for-free and for-pay trading, and so on.

If you want to build ownable, tradable feature flags, then it’s actually a
relatively sane architecture decision to make use of this chunk of the
emerging web3 tech stack to provide it. You might (as the rest of the tech
stack comes into play) end up actually having to write _less_ code?

Maybe the ownership experience of NFT-backed feature flags would actually be
_greater_ than non-NFT-backed feature flags, and you would be able to charge
more? Expensive to provide features (like ones that consume a lot of
bandwidth) could even cost more. Applications could end up with a business
model that feels more like game DLC?

…but with some fascinating behaviour around users optimising their own apps
around different roles (a viewer, a host, a facilitator, an editor, a teacher,
etc) to represent the roles they have in their teams, and - in this
multiplayer world - mutually learn from one another about how to adapt and co-
create their own user interfaces.

3rd party marketplaces to provide and trade feature flags would arise.

And then there should be some fun features too. It’s not all whiteboards. What
would it mean to have a rare and therefore somehow valuable feature flag? What
would it feel like to be gifted one?

For me, this is maybe something to draw out of web3 – either just as
inspiration or actually as some real tech.

Anyway. Adaptive user interfaces, avoiding clutter, adding social discovery,
NFT-backed feature flags. Apps would start really simple and then grow in
complexity around you as you discover features by meeting others. Add in a
business model and it sounds like a real-world economy, right? Lots of user
experience and design work to figure it out. Can you imagine Microsoft Office
2026 working like this? Something worth sketching I think.

_Thanks to Sofi Lee-Henson, Pearl Pospiech, and others
at[Sparkle](https://sparklespace.com) for the work and imagination in
developing these thoughts together. Standard disclaimer: this is super
speculative. Posting now to generating conversation and get my thoughts lined
up._
