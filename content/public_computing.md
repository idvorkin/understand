# Public computing and two ideas for touchless interfaces

Think about ATMs, or keypads on vending machines, or Amazon lockers, or
supermarket self-checkout, or touchscreens on kiosks to buy train tickets. Now
there’s a virus that spreads by touch, how do we redesign these shared
interfaces?

_(This post prompted because I know two people who have separately been
grappling with public computing recently. There must be something in the air.
These are two ideas I came up with in those conversations.)_

The obvious approach is to move the control surface to a smartphone app, just
like the Zipcar app lets me unlock my rental or sound the horn. But as an
answer, it’s pretty thin… how does a person discover the smartphone app is
there to be used? How do you ensure, in a natural fashion, that only the
person actively “using” the ticket machine or locker is using the app, and
everyone else has to wait their turn? A good approach would deal with these
interaction design concerns too.

So, imagine your train ticket machine. Because of the printer, it’s a _modal_
device: although it’s public, only one person can use it at a time.

Let’s get rid of the touchscreen and replace it with a big QR code.

Scan this code with your smartphone camera, and the QR code is magically
replaced - in the camera view - with an interactive, 3D, augmented reality
model of what the physical interface would be: menu options, a numeric keypad,
and so on.

There’s something that tickles me about the physicality of the interface only
visible through the smartphone camera viewfinder.

_How does it work?_ An exercise for the reader… the iPhone can launch a
website directly from a QR code seen in the camera view. So perhaps that
website includes a webcam view which can add the augmented reality interface?
Or perhaps it triggers an app download which similarly includes the camera
view? (Android has the ability to run mini _Instant Apps_ direct from the
store; there are rumours about iOS doing the same.)

The point is to make the transition from the QR code to the AR interface as
invisible and immediate as possible. No intermediate steps or confirmations or
changes in metaphor: it should feel like your phone is a little window that
you’re reaching through to work with the computer, like using a [scientific
glovebox](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Columbus/Microgravity_Science_Glovebox)
in a chemistry laboratory, and you’re just moving it into position.

The bonus here is that the interface can only be used while the user is
standing directly in front of it, so the “one person at a time” nature of the
machine is communicated through natural physicality. I don’t think you get
that with apps; an app tethered to a place would feel wrong.

The starting point here is a kiosk with a touchscreen.

Obviously we don’t want the touchscreen to be touched by the general public
with their filthy, virus-infested fingers. So, instead, use a tablet with a
camera in it, but the screen of the tablet is not intended to be touched. The
camera instead recognises hand gestures such as

The inspiration is this gorgeous [Rock Paper Scissors browser
game](https://tenso.rs/demos/rock-paper-scissors/) that uses machine learning
and the webcam. That is, the web browser activates your webcam, and you make a
fist (rock), flat hand (paper), or scissors gesture, and the A.I. _which is
also running in the web browser_ recognises it, and then the computer makes
its move. All without hitting the server.

Check out the live graph in the background of that site. It provides a view of
the classifier internals - how confident the machine is in recognising your
gesture.

_What this tells me_ is that all of this can be done with a web browser and a
tablet with a camera in it. For robustness, stick the tablet _inside_ the shop
window, looking out through the glass. Set the web browser to show the live
feed from the webcam, providing discoverability: people will see the moving
image, understand it as a mirror, and experiment with gestures.

It would be like a touchscreen with very large buttons, only you wave at it to
interact.

Look, the [Minority Report gestural
interface](https://www.youtube.com/watch?v=PJqbivkm0Ms) is cool but dumb
because your arms get knackered in like 30 seconds. But just using your hands
or fingers? I could live with a future where we do tiny techno dancing at our
devices to interact with them.

Whatever the approaches, the important considerations for public computing
interfaces would seem to be:

On **accessibility,** I’m into Microsoft’s [Inclusive
Design](https://www.microsoft.com/design/inclusive/) approach - to see it
summarised in a single graphic, scroll to the [permanent/temporary/situation
diagram here](https://blog.stormid.com/what-does-inclusive-design-mean/):
accommodations might be required for visual impairments, but a person with a
cataract has _temporary_ blindness; a distracted driver has _situational_
blindness. For me, understanding situational accessibility (like, having my
arms full of shopping or a wriggling toddler so I can’t press a touchscreen)
really made me start thinking about accessibility in a much broader way.

**Viability** is about the commercial and physical reality of public computing
interfaces: can it withstand being used 100s of times daily, is it reliable in
the rain, is it cheap, etc.

BUT, LIKE, ALSO:

Touchscreens with cameras, web browsers with computer vision, broadly deployed
smartphones, augmented reality, voice: these technologies weren’t around when
the last generation of public computing interfaces was being invented. It
might be worth experimenting to see what else can be done?
