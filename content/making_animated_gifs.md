# How my Twitter bot makes personalised animated GIFs

Ben Brown noticed that my bot @5point9billion made him a personalised animated
GIF [when it tweeted him
yesterday](https://twitter.com/5point9billion/status/725012835558916097) (on
the occasion of light that left Earth as he was born, right at that moment
passing the star Iota Pegasi, a little over 38 light years away). And he was
curious about how it did that. So:

[There’s a previous write-up about @5point9billion
here.](http://interconnected.org/home/2015/12/14/5point9billion) From that
post:

My new bot is called @5point9billion which is the number of miles that light
travels in a year. The idea is that you follow it, tweet it the date of your
birth (e.g. [here’s my starter
tweet](https://twitter.com/genmon/status/674333947405447168)), and then it
lets you know whenever you reach Aldebaran or wherever.

You get tweets monthly, and then weekly, and for the last couple of days… and
then you pass the star. It feels neat, don’t ask me why.

Since that write-up, I’ve also added a website to the bot. In addition to
getting the realtime notifications on Twitter, [you can sign in on the
site](http://electron.farm/5point9billion/) and see what stars you’ve already
reached.

Check this out: [There’s also a public
view,](http://electron.farm/5point9billion/public-map) with an animation. This
is a 3D animated map of all the star systems we can see from Earth, within 100
light years. It sits there and rotated. You can type in your date of birth,
and it’ll show you what stars you’ve already reached.

I made this public view as a “kiosk” mode when @5point9billion was [exhibiting
at the Art of Bots show](http://www.andfestival.org.uk/events/matt-
webb-5point9billion/) earlier this month. The stars were laid out on the
floor, fanning out from the Sun which was right by the kiosk. [Here’s a
photo.](https://www.instagram.com/p/BEPOAEZqpcI/) It was good fun to walk out
from the Sun till you find the star you’ve just passed. And then to walk out
to about 80 light years and think, hey, most people die around this point, and
look at the stars falling just further from you and think, hey, I probably
won’t reach those. Huh.

The star map is drawn and animated in Javascript and WebGL using
[three.js](http://threejs.org) which I really like.

And doesn’t it look kinda the same as the personalised star map that the bot
made for Ben? Yup.

I knew I wanted to tweet out personalised, animated star maps, whenever a bot
follower passed a star (there are over 500 followers, and between 2 and 5 of
them pass a star each day).

Routes I considered but discarded pretty fast:

This is the rendering pipeline I settled on:

If you’re curious, [here’s the source animation on the
website](http://electron.farm/5point9billion/mapgif?user=genmon&draw=1). And
[here’s how it looks in a
tweet.](https://twitter.com/5point9billion/status/725012835558916097)

If you want, knock the “draw=1” off the URL – you’ll get a blank page. Then
call step() in your browser’s Javascript console and see each frame being
generated.

There’s a wrinkle: Phantom doesn’t support WebGL, so the star map animation in
three.js had to be re-written to draw directly to canvas… which three.js
supports but you have to add custom sprites and a few other things. It gets
hairy, and I’m super happy to have worked with [@phl](https://twitter.com/phl)
on that side of things – he looked after the Javascript drawing with his
amazing code chops.

Another wrinkle: PhantomJS 2 (which this requires) installs on the Mac using
[Homebrew](http://brew.sh) just fine, but is a pain to build on Ubuntu which
is what my server runs. [There’s a pre-built binary
here.](https://github.com/Pyppe/phantomjs2.0-ubuntu14.04x64)

In summary, this is a rendering pipeline which:

I prototyped this rendering pipeline with another Twitter bot,
[@tiny_gravity](https://twitter.com/tiny_gravity) which just does a tiny
particle simulation once every 4 hours. Sometimes it’s pretty.

This animation doesn’t use three.js for drawing, it uses
[processing.js](http://processingjs.org), but the principle is the same.
Again, [the animation is just a
webpage](http://electron.farm/admin/gravity/animation?draw=1), so I can tweak
the animated GIFs in the same way I tweak the rest of my website and bot
behaviour. [Here’s that animation as a
tweet.](https://twitter.com/tiny_gravity/status/724949919811952641)

One of the things I’m most enjoying about having multiple projects is how they
cross-pollinate.

My main side project right now is my bookshop-in-a-vending-machine called
_Machine Supply._ [Here it is at
Campus](http://machine.supply/machines/campus), Google’s space for
entrepreneurs in Shoreditch, London.

[It tweets when it sells a
book.](https://twitter.com/MachineSupply/status/720914581502169088) Because of
course it does.

The selection is changed over every Monday, and you’ll notice that each of the
books has a card on the front [(here’s a
photo)](https://twitter.com/MachineSupply/status/720680713578803200) because
every book is recommended by a real human made of meat.

These cards and the shelf talkers (the label which says the item code and the
price) are beautifully designed by my new friends at [Common
Works](http://commonworks.co.uk). But they’re a pain to produce: For layout,
the templates are in InDesign (which I don’t have), then I have to send an
Excel spreadsheet of the new stock over to Sam at Common Works, which he then
puts into the template, and prints.

My new process comes straight out of the @5point9billion code. The browser is
my layout tool.

So Sam moved from InDesign to the web, and [here are this week’s shelf talkers
as HTML.](http://machine.supply/admin/stock/planograms/5/shelftalkers) This is
part of my admin site, I’ve temporarily turned off permission checking to this
page so you can see. The template is automatically populated with details from
the weekly planogram. (A planogram is the merchandising layout for a set of
shelves or a store.)

And [here’s the exact same page as a
PDF](http://machine.supply/admin/stock/planograms/5/shelftalkers.pdf). The
pipeline is taken from @5point9billion: Phantom is used to grab the webpage,
and this time render it to a PDF, complete with vector fonts and graphics.
Because it’s a PDF, it’s super exact – which it needs to be to print right and
fit neatly on the shelf edge.

It’s much quicker this way.

My rule for Machine Supply, as a side project, is that it should take the
minimum of my time, never feel like an obligation, and I should be able to
manage it on the hoof. As a hobby, it should be [Default
Alive](http://paulgraham.com/aord.html).

So automation is helpful. I like that this mode of generating PDFs can be done
without my laptop: I can do everything from my phone, and print wirelessly.

Anyway. [You should follow
@5point9billion!](https://twitter.com/5point9billion/status/675734875106902016)
It’s fun, and you get a personalised animated GIF every time you pass a star,
generated with the most ludicrous rendering pipeline ever.
