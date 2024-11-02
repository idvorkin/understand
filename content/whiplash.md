# I don’t believe in Zoom fatigue. HOWEVER…

I’m sceptical about “Zoom fatigue,” which gets talked about a bunch, this idea
that you get fatigued from spending a ton of time over the day on video calls.

OR RATHER what I mean is, yes, I do indeed get fatigued from a day of video
calls (evidence: how I right now), but no, I don’t think it’s down to number
of hours on calls specially.

My guess is that it’s about repeated and rapid changing social context.

You’re in a high bandwidth interaction (full video, full audio, conversational
turn-taking, eye contact), then the call ends and you’re on your own in your
room. Then high bandwidth interaction, then on your own, then high bandwidth
interaction, then etc.

It’s not Zoom fatigue, it’s Zoom whiplash.

It’s a hunch. I can’t prove this.

The trick to get around this is to move smoothly up and down the gradient of
social interaction intensity, never dropping below a basic floor of
_presence:_ the sense that there are other people in the same place as you.

Instead of having two modes, “in a call” and “on my own,” we need to think
about multiple ways of being together which, minimally, could be:

And the job of the designer is to ensure that their software ensures the
existence of these different contexts, instead of having the binary on-a-
call/not-on-a-call, and to design the transitions between them.

(I posted in January about [lessons from architecture for the
metaverse](/home/2022/01/21/social_gradient), drawing from _A Pattern
Language_ by Christopher Alexander, and that was specially about how to design
this kind of smooth social gradient.)

Presence? The solution to social context whiplash.

As a baseline, ensure that the user always has a sense that other people are
around. That’s all presence is.

If you have presence as a “default” then you can move up and down the social
gradient quite happily.

It’s pretty easy to create a sense of presence in software:

It has to be live.

HOWEVER, in solving the whiplash problem by insisting on a baseline of
presence, we’ve introduced a whole new problem: being around other people is
exhausting.

Being on display is exhausting! What’s at the root of that? Another hunch…

When you have “presence” as a software feature, there’s a vague sense of being
monitored. You can never escape the idea that other people can tell whether
you are active at your computer or not. Some people care about this more,
others are able to care about it less, but it’s there none-the-less.

What happens is that the part of our simian brains that looks after
“presentation of self” (per Goffman) kicks in. _That’s_ work. The self-
governing of how one is perceived by others.

Not quite panoptic but _sousveilled_ – the act of watching one-another rather
than surveillance from above.

So you end up being ever so slightly aware that other people can tell whether
you’re active on your computer or not. Whereas, in the office, people can tell
that you’re working by the view of you concentrating - whether hunched over a
sketchbook or staring preoccupied at the ceiling - when you’re remote, it’s
totally equivalent whether you are not moving your cursor because you’re
thinking harder than you ever have… or if you’ve snuck off down the shops.
Which means you have to care about it. This creates a unnamed paranoia and
incentivises the performance of work rather than work itself.

I.E. IN A NUTSHELL: presence can be exhausting.

Introduced in 2011, the US military has a drone surveillance technology for
monitoring motion over an entire city. The project is named [Gorgon
Stare](https://en.wikipedia.org/wiki/Gorgon_Stare) _(Wikipedia)._

And it’s an _incredible_ name, right? Because the effect of the panoptic gaze
on the city is to freeze it - if you don’t want to be seen then don’t move -
what the drone’s eye, like the eye of Medusa (a Gorgon), is to turn people to
stone.

So there a just a touch of telepresence that I feel like that, like 0.1% as
much but still.

Like: I’m unable to type in a Google Doc if other people are there. Do you get
that? I end up writing in another doc and copy-and-pasting in the new
iteration. It’s a fear! Literally petrifaction/petrifying. The Gorgon Stare of
_Anonymous Goose_ lurking up there in the top right of the browser viewport.

PREVIOUSLY: Freud’s whole thing about Medusa was that individual wasn’t being
_turned to stone_ by Medusa, but instead making a _decision to become stone_
in a personal response, escaping their own terror of castration. To do with
Medusa’s head snakes resembling – look, [as previously
discussed](/home/2021/01/27/medusa), go read. I would _love_ to know what
Freud would have made of Google Docs.

I love this cascade of design problems/solutions/problems.

Zoom fatigue is really Zoom whiplash so introduce presence.

Presence is itself exhausting. And so…?

What’s the best way to _personally_ feel present, online, but without the
knock-on micro effects of panoptic sousveillance to everyone else on your
presence list? One to figure out.

I suspect this problem can be solved by having lots of different places that
you can be present in.

Instead of Slack showing _everyone_ who is online (present) right now, it
should show who is online just in the channel I happen to have open. That way
I get the benefit of feeling like there are people around me, but without the
concern that other people might think I’m lazy if I take 30 minutes away from
my computer to do some hard thinking. I have plausible deniability. As far as
anyone else is concerned, I may just be in another room.

And that’s why social software should always have multiple rooms that you move
between.

The opposite of fatigue is immersion.

When Ze Frank invented the genre of personal web videos - video blogging -
back in 2006 ([which I wrote about here](/home/2020/06/22/anti_attention)) he
was absolutely insistent that the presenter had to stare directly into the
camera. He went as far as _editing out his blinks._

he advises would-be vloggers not to blink because when you blink, “that’s one
less connection made” with viewers.

I have a similar feeling towards social software.

When you have a video call, you feel immersed in the social context.

When you drop back to a space without any kind of social context, not even
presence, your desktop, it breaks immersion. _Blink._

But when your software makes a promise to never drop the social context below
the presence baseline, you never stutter immersion, and it just builds and
builds and builds as you move around.

That’s what I’m finding in the day job anyhow. (We’re building a platform for
being social online, with an architectural approach and multiple “spaces” that
you move between. There’s nothing special going on with the tech, it’s just
multiplayer webpages, no rocket science, but gosh it works – a kind of [lo-fi
metaverse](/home/2021/12/02/metaverse).)

TANGENTIALLY:

Why did the US military develop _Gorgon Stare?_ Because of Will Smith.

In _Enemy of the State_ there’s an imagined technology, a satellite that can
watch people on the ground across vast areas. This was of course pure fantasy
at the time. An engineer who works for the government saw the film in a
theater and thought it would be quite incredible if the government could
actually do that. That seed of inspiration precipitated a whole series of
events and development projects that culminated with Gorgon Stare about ten
years later. It took a while, but during that period the rate at which camera
technology got more powerful outpaced Moore’s law, which predicts the rate at
which computer chips become more powerful. It was this phenomenal jump in
capability in a very short period of time, all driven from an initial seed of
inspiration, a 1998 Will Smith blockbuster.

My friend Mark H tells me that _Enemy of the State_ is an unofficial sequel to
Francis Ford Coppola’s _The Conversation_ (1974), Gene Hackman’s character
being the same but with a different name because they couldn’t sort out the
rights. _The Conversation_ being notable for its remarkable sound and
additionally distinctive camera-work from above to visually depict the
narratively essential long-range sound monitoring equipment, a visual trope
that was naturally extrapolated in _Enemy of the State_ to its unreal-but-
then-becoming-real satellite viewpoint. An extraordinary conceptual ancestry.
