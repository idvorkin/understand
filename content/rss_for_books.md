# Re: Tom Critchlow’s proposal for a decentralised Goodreads-like system, how about using RSS?

Tom Critchlow is having smart ideas about [websites that share lists of
books](https://tomcritchlow.com/2020/04/15/library-json/), and an open,
decentralised way to do it. So this blog post is a response to his ideas and
gets a bit technical.

Whenever I’m thinking about new systems, I like to keep in mind what I’d like
to enable. So here are some lists of books:

I would _love_ to be able to subscribe to these, and also have a custom
aggregator so that I could read a review about one book, and find out who else
has been talking about it.

Like Tom, I am no stranger to projects about books, having [built a book
vending machine that sent tweets](http://www.mwie.com/special-
projects/machine-supply) and [run a newsletter to share book
recommendations](https://tinyletter.com/machinesupply/archive) because, like I
said back in 2015, [knowing what books someone loves is to know their
perspective and their
journey.](http://interconnected.org/home/2015/07/22/machine_supply)

It would be neat if I could subscribe to people’s lists and recommendations,
like subscribing to blogs or following someone on Twitter, then tap through
and browse their bookshelves.

And I agree with Tom when he says that this doesn’t need to be (yet another)
competitor to [Goodreads](https://www.goodreads.com). As he says:

Thinking through building some kind of “web of books” I realized that we could
use something similar to RSS to build a kind of decentralized GoodReads
powered by indie sites and an underlying easy to parse format.

Although where I differ is that Tom says "something similar to RSS" and my
response is: well why not just _use_ RSS? Well, kinda…

Tom’s suggestion is **library.json** which is a machine-readable data format
that includes lists of books. Each book object has a title, author, link, date
finished, and links.

What I suggest instead is that this is split into two formats:

Taking the book list format first: rather than inventing a new format, my
suggestion is that this is RSS plus an extension to deal with books.

This is analogous to how the [podcast feeds are
specified](https://developers.google.com/search/reference/podcast/rss-feed):
they are RSS plus custom tags (this is the [recommended approach in the RSS2
spec](https://validator.w3.org/feed/docs/rss2.html#extendingRss)).

Why use RSS instead of a new JSON format? Because…

Playing near existing ecosystems is great. It’s easier to hack together
implementations and get going, and it’s more likely that people will get
involved.

In terms of the actual tags for the book object, I would suggest:

Then the question is how to handle **library.json** …

Well there’s already a way to group RSS feeds, and that’s OPML. Yes it’s
slightly weird for this purpose, but it’s [well-established for sharing
subscription lists](http://dev.opml.org/spec2.html#subscriptionLists) and with
some strong and documented conventions, it could work well. For example there
should probably be:

Why use OPML? Because RSS readers already support importing feed from OPML,
and it’s easier to build an ecosystem from an existing one.

I’m very taken by the use case in Tom’s post where it says “Ribbonfarm has
just added a new list…”. This would be implemented by the aggregator
monitoring for updates in the OPML file.

I like that

I would definitely like an aggregator that showed me book reviews from
everyone I follow explicitly, and also everyone _they_ follow – but no-one
else. That would deal with the potential spam problem.

If this was also going to be public, how about a file called **following**
which is exactly like the library but, instead of pointing at my own RSS lists
of books, pointing at other people’s library OPML files? It’s what OPML is
made for…

I know that using RSS instead of JSON objects looks more complicated on the
face of it… but RSS is already battle-tested and there’s no point reinventing
the wheel. And in terms of building an ecosystem, it’s faster to start with
RSS rather than doing something bespoke. It worked for podcasting!

The next step would be to bash out a draft spec and put it on a web page so
people can point to it. Given something that a few of us agree amongst
ourselves, along the lines of the above, I would definitely be up for getting
a book feed coming out of my blog in that format, plus a library file, and
keeping it all live with a few reviews.

And that, if a few of us did it, we could quickly see what it all feels like
by using off-the-shelf RSS readers (I use
[NetNewsWire](https://ranchero.com/netnewswire/) on iOS and Mac), and then
start playing around with aggregators too. Maybe find someone who is into
WordPress to hack on a plugin too.

Anyway, Tom, [back to you!](https://tomcritchlow.com/2020/04/15/library-json/)
