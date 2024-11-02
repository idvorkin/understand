# Colophon

I’ve been asked a couple times recently about the technology I use to publish
this blog. I should have a colophon to link from the footer, right? So here it
is as of October 2024.

I roll my own blogging system.

Each post is a text file in a directory named for the date. Today the files
use Markdown with some metadata at the top. For example, [here’s the Markdown
version of this post](/home/2024/10/28/colophon.md).

This format pre-dates “Markdown front matter” popularised by Jekyll which is
why it doesn’t look the same. I’ve been writing here since 2000. Pre 2012 the
files are still in XML, originally output by blogger.com.

A build step creates an sqlite database as an index used by archive pages,
tags and backlinks. (Historic posts are automatically given links to follow-up
posts.)

Pages are vanilla HTML and assembled by a lightweight app. The app is coded in
Python using Flask and Jinja templates. So the HTML isn’t pre-built (templates
are rendered on every request) but the database is “internal” and read-only,
i.e. quick. Simon Willison calls this pattern [Baked
Data](https://simonwillison.net/2021/Jul/28/baked-data/) and I find it perfect
for this kind of site.

The site is served by Apache2 with mod_wsgi from a lowish-end Ubuntu instance
hosted at Digital Ocean. I don’t use an dedicated app server, or a CDN or
cache. Posts have hit the top of Hacker News a handful of times without load
struggle; this approach seems fine.

My blogging system doesn’t have an authoring UI. I write in a writing app.

I find there are three stages in writing a post and they happen at different
times, when I’m in the mood:

I use [Ulysses](https://ulysses.app) for all of this. I often drop into
[BBEdit](https://www.barebones.com/products/bbedit/) to finish things off.

I still distrust non-ASCII characters so I run a command to strip those (using
iconv, if you’re interested). But I make an exception for accented letters in
Proper Nouns.

After a new post is saved as a file, I push it to GitHub (the whole thing is
in source control) then run a deploy command which updates the files on the
server, causes it to build the database, etc.

If I need to edit from my phone or (rarely) if I want to post from my phone, I
use the app [Working Copy](https://workingcopy.app) to add the file to source
control, then run the update script on the server.

I try to be mindful of the mental blocks I place in the way of writing. [My 15
personal rules for blogging](/home/2020/09/10/streak) _(2020)_ help me to
avoid them. I’m not writing as frequently as I was when I wrote that, but even
so I’ve currently been publishing new posts for **240** consecutive weeks (my
streak is in the site footer).

Related: [More about how I use Ulysses](/home/2022/05/27/apps) and also RSS
_(2022)._

The blogging engine has changed several times over the past 24 years.

24 years is longer than many programming languages are popular and definitely
most frameworks. In that time I’ve cycled through being good and rubbish at
software development at least twice.

So following the principles of web longevity, what matters is the data, i.e.
the posts, and simplicity. I want to minimise maintenance, not panic if a post
gets popular, and be able to add new features without thinking too hard. If
push comes to shove, I need my site to be simple enough such that I could re-
write the blogging engine in half a day or so (which has happened).

I don’t deliberately [choose boring technology](https://boringtechnology.club)
but I think a lot about [longevity on the web](/home/2017/08/17/upsideclown)
_(that’s me writing about it in 2017)_ and boring technology is a consequence.

It does add a certain kind of complexity to handle my own hosting. It’s not
like I _enjoy_ writing Apache conf files. Like, why not build the site using
Jekyll and host it all for free on GitHub Pages?

But what I lose in simplicity I gain in control.

For example, it’s important to me that I have a friendly RSS feed (see
_Extras,_ below). But GitHub Pages doesn’t let you change the HTTP headers
which is a requirement to do that. So I don’t want to use any blogging system
that constrains the features I might want to add, or encourages me to make use
of its own special features that I can’t rebuild myself next decade or the one
after.

And adding a new feature (like the streak counter) doesn’t require reading any
framework docs because it’s just Python.

(My conservatism isn’t limited to unicode. I added support for images only
earlier this year, and don’t plan on using them except for special occasions.)

p.s. this isn’t an attitude I bring to all software I build. It’s particular
to my blog.

A couple of other features:

I no longer automatically crosspost to any social networks.

I’ve had this setup since April 2020. I don’t 100% remember why I rewrote it
then. I think I wanted to tweak the old design and couldn’t straightforwardly
compile the templates after a security update.

That previous blogging engine appears to date back to 2008. It originates from
before GitHub so it’s not entirely clear. It had at least 3 designs and used
Python and CGI.

2000–2008 is a mystery.

I am aware that my setup appears baroque with many fiddly manual steps
documented only in my shell history. Honestly I regard myself as a kinda not
very technical person with a simple setup and (a) reading the above back to
myself, it’s a surprise even to myself, a travesty, a fiasco, and yet (b) I
feel like it accords with a principle of simplicity on a certain otherwise
unnameable axis.

However it is decently grooved with how I write and how I want people to read,
and the cadence I have for maintenance and adding new things. A good trade.

I think that’s it?
