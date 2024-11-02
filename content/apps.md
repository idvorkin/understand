# The apps I use to read and write for this blog

Because I’ve been asked a couple times recently:

I keep up with 345 websites and newsletters using an app called
[NetNewsWire](https://netnewswire.com). It’s free and I have it on my Mac,
iPhone, and iPad. It’s a type of app called a newsreader.

When I find a blog or website I want to follow, I look for an RSS feed
(sometimes just called a “feed”) and subscribe. This is also free. NetNewsWire
grabs the feeds periodically, and presents the articles so that I can read
them without ads or design.

(There are many newsreader apps out there. NetNewsWire is my favourite because
it’s clean, easy, and fast.)

(Learn the basics about using RSS at [AboutFeeds.com](https://aboutfeeds.com).
The feed for this blog is [here](/home/feed).)

How does NetNewsWire keep my subscriptions in sync between my various devices?
When you run the app for the first time, it asks you to set up an account with
one of various providers. It’s a bit like the way your email app will ask you
who hosts your email. One free option for syncing is iCloud. I didn’t do that.
Instead I first created an account with [Feedbin](https://feedbin.com) for
which I pay $5/month. NetNewsWire uses Feedbin to sync my devices.

I pay for Feedbin for one big reason: it gives me a secret email address that
I can forward anything into. Here’s how I use it:

I read a lot of email newsletters, and email newsletters don’t have RSS. But
my email client is a terrible place to read long articles. My inbox is full of
distractions and I often miss things. So when I subscribe to a newsletter, I
also set up an auto-forward rule from Gmail to my secret Feedbin email (and
auto-archive the original email). Now newsletters appear in Feedbin, and
therefore I get to read them in NetNewsWire.

[Here’s my subscription list](https://interconnected.org/home/blogroll)
(you’ll find a bunch of blogs there you can also subscribe to).

How I use NetNewsWire:

I don’t read everything.

NetNewsWire has a “smart feed” called _Today_ which only shows articles that
have been published today. I look at that multiple times daily, then
occasionally at particular favourite blogs to see if I’ve missed anything. I
have about 6,000 unread articles. That’s fine.

I do almost all my writing in an app called [Ulysses](https://ulysses.app).
It’s on my Mac, iPhone, and iPad and keeps in sync with iCloud.

It keeps short text notes in an overall library, organised by folder. I’ve
used it for years. It’s well-designed, simple but not over-simple, and
reliable.

I have top-level folders for

(I don’t keep track of to-dos much, but when I need to I use an app called
[Things](https://culturedcode.com/things/) which I have on all my devices.
It’s also well-designed, structured without enforcing too much structure, and
simple without being too simple. I organise tasks by project, and tag them by
person and by whether I’m expecting to hear from them or they’re expecting to
hear from me. This keeps general to-dos out of my notes.)

Inside the top-level folder for this blog the main two folders are:

My writing process is as follows.

Whenever I see an interesting link, on the web or reading subscriptions, I use
the share icon and save it to my Links folder in Ulysses. I copy and paste a
little context, or add a few words to make sure I can find it later. I don’t
sweat it with tags or detail. I save maybe a dozen links a week.

(My long history of keeping these links is also how I put together talks, or
do invention work when I’m in client work mode. I don’t have to be smart about
a topic, I just have to have been keeping notes for longer than most people
would think reasonable.)

Whenever I have an idea for a blog post, I make a quick note in Drafts. This
might be a single line or it might be a paragraph. Drafts tend to start with
an observation, a question, me trying to explain something to myself, or a
connection between two ideas. Ideas for post appear suddenly and disappear
just as fast – so I’m diligent about writing them down immediately even if I’m
half awake or walking down the street. I write down maybe 3 or 4 ideas a week.

When I’m in the mood to write, I browse through my collected links and my
drafts and wait for something to catch my eye. This is rarely at the same
point as capturing an idea.

Often what happens is that two drafts rhyme with one another, so I bring the
two together.

Another frequent occurrence is that I can’t think of anything to write, so I
start by trying to explain in plain language why I find something interesting.
I might get a few paragraphs along before I feel like the post isn’t going
anywhere, so then I stop but I leave the expanded text in the draft.

I do this probably daily, 20 or 30 minutes expanding notes, trying bits of
narrative, connecting ideas, and generally reminding myself of what’s in my
notes.

Two or three times a week a post gets all the way to the end. Sketching and
thinking my way through an idea is a different process to actually writing. I
often surprise myself in this process – I usually don’t write with an endpoint
in mind. It’s more like improv, and my opinion sometimes turns 180 through the
process. I barely copy edit when done. Once over quickly, that’s it.

Then I title it and it’s done.

My blog is a homegrown setup and it doesn’t include an editor, web-based or
otherwise. Posts are in Markdown (for the last decade; the first decade they
were in XML). It’s all templated and I wrote my own server-side app for
rendering.

When I write a post I save the text file in a directory with today’s date and
add it to the code repository using git. On my Mac that means using Terminal.
On my phone and iPad I use an excellent app called [Working
Copy](https://workingcopy.app) which is a git client. The code gets pushed to
Github. Then I connect to my server over SSH and run a script which deploys
the latest code, including the new post.

This is a pretty baroque process. I wouldn’t recommend it to anyone. But I
like controlling my own code and having the ability to tweak the way my blog
works, so it’s good for me.

I’m very often not happy with what I write. Sometimes I’m super excited.
However I also know (from experience) that my feelings about a particular post
do not correlate well with how it will be received. So out into the world it
goes, either way.
