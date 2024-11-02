# Let’s use spreadsheets to rewire apps and make new ones

How about an app with a spreadsheet under the hood?

Like, the experience would be this: you’re using your photos app or Zoom or
expense filing SaaS tool, then you go to Settings and scroll aaaaall the way
to the bottom, and tap a power user button that says _“Open Spreadsheet.”_

Then, magically, Google Sheets opens with all your data in it, and you can
sort and query it in all the ways you couldn’t before, and change the titles
of your expense claims with spreadsheet functions and that all gets reflected
back into the app, or build a callout to an AI to describe all your photos and
add natural language tags, do it yourself or ask a friend who knows Excel
functions, or whatever really. Anything the app developers didn’t add because
they’re building for the 80% use case, and you’re building just for you.

So that’s the idea.

_Example #1. Where the spreadsheet is an alt UI for the app._

This is the pattern described by Geoffrey Litt and Daniel Jackson in their
2020 prototype, _Wildcard._

In this paper, we present _spreadsheet-driven customization,_ a technique that
enables end users to customize software without doing any traditional
programming. _The idea is to augment an application’s UI with a spreadsheet
that is synchronized with the application’s data._ When the user manipulates
the spreadsheet, the underlying data is modified and the changes are
propagated to the UI, and vice versa.

You can see some videos at that link: _Wildcard_ is a prototype browser
extension and, visiting Airbnb, you can pop open a spreadsheet view and sort
search results in ways not supported by the official site, run calculations
etc.

(Litt wrote a long Twitter thread listing [lesser known projects that also use
spreadsheets](https://twitter.com/geoffreylitt/status/1589656517157920769).)

_Example #2. Where the spreadsheet is a canvas to weave together new apps._

Fabian Stelzer recently made a Google Sheets template called HOLOSHEET that
includes functions to call out to GPT-3 (text generation) and Stable Diffusion
(image synthesis) to draft and visualise movies…

HOLOSHEET, story edition!

built a google sheet powered by GPT-3 and #stablediffusion that outputs full
stories, with images!

you input a prompt & the AIs generate story, visuals and a title

in any style you want..

here’s “The wizard approached the abyss”

a few seconds later:

_(There’s a series of screenshots at that link.)_

So you might say "The wizard approached the abyss" and specify a fantasy style
from the dropdown, then an embedded, parameterised GPT-3 prompt outlines the
story in four scenes, with each scene then being sent to another AI for the
illustration.

Side note: Stelzer isn’t a coder. To make the `=GPT3()` Google Sheets
function, [he asked GPT-3 itself to write the
Javascript](https://twitter.com/fabianstelzer/status/1572571003804614657).

So both of these are examples of that [old design movement Adaptive
Design](/home/2020/08/26/adaptive_design) _(2020)_ – end-user adaptation of
products that metaphorically have the wires hanging out the back.

Like, sometimes: when you own a house, and not only does it allow for changing
around the rooms and so on, but it has been architected so that there’s a
blank wall and space on the plot for you to build an extension.

As with architecture, so software.

Adaptive Design in software allows for

(The second point came up in conversation recently. Yes sure it’s important to
go and talk to users and co-create solutions. But why not give people the
tools and knowledge to adapt the technology _themselves_ and then pay
attention to the power users?)

What’s neat about spreadsheets, and particularly neat about Google Sheets, is
that:

They’re an interesting vernacular, spreadsheets.

_What should startups do?_

In the early 2000s, user interfaces were being torn up and re-invented as work
went online. The response was a fluid world of web APIs, remix culture, and -
to frame that with theory - Adaptive Design.

_(Anyone remember[Yahoo! Pipes](https://en.wikipedia.org/wiki/Yahoo!_Pipes)
(RIP)? A universal canvas for remixing the web with native handling of APIs
and RSS… a bigger loss than Google Reader, that one.)_

I feel like we’re seeing this deconstruction/reconstruction again? With
generative AIs, and new multiplayer ways of working and new tools for thought,
there’s a growing participation in finding out what our new tools should be
and how they should behave.

Maybe this time round, instead of APIs we could have Excel formulas? APIs
never had that work surface to knit them together; formulas have that built-
in.

I wonder what an app team could do to be really spreadsheet friendly? I wonder
what the Google Sheets team could do?

And: back in the day there were API lifecycle/management startups _(that then
all got acquired)._ Will there be equivalent startups to
publish/consume/manage the spreadsheet surface?

Yeah so we should do that.
