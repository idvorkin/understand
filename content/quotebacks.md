# Quotebacks and hypertexts

If you’re reading this on my website, you’ll notice that the next chunk of
text looks a bit different. That’s because it’s a _quoteback._

Quotebacks are like a quote retweet, but for any piece of content on the web.
They work on any webpage, and gracefully fall back to a standard blockquote.

Thus, “Quotebacks” is three things:

1\. A web-native citation standard and quoting UX pattern

2\. A tiny library, `quoteback.js`, that converts HTML `<blockquote>` tags
into elegant interactive webcomponents

3\. A browser extension to create quoteback components and store any quotes
you save to publish later.

Quotebacks is a project? invention? _protocol?_ by Toby Shorin and Tom
Critchlow. [Here’s Tom’s introductory
post:](https://tomcritchlow.com/2020/06/09/quotebacks/) which has some
background. "The ultimate goal is to encourage and activate a deeper cross-
blogger discusson space. To promote diverse voices and encourage networked
writing to flourish."

I’m seeing a bunch of folks [trying](https://www.kickscondor.com/admiring-
quotebacks-strategy) [out](http://peterbihr.com/2020/06/quotebacks-are-great/)
[quotebacks](https://warrenellis.ltd/isles/quotebacks/). If you keep a blog
yourself, I urge you to give it a go. I’ll talk about why later in this post.

I’m not using the Chrome extension to collect quotes myself. I have my own
weird workflow for [hamsterkaufing](https://www.dw.com/en/coronavirus-scare-
when-will-hamsterkauf-become-an-english-word/a-52635400) the web.

But I _do_ want to display quoteback embeds, and you can see one at the top of
this post. _(If you’re reading this in RSS or email, check the website.)_

How? I write quotes in a special format in the Markdown text documents that
lie behind this blog. (I keep everything in various forms of plain text and
have done for a couple decades.)

These text docs are transformed into HTML for the blog using [Python-
Markdown](https://python-markdown.github.io). So I’ve written a Python-
Markdown extension called **quotebacks-mdx** to transform this special format
into the quotebacks embed HTML.

I’d also like feedback on the Markdown format I’m using – if people implement
extensions in other languages, it would be good if something like this became
a de facto standard.

Why did I do it this way?

And, even though I’m not using the Quotebacks browser extension, I’m adopting
the embed format - the protocol - because of what we might one day build on
top.

Back in 1945, Vannevar Bush published his insanely visionary essay **As We May
Think** in _The Atlantic._ Through his imagined machine called the **memex**
he predicted the web and its effect on human knowledge, work, and
conversation:

Consider a future device … in which an individual stores all his books,
records, and communications, and which is mechanized so that it may be
consulted with exceeding speed and flexibility. It is an enlarged intimate
supplement to his memory.

Phones!

[Here’s the original
essay](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-
think/303881/) though the [Wikipedia
summary](https://en.wikipedia.org/wiki/As_We_May_Think) is short and good.

The core feature of the memex is **trails.** It isn’t just a library.

Wholly new forms of encyclopedias will appear, ready made with a mesh of
associative trails running through them, ready to be dropped into the memex
and there amplified. The lawyer has at his touch the associated opinions and
decisions of his whole experience, and of the experience of friends and
authorities. The patent attorney has on call the millions of issued patents,
with familiar trails to every point of his client’s interest. [Etc.]

Wikipedia! Work!

WELL.

And… bloggers:

There is a new profession of trail blazers, those who find delight in the task
of establishing useful trails through the enormous mass of the common record.

Flash forward…

In the early 1960s, Ted Nelson coined the text **hypertext**. The web is a
hypertext, and the [original 1989
proposal](https://www.w3.org/History/1989/proposal.html) cited Nelson’s work.

His project **Xanadu** \- although never completed - was an expansion of what
he meant by this original concept.

Hypertexts are connected texts. But Nelson saw _two_ types of connections:
links (which we have) and something else called _transclusion._

From one paper [about Project
Xanadu](http://xanadu.com.au/ted/XUsurvey/xuDation.html):

This may be simplified to: connections between things which are _different_,
and connections between things which are _the same_. They must be implemented
differently and orthogonally, in order that linked materials may be
transcluded and vice versa. This double structure of abstracted literary
connection – _content links_ and _transclusion_ – constitute xanalogical
structure.

Transclusion:

Transclusion is what quotation, copying and cross-referencing merely attempt:
they are ways that people have had to _imitate_ transclusion, which is the
true abstract relationship that paper cannot show. Transclusions are not
copies and they are not instances, but _the same thing knowably and visibly in
more than once place_. This is a simple point which is remarkably difficult to
get across.

And later in the paper:

Note also that the famous “trails” of Vannevar Bush’s memex system (103) were
to be built from transclusions, not links.

[Here’s Wikipedia on
transclusion.](https://en.wikipedia.org/wiki/Transclusion)

What I love about the web is that it’s a hypertext. (Though in recent years it
has mostly been used as a janky app delivery platform.)

And what I like about Quotebacks is that it already feels like an essential
part of that hypertext toolbox! The Chrome extension meet the needs of Bush’s
trailblazers; the embed format mimics Nelson’s transclusion.

Now the Quotebacks projects doesn’t immediately fulfil on this grand promise.
But the great thing about a protocol is that I can adopt it and support it,
and _you_ can adopt it and support it, and if there’s enough of a consensus,
we can build more on top. So what I’d be interested to see:

_(I’m less bothered about finding out specifically when people use one of my
posts in a quoteback. That would be neat I guess, but tracking mentions is a
first-order problem and besides it’s a spam honeypot.)_

What I’m talking about is the kind of hypertext that I love, one in which my
blog is a place for thinking out loud.

My blog is not my notebook, and it’s not my marketing platform.

My blog is my laboratory workbench where I go through the ideas and paragraphs
I’ve picked up along my way, and I twist them and turn them and I see if they
fit together. I do that by narrating my way between them. And if they do fit,
I try to add another piece, and then another. Writing a post is a process of
experimental construction.

And then I follow the trail, and see where it takes me.
