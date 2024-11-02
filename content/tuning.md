# My new job is AI sommelier and I detect the bouquet of progress

I made an AI clock for my bookshelves! It composes a new poem every minute
using ChatGPT and mysteriously has an enthusiastic vibe which I am totally
into. Kinda. Maybe. Well, see below.

[Here are photos on
Twitter.](https://twitter.com/genmon/status/1636698753007603713) (Check the
thread for more pics.)

The e-ink screen shows:

Eleven-thirty eight, don’t hesitate /

Time to savor life, don’t be late.

And it totally blew up. (rn: 5,987 likes, 802 retweets; 1,165 reactions on
LinkedIn.) So I need to do something with all that interest. It is super
gratifying!

This post is not about that.

BUT having the clock _does_ mean that I’ve been glimpsing AI-generated poetry
pretty regularly for the past few days, plus the time I was making it, so now
I have _opinions._

Opinions about flavours of large language model, of all things.

11:51, time to be bold, /

Minutes tick by, stories untold.

So… the clock displays a rhyming couplet based on the time. The prompt also
feeds it a concise description of the room from its pov, so it sometimes
refers to books or the rug, or its own self as a small screen.

I say it’s generated with ChatGPT but technically what I mean is that it’s a
completion using a model from OpenAI called `gpt-3.5-turbo`.

A model is a giant matrix of numbers that represents how likely it is that one
word comes after a previous sequence of words. Models take months and $x00
million in capex to train. (GPT-5 is currently being trained on an
[estimated](https://twitter.com/davidtayar5/status/1625140481016340483) $225
million of NVIDIA GPUs – graphics cards.) There are now several large language
models in the world though OpenAI’s models are the most available for use.

And they vary! In character and behaviour!

So whereas `gpt-3.5-turbo` is the model behind ChatGPT, I _could_ have used
OpenAI’s previous major model, `text-davinci-003`, commonly called GPT-3 (I
don’t have access to GPT-4 yet).

I spent a morning looking at poetry composed by both models.

If I were an **AI sommelier** I would say that `gpt-3.5-turbo` is smooth and
agreeable with a long finish, though perhaps lacking depth. `text-davinci-003`
is spicy and tight, sophisticated even.

_(Perhaps I AM an AI sommelier. I just made that up. Perhaps I can put that on
my LinkedIn.)_

So `gpt-3.5-turbo` kinda leans towards the vapid with its prose. It’s more
readable, but there’s less variety, and - like an excitable puppy - it
frequently runs on. It’s hard to get it to stick to 2 lines for the poem. It
will fib about the time if that means it can get a rhyme.

`text-davinci-003` is more likely to pick ten-dollar words. It hits those 2
lines reliably and in sometimes surprising ways. With my AI literary critic
hat on (another new career) I way prefer it.

BUT: `gpt-3.5-turbo` is 10% of the price.

That AI clock costs me $1.80 per day to run. It’s composing a new poem every
minute so that’s 3,600 completions a day.

I prefer davinci’s words… but do I like them enough to pay $18/day? Punchy.
No.

Though if anyone were to commission me for lobby art, davinci is what I’d
reach for. _(You know how to reach me…)_

The clock strikes one-thirty-eight, /

Afternoon sun shines bright with fate.

Another difference between models is **instruction tuning.**

Once you’ve hoovered up all the text on the internet and trained your model,
you can do something called “fine-tuning” which is to bias it to respond in a
certain kind of way. You can feed it, say, a corpus of scientific papers, and
then the model will respond in a way that sounds more like that.

The model behind ChatGPT, `gpt-3.5-turbo`, has been fine-tuned based on actual
user interactions, as ranked by OpenAI:

To make our models safer, more helpful, and more aligned, we use an existing
technique called reinforcement learning from human feedback (RLHF). On prompts
submitted by our customers to the API, our labelers provide demonstrations of
the desired model behavior, and rank several outputs from our models. We then
use this data to fine-tune GPT-3.

In particular, the actual user interactions consist of questions, chat,
requests, and so on, not just a partial sentence to be completed.

Which explains ChatGPT’s agreeableness and, well, chattiness.

The best way to notice instruction tuning is to play with a model that
_hasn’t_ been instruction tuned.

Facebook’s large language model, LLaMA, is available to researchers and has
also recently leaked. Simon Willison details [how to run LLaMA on your own
laptop](https://til.simonwillison.net/llms/llama-7b-m2) if you’re so inclined.
And if you can get your hands on the model _(ahem cough)._

It is amazing to run this on your own machine!

But - and this is the best way I can communicate this - it’s like talking to
someone who is asleep, or hypnotised.

This AI sommelier says that LLaMA _mumbles._ It’s like talking to an ancient
wizard who repeats the last half of your sentence and then rambles on a bit
and then starts talking in circles.

Whereas ChatGPT – we’re interacting! It’s awake!

Now I know (or at least assume) that neither of these models are sentient, but
the difference is night and day.

Instruction tuning!

In cozy shelves, I do reside, /

It’s nearly noon, the clock confides.

AND THEN there’s ChatGPT’s quiet obsession with _progress._

My prompt for the AI clock tells the model that it’s a rhyming clock, and
about its embodied situation, and also gives it some pointers about how to
respond. In particular I whispered this line in its ear:

Be imaginative and profound. Sometimes refer to your physical situation.

Now, I experimented with a variety of prompts.

I tried out adding the word “playful”. I tried “motivational,” and “poetic.”

All of those _modified_ the vibe.

I also tried a prompt which asked the clock to sometimes refer to the future.
I wanted solarpunk epigrams!

I included a little detail - about humanity and progress and the galaxy - just
as I provide detail about the physical situation: the room and the rug, the
bookshelves, the books and the Lego that the small screen is next to.

But I found that, when I included the idea of the _“future,”_ this dominated
every response from the model.

Like, _every_ poem included a reference to the future; variety collapsed.

And the only way I can read that is that there is something in the instruction
tuning of `gpt-3.5-turbo` which includes a belief in progress? A bias towards
the future, rather than pastoral conservatism, which can manifest in an almost
pushy fashion from time to time?

And so a mere mention of the future reinforces this bias and brings it to the
surface.

I don’t know how explicit this is - maybe it’s encoded unknowingly in the bias
of the rankings from the OpenAI team - but, with my AI sommelier hat back on,
I sense that progressivism is in the _bouquet,_ somehow.

Because even _without_ the gravity of the “future” concept in the prompt, this
motivational hustle still comes through from the AI clock – and I didn’t put
it there.

Tick tock, don’t mock, it’s 9:29 on the dot. /

Time to rise and shine, leave the bed and get in line.

_Look:_ an analogy.

Back in 2014, Facebook conducted "a vast experiment in which it manipulated
information posted on 689,000 users’ home pages and found it could make people
feel more positive or negative through a process of ‘emotional contagion’."

In a study with academics from Cornell and the University of California,
Facebook filtered users’ news feeds - the flow of comments, videos, pictures
and web links posted by other people in their social network. One test reduced
users’ exposure to their friends’ “positive emotional content”, resulting in
fewer positive posts of their own. Another test reduced exposure to “negative
emotional content” and the opposite happened.

The study concluded: “Emotions expressed by friends, via online social
networks, influence our own moods, constituting, to our knowledge, _the first
experimental evidence for massive-scale emotional contagion via social
networks._ “

This was unethical.

But at least it was being studied! It was performed knowingly!

OpenAI, to its credit, does deep work into the unintended capabilities and
societal impact of GPT. There’s the GPT-4 “Safety Card,” [as previously
discussed](/home/2023/03/16/singularity), including a “red team” _(a group
which tries to do the bad thing, to see what happens, so we can anticipate and
prepare)_ which investigated the possibility for automated propaganda via
large language models:

Based on GPT-4’s performance at related language tasks, we expect it to be
better than GPT-3 at these sorts of tasks, which increases the risk that bad
actors could use GPT-4 to create misleading content and that _society’s future
epistemic views could be partially shaped by persuasive LLMs._

I would suggest, for the _next_ Safety Card, the red team investigates what
happens when consulting ChatGPT is widespread by students, in business, and by
politicians – and when there is a gentle systemic bias of this kind towards
_(hand waves)_ “the future.”

_(And, if so, could there be a instruction-tuning hack on the societal psyche
of another nation… a la[state-sponsored fashion
hacks](/home/2022/08/16/fashion)…)_

Maybe it’s fine! Maybe we’ll all get in our rockets and inhabit the galaxy
without really understanding why! Maybe we don’t need to sit and contemplate!

Maybe I’m imagining things and none of it means anything at all!

Most likely scenario tbh. But still.
