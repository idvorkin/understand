# Clues for software design in how we sketch maps of cities

There’s a remarkably simple notation for sketching cities, and I think it
points at a better way to design software.

Kevin Lynch was "an urban planner who carried out pioneering work on people’s
urban cognitive maps from the 1950s."

And:

As a planner, Lynch was interested in analysing the urban form, and in
particular identified the criterion of the ‘legibility’ of a cityscape which
he defined as ” the ease with which its parts can be recognized and can be
organized into a coherent pattern”

… His method involved externalising the ‘mental images’ that city-dwellers
have of their cities, through interviews and sketch-mapping exercises.

(From these [lecture notes on the work of Kevin
Lynch](http://homepages.phonecoop.coop/vamos/work/lecturenotes/sun/LectureNotes/Env4_EnvCog/environmental9.html).)

This shared “mental images” is the subject of Lynch’s book [The Image of
City](https://en.wikipedia.org/wiki/The_Image_of_the_City) (1960) (and it blew
my mind when I read it in - checks notes - 2003).

**[Here’s an example of one of Lynch’s maps:
Boston.](https://www.researchgate.net/figure/Lynchs-mental-
maps_fig2_309728517)**

What you’ll see from that map is that it’s totally recognisable as a city, and
you could totally use it to navigate, but it’s also what you would scribble on
the back of a napkin. It’s also way more memorable. If you gave me a glimpse
of Boston from Google Maps and asked me to sketch it for someone else, I can’t
imagine it would include any of the salient details. But given a Lynch map, I
bet I could pass on the most relevant bare bones, just from memory.

So Lynch has managed to capture what is essential about maps for (a)
understanding, and (b) communication.

Lynch’s insight is that these scribbled maps use a notation of only five
elements. From those earlier lecture notes, there are:

Out of these five elements, you can build an “image” (in Lynch’s terminology)
of the city.

_Landmarks_ grab my attention, for this reason: they come up in _Mind Hacks,_
in a chapter about memory and the hippocampus.

We know that the human brain has specialized mechanisms dedicated to
remembering landmarks, and that (interestingly) this region and those nearby
seem to be responsible for giving humans and other animals a sense of where
they are in space. Brain images of people navigating through virtual
environments has shown that _even if we don’t consciously recognize something
as a landmark it still triggers a response in this specialized part of the
brain._

_(Quick plug:[Mind Hacks is now available in
Chinese!](https://item.jd.com/13054358.html) Check out the 11 second product
video with perky music on that page. That brings us up to 7 translated
editions, which feels pretty special.)_

So what I find intriguing is that we, us humans, appear to have a “landmark
sense” that we all share.

Which is why, I guess, you can follow directions to go down the street and
turn left at the fountain, and if you pass a cathedral then you know you’ve
gone the wrong way – because such a landmark would certainly have been
mentioned.

The question is this:

Do Lynch’s other elements also have neurological underpinnings?

And a follow up: If so, how could that be useful?

The reason I ask is because of the Doorway Effect, which is something that
happens also in physical space and not outdoors but indoors: "Memory was worse
after passing through a doorway than after walking the same distance within a
single room."

… some forms of memory seem to be optimized to keep information ready-to-hand
until its shelf life expires, and then purge that information in favor of new
stuff. Radvansky and colleagues call this sort of memory representation an
“event model,” and propose that walking through a doorway is a good time to
purge your event models because whatever happened in the old room is likely to
become less relevant now that you have changed venues.

What’s especially intriguing about this study…

The Doorway Effect appears for real doorways. But ALSO: "It doesn’t seem to
matter, for instance, whether the virtual environments are displayed on a 66”
flat screen or a 17” CRT."

So, to review the precarious stack of speculation that I’m on:

Which provokes two thoughts:

Given there’s an explosion in software to accrete and organise knowledge, is
the page model really the best approach?

Perhaps the building blocks shouldn’t be pages or blocks, but

Or rather, as a knowledge base or wiki develops, it should - just like a real
city - encourage its users to gravitate towards these different fundamental
elements. A page that starts to function a little bit like a road should
transform into a slick navigation element, available on all its linked pages.
A page which is functioning like a landmark should start being visible from
two hops away.

It would be interesting to investigate exactly what the minimal level of
physical appearance is required to trigger the automatic behaviour of
loading/resetting human memory and associations.

Like, following a hyperlink might not activate the neurological automation.

But what if there was a zooming out animation, or a change in colour, or the
old page slid off to the side?

What’s the minimum you need to trick your brain into believing that you’re
moving around an environment?

And could design features as simple as these make tools like Notion, Roam,
Obsidian, Evernote and other note taking software, Wikipedia, etc, _radically
better_ for organising, navigating, sharing, and internalising knowledge, for
individuals and for teams? If so, can you imagine the efficiency gains and the
new ideas that could emerge?

_Hippocampus ergonomics._

It would be worth a research lab and a year or two, I think.

One final and quite literal idea: Could Lynch-style maps be generated
automatically, and could this be an interface to Google Maps?

This paper believes this is possible: [A computational approach to ‘The Image
of the
City’.](https://www.sciencedirect.com/science/article/pii/S0264275118309776)

Although: "Out of the five elements, landmarks were found most challenging to
extract."

My guess is that landmarks can’t be extracted from maps because they’re
reliant on the visual field, approaches, other nearby potential landmarks, and
so on. You would need to train an artificial landmark sensor in a machine
hippocampus, perhaps giving it access to Street View and getting feedback data
from humans on the spot asked to point at their nearest landmark.

Computationally producing Lynch maps would also allow for the _reverse_
process, which is to give a robot car directions in the same way you would a
person: down the street, left at the big building, follow it till the end and
we’re the second on the left.
