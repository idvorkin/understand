# Artist patronage using Web3: a sketch of a payment mechanism

Here’s an idea for a (possibly) novel form of payment, inspired by the
crypto/Web3 world, specifically to support performers, artists, and creators.
I call it _Stake Patronage._

Perhaps this already exists! In which case let me know.

Some background before I get to the mechanism…

**Why I’m interested in Web3:**

The cryptocurrency world is troubling because of (a) carbon cost, and (b)
scams. BUT in the midst of this are fascinating hints of emerging new
infrastructure for the web.

The consumer web over the past decade has become centred on vast attention
aggregators resting on adtech and a small number of cloud computing providers,
and the economics, incentives, and who-owns-what is at this point locked in.
It’s not great.

With Web3 we may find our way to a new settlement between users and
corporations. Here and there are glimpses of new ways of storing files, new
ways of owning and providing access to data, new ways of asserting identity,
new forms of payments – and from all of this, there may be a route to upend
the status quo.

Is finding the way worth the carbon and the scams? I’m sceptical about whether
crypto will eventually mean (as its boosters promise) a newly egalitarian
economy or breaking up of monopolies or net increase in personal freedom and
agency. Honestly I lack the imagination/faith to imagine a future so totally
transformed. But these new capabilities are tantalising… so I keep a personal
running list of what I find interesting in the Web3 gold rush, in the hope of
spotting something useful in its fundamentals that has immediate
applicability.

**Why I’m interested in novel payment formats:**

New payment formats mean new behaviours.

For example, we’ve got:

_(Of course it’s more fine-grained than that.)_

And you can see what the effects of these being “standard” allows in the
digital space:

Then there are a couple of novel-but-now-accepted payment formats:

What makes a payment format work? Trust. Trust from the consumer that the
vendor won’t run off with their money. Trust from the vendor that the money
will eventually find its way to them.

Deep down, payment formats are implemented as _“payment rails:”_

“Rails” are payment jargon for the technological and financial links between
various entities which allow money movement. Visa provides rails, debit card
networks provide rails, etc etc.

That quote is from this fantastic edition of Patrick McKenzie _a.k.a._
patio11’s series _Bits About Money:_ [BNPLs: Businesses Needing Provided
Legibility (Jan 2022).](https://bam.kalzumeus.com/archive/buy-now-pay-later/)
It unpacks another payment format, BNPL – “Buy Now Pay Later,” which is
beginning to appear all over the web next to the “Buy Now” button as an
alternative to using your credit card. Instant instalment payments, and that
boosts sales for the merchants (a new consumer behaviour).

McKenzie unpacks _payment rails_ in another article which is absolutely worth
absorbing in detail:

You could have made a payment by saying “I’m good for $4; please give me
coffee”, and in some cases (such as stores you have a tab with) that suffices.
But the reason it works at scale is that the trust problem has been solved by
so-called _payment rails,_ which are a constellation of firms that have
implemented a protocol to quickly make a series of offsetting promises about
debts such that the cafe quickly becomes almost positive it is owed money for
the coffee and that that debt will be collected with a very high certainty.

In credit cards, a brief and intentionally simplified version of the actions
of the payment rail is: you agree with your bank that you owe them $4, your
bank agrees with a credit card network that it owes a particular processor
almost $4 (taking a fee), and the credit card processor agrees with the cafe
that it owes them a bit less than $4 (taking another fee).

In the _settlement_ phase of the transaction, the credit card processor makes
an agreement with its bank that it owes the processor a bit less than $4,
which it discharges by having their bank agree that it owes the cafe’s bank a
bit less than $4, which the cafe’s bank discharges by agreeing they owe the
cafe a bit less than $4. And so your debt for coffee is now two offsetting
debts; between you and your credit card issuer, and between the cafe’s bank
and the cafe. You will, at some point in the future, probably up with your
credit card issuer, and the cafe will probably withdraw money from the bank
(perhaps to e.g. buy beans or pay the barista), but from your mutual
perspective the transaction for the coffee will be long over by then.

So the _technical_ implementation of high-trust rails allows for _new
behavior_ from consumers.

HYPOTHESIS: One capability to come out of the Web3 space is novel payment
rails.

Because I’m hand-waving and not talking about end-to-end protocols and
implementation, I’ll just say payment formats, not rails.

With crypto, you’ve got a couple of problems with payments:

Could novel payment formats reduce this friction with crypto transactions, and
provide for new behaviours besides?

**Proof of Stake as the underpinnings of a novel payment format:**

I’m still getting my head around all of this, so let me spell out my
understanding as literally as possible. (Factual corrections gratefully
received. Apologies for being casual with terminology.)

A blockchain is a transaction history. Each new transaction is verified to be
non-fraudulent by looking at that history (you want to avoid double-spending,
for example). The trick is how to do that in such a way that many, many
parties trust that no-one is defrauding the system, and the answer with
cryptocurrencies is that you decentralise the verification and make it so that
all these parties can come to consensus without a single party being in
control. The consensus mechanism varies.

With Bitcoin, the consensus mechanism is based on _Proof of Work._ As part of
compiling the transaction history, verifiers run hard sums for each step, and
the cumulative effect is that it would be _really really expensive and slow_
to fabricate a fictional transaction history in order to defraud people (but,
remarkably, very quick to check whether the history looks legit).

(The verifiers, or “miners” for Bitcoin, get paid the transaction fee.)

Other blockchains use other consensus mechanisms and there is one called
_Proof of Stake_ that burns less computational resources (and therefore less
carbon).

With Proof of Stake, each step in the transaction history is signed off
(“validated”) by someone who holds a large amount of that currency. That’s
provable because it’s part of the transaction history.

Again the transaction history becomes hard to fake. And again the validators
who knit the transaction history into the blockchain get paid the transaction
fee.

_Important note: from what I understand, the big blockchains are shifting to
various variations of Proof of Stake because it more-or-less deals with the
carbon problem. Good news._

Where this gets interesting, for people like you and me (as opposed to the
people with large enough computers to become validators), is with **Delegated
Proof of Stake.**

With Delegated Proof of Stake, a validator doesn’t need to hold coins
themselves. Instead, I can “stake” my coins with a validator, they will
perform the validation, and then they will share the transaction fee reward
with me.

FOR EXAMPLE:

Okay, this is how it works today, and there’s the hint of something
interesting here.

If staking = asset appreciation + yield, could the two income streams be
separated and used for a new recurring payment format?

**Imagining Stake Patronage:**

My proposal is that it should be possible to stake my coins with a validator,
retaining ownership of the coins as before, but name a separate beneficiary
for the yield.

(It’s a variation of Proof of Stake, deep in the blockchain consensus
mechanism itself, and that’s why I call it Stake Patronage.)

The use case here is to support artists and creators, such as with the low
monthly recurring payments offered by services like Patreon and Substack in
the “regular” dollar economy.

So it would work like this:

The format has some benefits:

(By “artists” I know I’m skewing more towards live performers rather than
artists who produce static, tradable works. But I think patronage has pretty
broad applicability.)

**Implementation and user experience:**

I can picture the user experience.

A site, like YouTube but with more social presence, has a number of live
streams available. You can see which are the popular ones because they have a
large number of coins staked for their benefit. Or maybe there are curators
who support up-and-coming artists: curators have patrons too.

(Any platform needs a non-zero-cost score to figure out popularity, if only to
sort the search results. The web has PageRank based on hard-to-earn backlinks;
YouTube has views based on scarce time; Twitter has followers based on scarce
attention. Here, artists would have patrons.)

So there are leaderboards, but of course because Stake Patronage is on the
public blockchain, this is a distributed score, not limited to a single site.

Then, next the live stream, there is a button so that viewers can choose to
stake the coins in their wallet. _“Like, Subscribe and Stake,”_ the performers
say at the end of a set, by way of sign-off.

The site itself would act as a validator, or perhaps partner with an existing
validator.

And then the artists receive yield.

The analogy for me is this: subscribers are stickier than one-off transactions
for writers; patronage is stickier than tip-jars for performers. Just as NFTs
unlocked a new market for visual artists, perhaps Stake Patronage could unlock
a market for performers, artists, and creators more generally.

_In terms of implementation, how would this work?_

Generalised, maybe this isn’t just about patronage. Could yield also be
directed to charities? A way for crypto holders to support good works without
giving up their appreciating asset.

But this is where my hand-waving knowledge really runs out of road.

Of course the above is quite possibly totally wrong-headed. But for me it’s
areas like this where Web3 gets interesting: we can think about behaviours we
want to encourage (like artist patronage) and then tweak the actual underlying
economics to make that a low-friction path. Is this route viable? Unknown. But
the exercise in figuring it out makes me want to spend more energy on finding
opportunities in Web3.

On the off-chance you know how to do this, or you’re at Tezos or Coinbase or
similar and you have a _path_ to knowing how to do this – get in touch? I’m
working on a platform for performers and patrons that is the perfect test-bed
for this.

_Thanks to Ed Cooke and Jon Boutelle at[Sparkle](https://sparklespace.com/)
for conversations and being early readers. Blind spots and misconceptions all
my own. As always this is a snapshot: thinking out loud rather than a final
view._
