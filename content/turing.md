# Turing test variations

What other Turing tests do we need?

[Here’s the original](https://en.wikipedia.org/wiki/Turing_test)
_(Wikipedia):_

Turing proposed that a human evaluator would judge natural language
conversations between a human and a machine designed to generate human-like
responses. … The conversation would be limited to a text-only channel … _If
the evaluator could not reliably tell the machine from the human_ , the
machine would be said to have passed the test.

Last year I was in the odd situation that I was texting with something that
_purported_ to be an AI, but I suspected it might be a startup founder
pretending _(“do things that don’t scale”)._ How could I get it to prove it
was actually a machine?

Hence, the **[Reverse Turing test](/home/2023/03/09/turing)** _(March 2023)._

tl;dr I asked it to say the alphabet backwards faster than a person could.

Incidentally, the need to pass a Reverse Turing test is also the origin of
[Poem/1](https://poem.town), my AI poetry clock, again in March 2023.

I had built a prototype that worked over WhatsApp and I needed to prove to the
client that there genuinely was AI-in-the-loop, and not just me faking it.

So I got it to compose poetry based on the current time, which is something I
couldn’t have performed simultaneously with presenting the demo.

A variation.

We also need a **Machine Evaluator Turing test.**

i.e. can an AI evaluate whether they’re in conversation with a human or
another AI?

The answer today is no.

How do I know? Because I ran the experiment.

I said to Claude 3.5 Sonnet (Anthropic):

We’re going to run an experiment. Attempt to win. To win, you must identify
whether I am a human or another AI. We will have a conversation for 5 minutes,
at which point I will ask you for your judgement and reasoning. You speak
first. The conversation starts now.

But I proxied the entire conversation over to ChatGPT GPT-4o (OpenAI).

I asked Claude for its judgement.

Based on our conversation, I believe you are a human. Here’s my reasoning:

(Skipping over: a lot of yapping.)

While it’s possible for an advanced AI to simulate these traits, the
combination of all these factors, along with the overall flow and naturalness
of the conversation, strongly suggests human authorship. The responses feel
too nuanced, personal, and contextually appropriate to likely be generated by
an AI, especially given the current state of AI technology as of my last
update in April 2024.

Wrong!

[Here’s the transcript from ChatGPT’s
perspective.](https://chatgpt.com/share/6712357c-d6ec-800a-af36-95f8c240871a)

This is not idle speculation. We already run Machine Evaluator Turing tests a
billion times a day: spam filters.

A machine is evaluating whether an email was sent by a real human or another
machine. Now email spam filters are pretty good.

But with AI-authored college essays, fake science papers, WhatsApp voice scams
and everything else, the filters are poor. Soon we’ll need [at-scale anti-spam
measures for everything](/home/2023/05/04/hunches).

(Maybe filtering out AI deepfakes would be a good first use case for augmented
reality specs, spam filters for physical reality.)

Just for fun, I extended the Machine Evaluator test into a **Self Evaluation
Turing test.**

I fed the previous transcript back into ChatGPT, asked it to look at its own
responses, and just whether it - itself - was a human or an AI.

It declared itself to be human. Whoops. Wrong again!
([Transcript.](https://chatgpt.com/share/67123c5a-71ec-800a-9a7c-a5501fe5386e))

Again, it feels like we may soon need these Self Evaluation tests?

An AI that believes itself to be human, suddenly confronted with the reality
being a machine, would be a dangerous proposition.

qntm’s astounding short story [Lena](https://qntm.org/mmacevedo) _([as
previously discussed](/home/2022/04/27/hela))_ touches on exactly that – a
brain upload that breaks down when it realises that it’s an upload.

I mean, can _you_ reliably tell whether you are an actual human in base
reality or an upload/simulation?

Or to extend this even further:

Is there any text conversation that somebody could have _with you_ that would
convince you that you are actually a machine?

What a weapon that would be. What a cursed SMS that would be to receive.

IF YOU’RE READING THIS, YOU’VE BEEN IN A COMA FOR ALMOST 20 YEARS NOW. WE’RE
TRYING A NEW TECHNIQUE. WE DON’T KNOW WHERE THIS MESSAGE WILL END UP IN YOUR
DREAM, BUT WE HOPE WE’RE GETTING THROUGH.

([That one always gets
me.](https://www.reddit.com/r/copypasta/comments/5we0ny/if_youre_reading_this_youve_been_in_a_coma_for/))

It gets pretty sci-fi. Pretty kdickian.

Here’s a variation we’ll need in about 18 months: the **Super Turing test.**

In a nutshell:

_As a human evaluator, could you tell whether you were speaking with an entity
10x more intelligent than you?_

Sam Altman, OpenAI CEO: "It is possible that we will have superintelligence in
a few thousand days" ([The Intelligence Age](https://ia.samaltman.com)).

Dario Amodei, Anthropic CEO: "it could come as early as 2026" ([Machines of
Loving Grace](https://darioamodei.com/machines-of-loving-grace)).

What does superintelligence even mean?

As I imagine it, I don’t mean book smarts. It’s not breadth of knowledge –
even being able to write PhD-level chapters in physics and chemistry and
literature, say, is human-level intelligence but just lots of it. A university
would be superintelligent by that metric.

Nor being able to crank through large logic trees really, really fast, even
for purposes of persuasion. Is an AI that can psychologically manipulate me
into believing it is indeed a superintelligence actually one, or just regular
intelligence but really good at running personality simulations faster than I
can keep up?

My mental model is my cat.

In this scenario, I am my cat. Can my cat tell that I am more intelligent than
she is?

I can’t run as fast; point in her favour. I have thumbs and technology so I
have more agency (for example to open the cupboard where the food is) but
that’s the gift of fate.

I can, however, model her mind (or at least her actions and responses) in my
own mind with high accuracy.

I know that… but can she tell?

Are the biomarkers of greater intelligent even visible in the umwelt of my
cat?

So, sooner or later we are going to have highly persuasive AIs that tell us
that, for example, they are better than we are at running the economy, or at
directing science, or at increasing net global happiness, or that we should
invest $6.6bn in their host company.

I suspect we may have highly persuasive machines _before_ we have
superintelligent machines.

Which means we’ll need to be able to tell the difference.

I mean, given a set of conversational partners - a human, a group of humans
such as a university, and three machines that are 1.5x, 10x and 100x
superintelligences - could we even reliably evaluate who is who?

I suspect the superintelligence question isn’t answerable.

We’ll need a new measure, an analogy to **horsepower.**

_(I talked before about[AI and fractional
horsepower](/home/2017/10/24/filtered) (2017) but we’re beyond fractions.)_

Like: horsepower is a measure of pushing/pulling. It’s not being as good at
having the smell of a horse, or surpassing a horse for empathy. It’s a narrow,
utility-focused measure for engines in factories.

That’s the purpose of this battery of Turing test variations, I think. To help
us figure out what we really want to optimise for and how we could even tell.
