# Self-driving corporations

I’ve been thinking about how companies could be automated, and what we would
use them for if that were possible.

Think of something like [Stripe Atlas](https://stripe.com/atlas): "Spend 10
minutes filling out a bit of information, and then we’ll create the legal
framework for your company"… including legal docs, paperwork filing, getting a
tax ID, issuing stock, and so on. All for $500 and some form-filling.

This is for company _formation_ – what if it was that easy ongoing?

I have a couple of basic use cases in mind:

The second is close to my heart because it’s what I do right now.

I reckon I could write an operations manual for a micro agency pretty simply.
We had a _“choose your own adventure”_ style operations manual at
[BERG](http://berglondon.com) in the form of linked checklists. Like, “is it a
Friday? Do bank reconciliation. Is it the last Tuesday of the month? Then
process holidays, process employee changes, run payroll,” and so on. It built
up over time.

But what if the “agency in a book” could be software? What if the checklist
was actually a set of forms, and the forms actually filed the paperwork?

Forming a company is the easy bit. The challenge is running it, because

For example: for [Mwie Ltd](http://www.mwie.com), now is the time I have to
file my Confirmation Statement which declares the current shareholders of my
company. It’s easy to do because my accountants have made a screen to look at
and a button to click… but if I forget to visit the website before 24
November, I’ll be in a ton of trouble.

This ongoing form filing is called “compliance.”

Right now, there are a ton of tools to help you manage the _output_ of your
company (Shopify, Trello, PowerPoint) but very few to manage the _compliance._

Okay, so there are tools to make form-filling easier. I can employ a payroll
company to file on my behalf. Or I can employ an accountant to ask me
questions once per year, and prepare my yearly accounts.

What I want is to flip the model.

The automated corporation (which is software) should always be in legal
compliance, even if I do nothing. So the forms should, behind the scenes, be
printed and sent off; the accounts submitted; the quarterly VAT returns made
and paid.

This requires automation of my bank account, I know.

But what I’m saying is that my self-driving corporation should, once formed,
stay on the road, whatever forms and robot phone calls it takes.

But if I forget to reply to the email, or forget to log a benefit, or
accidentally pay someone below minimum wage, or run out of cash, the company
will be operating illegal. _This should never happen._

Think about a desktop computer. I can’t drag a folder icon inside itself and
break the file system. The computer doesn’t let me.

Or, more technically, consider databases. Databases confirm to the
[ACID](https://en.wikipedia.org/wiki/ACID) properties: "ACID (atomicity,
consistency, isolation, durability) is a set of properties of database
transactions intended to guarantee data validity despite errors, power
failures, and other mishaps."

In short, no matter what you ask a well-designed database to do, you won’t end
up with broken or illogical data.

What would it mean to have such a guarantee for a self-driving corporation?

So, for example:

What I mean is that the self-driving corporation would only allow actions that
can be guaranteed to be downstream legally compliant.

That would mean that this company wouldn’t be as flexible as a regular, human-
driven company. It would have more limited contracts, for example. But it
would be impossible to crash it.

_(One question is about how to implement this. One mechanism might be to
require, in the incorporation legal, that all contracts require two directors.
But one of the directors is a robot who will only sign off on provably
compliant contracts.)_

In any complex system, there is always the possibility that things go off the
rails. What if someone sues this autonomous corporation? What if the tax laws
change radically?

Rather than the company “crashing” (which, in this situation, means that it
ends up operating illegally and the shareholders risk a fine or worse), there
would need to be some kind of exception handling:

I think of this a little like early evolution of computers. They ran raw
machine code. The core insight of the interactive computer was the event loop.
And every so often, it would crash. So then there were friendly ways of
crashing (the blue screen of death) and then of isolating crashes (this
application is not responding) and then ways of catching errors so that the
app can be improved for everyone (would you like to share the crash report
with the developers).

This is a bit of a thought experiment.

I [talked back in 2014](/home/2014/12/23/corporations) about "a little bottle-
city company … corporate governance as executable code" – and what I’m talking
about here is implementing the minimum viable version of that: a guaranteed
compliant, self-driving corporation, implemented in software, a layer that
sits between (a) the world of banks and government departments and paper, and
(b) the human owners and employees.

I suspect it would be both cheaper and simpler (I spend perhaps 5% of my time
and 3% of my income on the Red Queen’s race of company compliance, and I know
what I’m doing) so that increases the number of people who would be operating
independently, or starting companies, but can’t because of the existing
hurdle.

But more interestingly, an autonomous corporation is interoperable with
software. So Shopify could form and run a company for you, accounts and
contracts and all, guaranteed no shooting yourself in the foot. Or maybe a
blog could be its own company, and registering a Wordpress account would
automatically register it? Or a vending machine?

What would it mean to buy a “Dummies Guide” to starting, say, a roofing
business, and the book is code and you can just boot it up?
