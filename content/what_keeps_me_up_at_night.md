# How any of the Big 3 could own connected products

I’ve been doing some competitive landscape analysis around _connected
products/Internet of Things platforms_ – I’ll write up my thoughts soon.
During research I touched on Bluetooth 4, which seems like it could be the
connective tissue of a peripheral ecosystem around smartphones just as USB was
for peripherals around the PC.

And in this section, I hadn’t included [Apple’s MFi
Program](https://developer.apple.com/programs/mfi/) in the list (MFi is
hardware and certification for iPod, iPhone and iPad.)
[Greg](http://gregborenstein.com) asked me why. "Well," I said, "they don’t do
enough UX integration, and besides, I don’t want to give them any ideas. If
they did what I think they should do, they would totally own connected
products."

But hell! The Big 3 are full of the smartest technologists on the planet!

It’s not for lack of ideas that they aren’t doing this.

So here’s how Apple, or Amazon, or Google could totally become the platform
for the future world of connected products, and - with a connected products
platform [of my own](http://bergcloud.com/devkit/) \- the thought that one of
them might make a move like this is what keeps me up at night.

**Starting point:** With the Kindle, Amazon have an amazing chip that has
[global connectivity via
3G](http://www.amazon.com/gp/help/customer/display.html?nodeId=200375890).
They also have a billing model where the content provider pays for delivery
(currently [$0.15/MB](https://kdp.amazon.com/self-
publishing/help?topicId=A29FL26OKE7R7B) for Amazon.com deliveries to the US,
which explains why you don’t get many graphics-heavy books on the Kindle).
This kind of billing infrastructure is hard.

**What happens:** Amazon apply their genius for [service oriented
architecture](http://apievangelist.com/2012/01/12/the-secret-to-amazons-
success-internal-apis/) (SOA) to Kindle’s Whispernet functionality, take
advantage of their economies of scale, and provide wireless chips that any
developer can use. Just as they SOA’d their storage requirements into S3, and
their server farms into EC2 - now both services that are the tarmac of the
modern web - they couple this SOA’d hardware connectivity with [Amazon Web
Services,](http://aws.amazon.com) and create the perfect platform for
connected products. Of course Amazon also own an identity system with
associated credit cards/payments platform. Plus they really _get_ APIs.

Amazon would own connected products. You wouldn’t build on anything else.

**Starting point:** The emerging smartphone peripheral ecosystem (appcessories
and [whatnot](http://gregborenstein.com)) is built around Bluetooth 4, the low
power wireless standard that Apple have been including in
[their](http://appleinsider.com/articles/11/07/20/apple_adds_bluetooth_4_0_support_to_new_macbook_air_mac_mini)
[products](http://en.wikipedia.org/wiki/IPhone_4S) since 2011.

**What happens:** Right now dealing with appcessories on the iPhone sucks
(claiming and syncing), so Apple add some minor UX support, adding hardware
products to the homescreen with a parallel to
[Newstand](<http://en.wikipedia.org/wiki/Newsstand_(application)>) called
**Nightstand** – a virtual table for physical things. You associate each
product with your Apple ID. Then, to solve the problem that connected products
need to talk to the web without a smartphone present, they activate the
Bluetooth 4 already present in the Apple TV (and maybe add one to the Airport
Express), and make it so that any product that can connect via your smartphone
can also connect via any Apple TV you’ve signed in on using the same Apple ID.
For bonus points, [iCloud](https://developer.apple.com/icloud/index.php) is
used for the messaging layer, so any data sent via the Apple TV also shows up
on your iPhone. Of course Apple owns an identity system with associated credit
cards, fully capable of micro-payments and subscriptions.

Apple would own connected products. You wouldn’t build on anything else.

**Starting point:** Android. Motorola.

**What happens:** Google take cheap cellphone guts - the [peace dividend of
the smartphone war](https://twitter.com/cdixon/status/314244533007310849) -and
use Motorola to release a development platform that runs Android, rebooting
the [Android @Home](http://www.businessweek.com/articles/2013-05-08/time-for-
googles-android-at-home-to-make-a-new-splash) program that was launched back
in 2011 with smartphone-controlled lightbulbs. In this new 2013 world of
[Arduino](http://www.arduino.cc) and [Raspberry
Pi,](http://www.raspberrypi.org) hardware is way more accepted… but loads of
people already know how to develop for Android. So developers flock to this
new platform. You’re not locked into Google’s hardware, because Android
hardware is commoditised down to the CPU, unlike similar offerings from Amazon
or Amazon. The UX is provided by Android apps, of course. [Google Cloud
Messaging](http://developer.android.com/google/gcm/index.html) is used to link
the connected hardware to regular ol’ websites that developers build
themselves. Websites are easy, and Google trusts the web. The platform is a
great combination of open and familiar. Google also owns an identity system,
and a payments platform.

(A note: I don’t think Google could pull off the Apple model of a peripheral
ecosystem built around Bluetooth 4. Google doesn’t have enough non-smartphone
presence in the home, and Android fragmentation would be a major problem –
especially Samsung’s ownership of the front room via the Smart TV platform,
which would put the two companies at odds.)

Google would own connected products. You wouldn’t build on anything else.

I wouldn’t back any of ‘em.

It’s true, if any of the Big 3 made a move like this, you’d be dumb to use
anything else for your Kickstarter project or new hardware company. It would
be great. So many common problems would be solved.

But I’d be sad. We’d be stuck with a platform that met our imaginations only
of today. It wouldn’t evolve; big companies are too slow.

We’re only going to discover the weird and wonderful opportunities of
connected products once we’ve rolled our sleeves up and got our hands dirty.
How are connected products going to change our homes, our offices, our cities,
our _social lives?_ Who knows. It’ll take years to find out. And at that
point, maybe we can have a dominant platform. That’ll be fine. Until then
there’s [BERG Cloud](http://bergcloud.com/devkit/) and a dozen others to help
figure it out. There will be more. Let a thousand flowers bloom!
