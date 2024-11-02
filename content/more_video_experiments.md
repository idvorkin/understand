# More experiments with video calls, and what slides are for

After my (slightly ludicrous) [experiments with projectors and video
calls](/home/2020/06/04/projectors) I became pretty into the idea of having my
face **and** my slides in the frame of a video call.

So!

[Here are some MORE pictures of what I’ve made.](/more/2020/07/virtual-
webcam/) Check out that write-up page, the rest of this post will make way
more sense if you do.

Both of these experiments are made using a _virtual webcam_ setup - basically
I’m using some software mainly used by video game streamers to intercept my
webcam feed, and add extra elements to that video. The result is output as a
virtual webcam that can be chosen as the camera in Zoom, Google Meet, or
whatever you use.

As soon as I make something, I think of the 100 things I want to have next.
That’s why prototyping is good. You don’t need to have much imagination, you
just listen to what the prototype tells you.

For my first experiment, I made it so that when I sketch on my iPad, the
sketch is overlaid on my webcam.

The particular interaction I tried is included as a video on that write-up
page: I hold up one finger and draw a figure one; I hold up two fingers and
draw a figure two; etc.

It feels like this would be a neat way to provide narrative “anchors” when
giving a talk. Minimum viable chapter headings. Or maybe draw a quick diagram
in the air when only a diagram will do, [Pulp Fiction
style](https://www.youtube.com/watch?v=mi6tQthPDWc).

This one is pretty simply but feels like it’s got some legs: I gave my regular
slides a green background, which I then chromakey-removed and replaced with my
face on the webcam.

Like, I’m tracking [what Mmhmm is
doing](https://www.theverge.com/2020/7/7/21314035/mmhmm-personal-video-
presence-beta-phil-libin-sequoia-app) because I like the idea of including my
slides in my video feed like I’m a talkshow host. It’s still in beta and I’m
fascinated to see where they take the service.

BUT: fully blending webcam + slides, and designing for thumbnail view… that’s
what I want. FOR EXAMPLE, what I found is:

It is neat to have MASSIVE TEXT over your face because it means that everyone
in the audience can watch in gallery view - every face a thumbnail - yet your
slides are still visible.

_(There are pics of all of these on that write-up page linked at the top of
this post.)_

This is like speaking to an audience but keeping the house lights up, and
being on the flat instead of a stage. It’s a more egalitarian feel.

You can have lists that appear over your shoulder that provide structure
during long sections; you can takeover the whole image with a quote to draw
focus.

And then there are some games to play: you can peep around the side of images
that float in space. You can make faces at, say, a statement that undermines
your point that you’ve deliberately included – [as previously
discussed](/home/2020/05/15/video_talks) it can be narratively useful to put
yourself in the shoes of the audience by turning round and looking at a slide
with them, reacting to it. And this is a way to do the same on a video call.

The system I made is pretty janky, but I’ve used it enough that I know there’s
some creative potential I want to explore. Not just novelty but better
storytelling.

_(And although this system used**pre-prepared slides** I also tried **live
slides** \- typing words directly into a slide and having it appear over my
face, which I was on a call. That’s intriguing, though harder to manage.)_

I gave a talk on [Tom Critchlow’s
Discord](https://tomcritchlow.com/2020/07/08/discord/) to maybe 30 people, and
it ended up being audio-only due to technical hiccups. It’s been a while since
I spoke for 30 minutes straight, just my voice, no video. In that talk, I
found myself wanting to be able to live scribe numbers in the air, to indicate
where I was in a series of points. I wanted to play with my slides/webcam
combo, and use the size of the type to communicate emphasis -= body language
doesn’t work nearly as well over video as real life.

So I asked myself: when I’m doing a talk, what job am I really asking slides
to do?

I think I use slides as…

Sure there are graphs and diagrams and images and long quotes, and all the
other things that presentation slides have in them. Content.

But a talk needs to _engage_ or the content won’t come across anyway. Talking
for a long period of time, without a conversational back and forth, is pretty
unnatural, and you have to do a bunch of work to stop people tuning out.
That’s what I think slides are for – at least in part, and at least for me.

What I’ve found, with this composite webcam feed, is that the slides can do a
similar job for me as they do in real life - _anchoring, rhythm, and play_ \-
while keeping my face full frame, not taking over the full screen, and not
making it look like a pre-recorded TV show (which is distancing in its own
way).

I mean, I admit this is slightly, _“ooh hark at me, I’ve re-invented the
freaking WEBINAR,”_ but I enjoy public speaking, and it seems like there’s a
route to a satisfying version of the same kind of thing only from my sofa –
which is how I live now, a centaur: my top half on zoom calls and my bottom
half, soft furnishings.

So I’m going to keep digging in this direction.

Or rather… I’m going to try to fix my janky hacks so it functions for more
than 15 minutes without accumulating up a very distracting and weird-looking 5
seconds of video lag..

**The technical bit:**

I’m using [OBS Studio](https://obsproject.com) to capture the webcam and mix
it with other video sources. The [obs-virtual-webcam
plugin](https://github.com/johnboiles/obs-mac-virtualcam) (for macOS) outputs
the stream as a camera source that can be used in most video software.

For slides I use [Deckset](https://www.deckset.com) as it has a built-in
feature that expands type to fill entire slides, and also because I can simply
type into a text document to quickly make new slides while I’m on the call.

To capture the iPad screen I’ve been using
[AirServer](https://www.airserver.com) to run an AirPlay server on my Mac, and
that can direct video into OBS (add a Syphon source in OBS and choose your
iPad once you’ve started screen sharing).

It’s all pretty slow – I have to close applications, quit my network monitor,
etc, and the lag still builds up. I’d like to hear about ways of shortening
the video path if anyone has any ideas. I want to continue having this appear
as a virtual webcam so it works in all kinds of video call software.
