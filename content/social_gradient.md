# Designing multiplayer apps with patterns from architecture

I’ve found myself looking at architecture to pick up hints on designing
multiplayer apps. Or rather: the coming ecosystem of multiplayer apps.

The web is social in lots of ways. Zoom calls are high-bandwidth group video;
Google Docs are low-bandwidth group presence and chat. Discord has at-my-own-
pace group interaction and live voice channels.

These islands of social interaction are joining up. [Increasingly the web is
going multiplayer](/home/2021/09/27/multiplayer) _(and yes yes the metaverse
too)_ and we step between them – desktop to Slack to Zoom to Figma.

BUT – how should it _feel_ to move between them?

It’s obviously abrupt to hit a Zoom link in a (private) calendar and suddenly
join a full-on video chat, webcam ON, microphone ON, with a ton of people
there. Sometimes surprisingly so.

So the designers have spotted this experiential bump in the road, and now
video chat apps tend to have this interstitial window: you get to see if there
are people already in the meeting first, there’s a webcam preview to check
your hair, then your hit _“Join”_ at your leisure. Smoother!

The question is: is there a general approach to this? How do we design
transitions between different interaction modes and social contexts?

Here’s [A Pattern Language](https://www.amazon.co.uk/Pattern-Language-
Buildings-Construction-Environmental/dp/0195019199) _(Amazon UK)_ by
Christopher Alexander, Sara Ishikawa and Murray Silverstein.

**A Pattern Language: Towns, Buildings, Construction** is a 1977 book on
architecture, urban design, and community livability.

… “All 253 patterns together form a language.” Patterns describe a problem and
then offer a solution. In doing so the authors intend to give ordinary people,
not only professionals, a way to work with their neighbors to improve a town
or neighborhood, design a house for themselves or work with colleagues to
design an office, workshop, or public building such as a school.

It’s a brick of a book which is my excuse for never having read it cover to
cover.

HOWEVER – it’s neat to dip into.

For example…

This is a pattern about how to configure rooms in a single building like a
house or an office.

I’ll quote a bunch from the book and add some comments.

Unless the spaces in a building are arranged in a sequence which corresponds
to their degrees of privateness, the visits made by strangers, friends,
guests, clients, family, will always be a little awkward.

The connection to social software: instead of “degrees of privateness,” I’m
thinking more like “degrees of intimacy” or maybe “degrees of social
intensity.” So video calls on Zoom are _hotter,_ socially, than sharing cursor
positions while viewing a Google Doc together, which is _cooler._

_A Pattern Language_ gives an example.

In Peru, friendship is taken very seriously and exists at a number of levels.
Casual neighborhood friends will probably never enter the house at all. Formal
friends, such as the priest, the daughter’s boyfriend, and friends from work
may be invited in, but tend to be limited to a well-furnished and maintained
part of the house, the _sala._ This room is sheltered from the clutter and
more obvious informality of the rest of the house. Relatives and intimate
friends may be made to feel at home in the family room (_comedor-estar_),
where the family is likely to spend much of its time. A few relatives and
friends, particularly women, will be allowed into the kitchen, other
workspaces, and, perhaps, the bedrooms of the house. In this way, the family
maintains both privacy and pride.

In one environment…

In an office the sequence might be: entry lobby, coffee and reception areas,
offices and workspaces, private lounge.

And another:

In a house: gate, outdoor porch, entrance, sitting wall, common space and
kitchen, private garden, bed alcoves.

Your front door doesn’t open directly to your bathroom, right?

There’s a hallway then there’s a reception room – [even the lighting
changes](https://www.westinghouselighting.com/color-temperature.aspx). You
chooser a cooler 3000K bulb for the hall, and warmer 2700K bulbs for the room
you hang out in with guests.

What this means for software: there’s too much jumping straight to video. I
get a kind of social-cognitive whiplash from doing it.

Instead the interface should be more like:

The designer’s job is to move the user up and down this social gradient with
the user maintaining agency and anticipation of what’s next.

So that interstitial window before a video chat kicks of can be thought of as
a lobby or a porch. This what pattern 130 is about.

Arriving in a building, or leaving it, you need a room to pass through, both
inside the building and outside it. This is the entrance room.

In a social software sense: this is the threshold between cool presence and
hot video.

The pattern says that this isn’t just a threshold to be quickly passed over,
but that the liminal room has some vital features – and it unpacks them. You
should read the whole thing. To pull out just one: windows.

_1\. The relationship of windows to the entrance_

(a) A person answering the door often tries to see who is at the door before
they open it.

(b) People do not want to go out of their way to peer at people on the
doorstep.

(c) If the people meeting are old friends, they seek a chance to shout out and
wave in anticipation.

What could _good windows_ mean for Zoom, say, or Google Meet, or FaceTime or
any of the others?

Entrances matter! I talked last year about giving a talk online, and the
platform allowing me to gather people in the lobby (I could see their names
listed from the inside) and then [throw back the curtains to let them all at
once](/home/2021/06/15/doorways). Built great energy. Same idea as this.

Finally:

At the main entrance to a building, make a light-filled room which marks the
entrance and straddles the boundary between indoors and outdoors, covering
some space outdoors and some space indoors. The outside part may be like an
old-fashioned porch; the inside like a hall or sitting room.

It’s a lovely pattern. Fizzy with inspiration.

There’s a bit in it about having handy shelves, because people go into and out
of houses while carrying parcels.

What’s the equivalent for Zoom? Well, what if - on the way in, just before the
call - you could drag the documents you want onto a shelf in that interstitial
window, so you don’t have to hunt for them on your file system when you want
to share screen? And, on the way out, what if you were given a window with a
list of all the links shared in chat, or the email addresses of everyone there
ready to copy and paste, or maybe a list of actions from the meeting (perhaps
captured with voice recognition whenever somebody puts a single finger in the
air and says _“action item”_).

I wonder how much Zoom fatigue would be reduced if the transitions were cared
about.

Anyway I’m not just talking about Zoom – we spend a lot of time going in and
out of these social spaces, hot and cold, and they’re gradually connecting
together into a continuous multiplayer fabric, made out of all kinds of apps
and websites. I’m spending a bunch of time this year working on that, it turns
out.
