# A notification center for progress bars that sounds like birdsong

The return of dead time!

One curious experience in [hacking on
Braggoscope](/home/2023/02/07/braggoscope): there’s a lot of _waiting for the
AI._ Asking GPT-3 to extract some data costs 3 cents and takes 5 seconds.
Stick it in a loop and that’s 80 minutes for the 1,000 episodes in the _In Our
Time_ archive.

Now I’ve saved myself a few days writing code by asking the AI to do the heavy
lifting so 80 minutes and pennies per inference is neither here nor there, but
what am I supposed to _do?_

This has come up before:

_Long-running processes_ are kinda the norm, even though we have this
narrative about computers being instant? Whether that’s waiting for a 3D
render, or running the test suite on a codebase and going off to make a cup of
tea while it does its thing.

Or waiting for a restaurant delivery! Or a cab to arrive! Many process are
human-machine hybrids.

tbh I never know what to do with myself.

I can never move on for that 80 minutes. I can never multiplex tasks. Even
though I _know_ it’s only a fraction of the way through, cognitively the
computer’s task is still lodged in my head, and all I can do is doomscroll
Twitter or shuffle my shoes or whatever until it completes. Nothing
productive.

I blame notifications.

Operating systems are really good at dinging when the machine has finished
(and it’s my turn now).

An absolute _ton_ of effort has gone into effective dinging, over the years.
Apps can all ding. I can make my hobby code ding. There’s a top-level OS
feature called the Notification Center which is all about collecting dings, so
that I have a list of all the balls which are now in my court to deal with.

Engagement!

Computers and phones are not so good at, say, _humming_ to say: hey you don’t
need to do anything here. Don’t panic. Go away.

So, _progress bars,_ right?

Progress bars let me see that I’m only 10% of the way through a process, and
the pixels are creeping up oh so slowly, so I can safely get on and THINK
ABOUT SOMETHING ELSE secure in the knowledge that I won’t be interrupted by a
ding.

_Clever_ progress bars even show an estimate time of completion.

_(There’s a command line tool, I forget the name of it right now, where you -
a developer - give it only minimal information, and it deduces the rest,
providing a user interface with percentages and times and everything you’d
need.)_

I know we laugh at progress bars because they were often comically inaccurate
with time estimates – but we could have solved that with better design I’m
sure? Visually provided lower bounds (this process will not complete in less
than X) and confidence levels? Or just made them funny? "Reticulating
splines," that was good.

But we didn’t take on that design challenge…

Instead we got…

Spinners.

Spinners are the dumbest progress bar.

_“I’m busy and I may come back to you in 3 minutes or I may come back to you
in half a second but I’m not going to say which, and anyway the network may
have hung so just wait forever, I’ll just be here looking exactly the same,
spinning.”_

Imagine if all the effort put into managing notifications had gone into
progress bars.

We would have…

Why do I want this?

Well, the motivation as for the Notification Center itself: notifications are
consolidated because it helps manage attention. It’s less stressful to have
_“things I need to look at”_ effectively as a to-do list rather than having to
keep all the dings in my own brain.

Progress Bar Center, same same: it would help me manage my attention. By
listing all the things I DON’T need to look at, and letting me know that I
definitely _don’t need to look at these for the next X minutes_ then it means
I can cognitively stand down: I need no longer inhabit a state of perpetual
readiness.

And so I can finally focus on something else instead.

Imagining, for a second, a Progress Bar Center on my laptop or my phone:

It would be a home for my podcast _Now Playing_ too. And for my current Google
Maps journey. So this is semi-interactive.

Given that interactivity, I can imagine the commercial angle too: the progress
bar for a cloud render or my Amazon order may have a pay-for _Boost_ button to
buy more GPUs or upgrade to next-day delivery or whatever. The process economy
instead of the engagement economy.

And of course my GPT-3 tasks running, and Photoshop filters calculating, and
my movies downloading –

all, collectively, reassuringly telling me: the machine is busy on my behalf.
I can relax, I’m already being productive, put it all out of my mind, there’s
nothing I need to do.

And pulling on that thread of _putting attention aside…_

It’s easier to do that when the locus of attention is physically elsewhere?

Like: when music is coming from the speaker behind me, rather than from the
same location as the code problem I’m trying to crack on-screen, [it seems
less likely to distract me](/home/2021/11/19/airpods).

All these things asking for my attention from the same locus is fatiguing, in
the same way that staring into a point source of bright light is fatiguing,
but a diffuse glow from all around can can be just as bright and not fatiguing
at all – just illuminating.

So the equivalent for attention is (because [I’ve been thinking about room-
scale computing recently](/home/2023/01/20/map_room)) to scatter those
progress bars around the room.

And thinking of the _chugga chugga chugga_ of old hard drives and other
[synaesthetic data senses for machines](/home/2021/08/27/data_sense) – it
maybe would be cool to _sonify_ these progress bars?

The idea of making a soundscape of the workings of the machine has been around
for a while of course but I’ve found it hard to see a plausible route to get
there in this era of notifications. A room of dinging things would be torture.

But based it on this framework for progress bars!

You could do it for cheap with tiny speakers and Bluetooth, sell progress bars
by the handful like AirTags.

I would love it if sitting in my home office had the ambient sound of a
rainforest. Everything, I would think, listening, is working as it should.

The frogs are reaching a crescendo! (I am about to get a notification that a
job has finished, I think to myself.)

Or stepping into an office and hearing all the non-human workers sonified and
layered – the sound of progress as the distant hum of traffic, or the wind.
