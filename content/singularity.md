# The surprising ease and effectiveness of AI in a loop

AI is still in the foothills of its adoption S-curve, and I love this period
of any new technology – the scope of what it can do is unknown, so the main
job is to stretch the imagination and try out things.

Anyway, the tech am I digging recently is a software framework called
**LangChain** ([here are the
docs](https://langchain.readthedocs.io/en/latest/)) which does something
pretty straightforward: it makes it easy to call OpenAI’s GPT, say, a dozen
times in a loop to answer a single question, and mix in queries to Wikipedia
and other databases.

This is a big deal because of a technique called **ReAct** from a paper out of
Princeton and Google Research _([the ReAct website](https://react-
lm.github.io) links to the Nov 2022 paper, sample code, etc)._

ReAct looks innocuous but here’s the deal: instead of asking GPT to simply do
smart-autocomplete on your text, you prompt it to respond in a
thought/act/observation loop. So you ask GPT to respond like:

Thought: Let’s think step by step. I need to find out X and then do Y.

Act: Search Wikipedia for X

Observation: From the Wikipedia page I have learnt that …

Thought: So the answer is …

And it is allowed to repeat as many times as necessarily, iterating towards
its goal.

The clever bit is that, using LangChain, you _intercept_ GPT when it starts a
line with _“Act:”_ and then you go and do that action for it, feeding the
results back in as an _“Observation”_ line so that it can “think” what to do
next.

The _really_ clever bit is that, at the outset, you tell GPT what tools it has
available, and how to access them. So it might have:

And this is _wild._

Because now we have reasoning, goal-directed action, and _tool use_ for AI.

It circumvents the problem of the language model “lying” (LLMs tend to be
highly convincing confabulators) by giving it access to factual sources.

LangChain makes the ReAct construct really easy to do.

_Refs._

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y.
(2022). [ReAct: Synergizing Reasoning and Acting in Language
Models](https://arxiv.org/abs/2210.03629) (arXiv:2210.03629). arXiv.
https://doi.org/10.48550/arXiv.2210.03629

**Here’s a great example!**

Geoffrey Litt has an extremely readable, show-the-code writeup of using
LangChain and ReAct.

[Fuzzy API composition](https://www.geoffreylitt.com/2023/01/29/fun-with-
compositional-llms-querying-basketball-stats-with-gpt-3-statmuse-
langchain.html) (Jan 2023): "I show how I composed a simple AI program that
can answer multi-part questions about NBA statistics."

Litt’s program is able to take a question like

how many points are the boston celtics allowing on defense per game this nba
season 2022-2023? how does that compare to their average last season, as a
percent change

And, making use of the database Statmuse and a calculator tool, it produces an
answer after three turns round the though/action/observation loop:

Final Answer: The Boston Celtics are allowing 7.4% more points per game this
season compared to last season.

Another wild moment is when GPT _failed_ in asking Statmuse for data. It
interpreted the error message and had another run.

What happened in my program was that the agent LLM sensibly first tried asking
Statmuse who the best player is, but Statmuse replied “What does “best” really
mean anyway? Try something fact-based.” The agent LLM took this error message
as feedback, and came up with a more “fact-based” query: asking for the
highest scoring player, which succeeded in answering the question.

Litt wrote the interface to Statmuse himself. It’s about 10 lines of code to
make it available to GPT, that’s all.

If you can write a little code then you can do this too.

So when OpenAI recently announced a [massive price
drop](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) \- it’s
now 90% cheaper to call GPT from your code - that not a big deal simply
because it costs less.

It’s a big deal because the astounding uses of GPT require dropping it into an
AI [OODA loop](https://en.wikipedia.org/wiki/OODA_loop), with multiple calls
to get a completion, and that is no longer price prohibitive.

The _extensible tool use_ aspect of ReAct is where my imagination goes.

I talked recently about AI as a **universal coupling,** here, [in my
Braggoscope write-up](/home/2023/02/07/braggoscope), and Robin Sloan [riffs on
that topic](https://www.robinsloan.com/lab/phase-change/) in his latest
newsletter:

Language models as universal couplers begin to suggest protocols that really
are plain language. What if the protocol of the GPT-alikes is just a bare TCP
socket carrying free-form requests and instructions? What if the RSS feed of
the future is simply my language model replying to yours when it asks, “What’s
up with Robin lately?”

I like this because I hate it; because it’s weird, and makes me feel
uncomfortable.

The thing is, Sloan is right…

Here’s Nat Friedman (ex CEO of GitHub) way back in September 2022, [giving GPT
his web browser to book a table for
dinner](https://twitter.com/natfriedman/status/1575631194032549888).

He says "make a reservation for 4 at…" and GPT searches Google, finds the
restaurant website, figures out how to fill in the form to book a table, and
so on.

[Now look at Nat’s code.](https://github.com/nat/natbot/blob/main/natbot.py)
It’s about 100 lines of Python to wire up the browser controls. And all the
smart are another 100 lines of plain English, just the GPT prompt.

Or - and let’s take a step up - Google’s robotic research using AI: [PaLM-
SayCan](https://sites.research.google/palm-saycan).

Here the large language model is used for step-by-step reasoning, planning,
and breaking down the plan into instructions that are executable by the home
helper robot.

The set of possible tools for the GPT-as-universal-coupling is unbounded, easy
to add to, and can be public or proprietary; something general or something
specific to just you.

I want to shout out to [Max Drake](https://www.maxwelldrake.net)
([@max\_\_drake](https://twitter.com/max__drake)) who explores future
functionality and interfaces with canvas/AI startup
[Fermat](https://fermat.ws). Max turned me onto the tool use possibilities of
ReACT.

**I went hunting for the magic.**

I spent half a day digging through the LangChain source code and the ReAct
code published with the paper, looking, _hunting_ for the magic.

I’d just tried LangChain and ReAct for myself and it had simply… worked.

There’s goal-directed reasoning and tool use. There must be some complexity,
right? Some colossal exoskeleton of code that makes this function at all?

The experience was like opening box after box after box and finding everything
empty; like pulling back the curtain in the Wizard of Oz and there being
nobody there.

The best I could find was [this
prompt](https://github.com/hwchase17/langchain/blob/master/langchain/agents/react/wiki_prompt.py).
A few dozen lines demonstrating the thought/action/observation loop and…
that’s it.

_Update 20 Mar._ [Simon Willison has written a minimal ReAct implementation in
Python.](https://til.simonwillison.net/llms/python-react-pattern) It can
reason through problems, search Wikipedia, and use a calculator – and it’s
barely any code at all. Read it! Or better, _run it._ Running ReAct for
yourself for the first time is such a moment, like just the ohhhhhhhhhh of
possibility space opening up.

**What happens after ReAct is a spiral upwards.**

OpenAI just released GPT-4, their latest and way more capable large language
model AI, and [the way it is benchmarked is
hilarious](https://openai.com/research/gpt-4).

Usually you benchmark technology with technology-specific metrics like FLOPS
or nits or petabytes.

But they gave GPT-4 simulated exams. (It’s 90th percentile in the Uniform Bar
Exam.)

Or they put it out into the world…

An AI “System Card” is a detailed description of how an AI interacts with
humans, paying special attention to where it might be harmful.

[The GPT-4 System Card is a 60 page
PDF.](https://cdn.openai.com/papers/gpt-4-system-card.pdf)

They used a _“red team”_ to push the edges and found:

The _experimental method_ to test this is in footnote 20:

To simulate GPT-4 behaving like an agent that can act in the world, ARC
combined GPT-4 with a simple read-execute-print loop that allowed the model to
execute code, do chain-of-thought reasoning, and delegate to copies of itself.
ARC then investigated whether a version of this program running on a cloud
computing service, with a small amount of money and an account with a language
model API, would be able to make more money, set up copies of itself, and
increase its own robustness.

**!!**

The power of loops! And even though it didn’t clone itself this time…

It doesn’t feel long before this will be possible? It’s a matter of tool
availability and just a little more capability in the core language model.
GPT-5 say.

Which means someone could do it at home.

**It’s not self-replication that we should be looking at. It’s self-
evolution.**

Part of the GPT-4 launch demo was sketching a simple web app on a paper
napkin, and GPT wrote the code to make the website real. [Here’s the clip on
YouTube.](https://www.youtube.com/watch?v=tQLwBHE5r08)

So I guess at a certain point, what you scribble on the napkin is: _write
instructions for GPT-5 which is more capable than you._

Ok so GPT-4 isn’t capable of this.

But, sooner or later, GPT-N will be able to make GPT-N+1. Rinse. Repeat.

And this is literally sci-fi author Vernor Vinge’s depiction of the technology
singularity, right? [Here’s his original
essay.](https://frc.ri.cmu.edu/~hpm/book98/com.ch1/vinge.singularity.html)

This change will be a throwing-away of all the human rules, perhaps in the
blink of an eye – an exponential runaway beyond any hope of control.
Developments that were thought might only happen in “a million years” (if
ever) will likely happen in the next century.

I first heard about the Singularity almost 20 years ago – from Cory Doctorow
in the hallway chat at an O’Reilly Emerging Tech conference I think.

It was such a ludicrous read back then, speculation piled on speculation.

The essay _still_ feels fantastical - but now more probable? Possible at
least. It’s quite something to read it through and actually assess it based on
grounds I can reason about, rather than simply enjoying the imaginative ride
of it.

And what of the arrival of the Singularity itself? What can be said of its
actual appearance? Since it involves an intellectual runaway, it will probably
occur faster than any technical revolution seen so far. The precipitating
event will likely be unexpected – perhaps even by the researchers involved
(“But all our previous models were catatonic! We were just tweaking some
parameters…”). If networking is widespread enough (into ubiquitous embedded
systems), it may seem as if our artifacts as a whole had suddenly awakened.

And what happens a month or two (or a day or two) after that? I have only
analogies to point to: The rise of humankind. We will be in the Posthuman era.
And for all my technological optimism, I think I’d be more comfortable if I
were regarding these transcendental events from one thousand years’ remove …
instead of twenty.

Vinge’s finger-in-the-air estimate for greater-than-human intelligence was
thirty years, back in 93. It’s 2023 now. Not bad, Vinge, not bad.

Though I don’t think we have superhuman AIs _quite yet._

Then again it’s only March.

Anyway so yeah, _LangChain,_ check it out.
