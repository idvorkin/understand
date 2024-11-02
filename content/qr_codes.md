# Using printed QR codes for links in books

I’m currently reading Alexandra Deschamps-Sonsino’s excellent [Creating a
Culture of Innovation](https://www.amazon.co.uk/Creating-Culture-Innovation-
Optimal-Environment/dp/1484262905), which is simultaneously a survey, history,
and playbook for how to invent the future from inside corporations.

_(Cleverly, Alex is serialising the book as a series of free Friday lectures,
starting later this month.[Register for tickets
here.](https://www.eventbrite.co.uk/e/creating-a-culture-of-innovation-
tickets-136196382045))_

There are many links in the footnotes, which is great. But I like reading on
paper (it helps me focus) and it is _tedious_ typing URLs into my phone
browser letter by letter.

We had a similar problem with _Mind Hacks,_ and our workaround then was to put
all the links [on a single web page](https://mindhacks.com/book/links/).
Functional but not great.

So I was very taken with **Tom Critchlow’s recent experiments with printed QR
codes** (for his [upcoming book on indie
consultancy](https://tomcritchlow.com/strategy/)):

Is there an “in-line” QR code format? The print book <–> HTML connection is
awful. Best standard seems to be footnote the link and then print the URL…

He shows a couple of elegant examples of what he’s looking for, such as

QR codes are a neat solution because smartphone cameras natively resolve them
to hyperlinks, without even taking a photo.

BUT

As [this deep dive into printed QR codes](https://lethain.com/qr-codes-in-
books/) shows, there are design challenges:

So, taking this route, you end up with large QR codes on the page. Not ideal.
At worst, ugly.

Of course there are workarounds: one big QR code per chapter, perhaps,
providing a menu of all the links in all the footnotes.

I’d love to see a solution like Critchlow’s original mockups. Inline, robot-
readable links have an elegance that reminds me of Tufte’s
[sparklines](https://en.wikipedia.org/wiki/Sparkline). Though perhaps this
route has reached a dead end.

What’s the limit on how small a QR code can be printed - and scanned reliably

- and what’s the character limit for that? Could it contain a URL?

Is there an alternative QR code standard which is simultaneously much more
compact, and also already supported by smartphone cameras?

If we need a whole new standard, we could think about sorting out the
opaqueness problem of existing QR codes. What about a robot-readable glyph
that was interpreted by the smartphone camera to simply mean: _use OCR on the
following string of characters and treat it as a web address_ (or a bank
account number, or a Twitter username, or whatever). Basically a robot-
readable protocol prefix, like “http:”. That would have the benefit of being
robot-readable and human-readable simultaneously.

But new standards would take years. I’d prefer tiny QR codes in books that
work today.
