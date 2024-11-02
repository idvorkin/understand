# Prompt engineering and prompt whispering

Hi Sid

Thanks for your message!

_I was wondering if you could tell me what you see as the distinctions between
prompt whispering and prompt engineering._

I guess it’s two questions isn’t it: if there’s a difference and, if there is,
whether it’s useful to make it.

**Prompt engineering** I see as treating prompts like Lego, and being _able_
to treat prompts like Lego, and all that requires.

For example I’m working with one startup (code named _Austin)_ and we’re using
a large language model (GPT-3) as an agent to talk a user through various
tasks.

It can perform other functions aside from speaking to the user: it can write
to a persistent log book for example. It needs to be reliable and to have the
same “personality” throughout.

So there’s an architecture to the prompts. One part to set the tone, another
to set the output format, another to set up a “chain of thought” pattern
(because the result is better that way), another to set the available
functions and how they’re used. Then each task is its own sub-prompt,
dynamically inserted as appropriate, each with its own goal and instruction
sequence. This keeps overall prompt complexity low and prevents instruction
drift. The agents jump between these constructed prompts as it jumps between
current tasks.

Ideally the sub-prompt parts would be semantically isolated, like blocks of
code, but the nature of things means that they’re not. If the personality of
the agent is wild and quirky then that’s going to escape the vibe scope and
contaminate behaviour in, say, the part of the prompt that insists on a
particular structured output.

Then, because it’s engineering, you need observability and logging and tracing
for debugging. And also, because this is a team sport, you need tooling and
jigs so that others can compose their own prompts out of your kit of parts and
see what happens, or for them to tweak the wording and A/B test the result.

And we haven’t even got into the overall AI system, chaining together
different prompts with semantic search or database lookups and API calls, or
fine-tuning an LLM, or whatever.

I think it’s the need for composability and reliability at scale that means
this slots into the _software engineering_ mould, hence “prompt engineering”.
Though whether the term is around for the long term, who knows? I remember
when even tiny startups would have a dedicated database administrator to tune
the database, write SQL and optimise queries, and so on, and is “DBA” still a
commonplace role? Not really.

Then there’s **prompt whispering** which is a bit of a gag I admit. I first
used it pre ChatGPT in the context of image synthesis, [in June
2022](/home/2022/06/02/dalle):

"What’s happening is a new practice of prompt engineering – or rather let’s
call it prompt whispering. Prompt whisperers have a sophisticated mental model
of the AI’s dynamic behaviour… or its psychology even?" – and I don’t know
whether I’d put it in quite those terms today, then again maybe it’s close
enough.

_(btw I doubt that I coined the term. I didn’t consciously borrow it from
anywhere specific - it felt new to me - but also I feel like it was in the
air. There’s also my follow-up short story,[The Prompt
Whisperer](/home/2022/08/03/whisperer).)_

I’m currently solving [Braggoscope](https://www.braggoscope.com)‘s errors in
classifying episodes by Dewey number by asking the LLM to give its rationale
for the classification in the JSON property immediately preceding the number
itself. Accuracy has improved. That feels more like whispering than
engineering.

Another example: I was in a workshop recently with a team learning how to
prompt images. Their first attempt read more like a Google query… and the
results were not quite assinine but straightforward. Next we asked an LLM to
describe a potential image in great detail, what I’d call an open prompt, then
fed that into the image generator – the results were generative, something our
imaginations could bounce off.

Now I don’t mean to say that prompt whispering is “creative” necessarily. It’s
not the opposite of prompt engineering. It’s maybe the difference between
software engineering and hacking? A great hacker can coax the machine into
doing something that others can’t.

It’s a deft turn of phrase or a nudge with a single word that has a
disproportionate effect on the output. It’s a sensitivity to when prompting
the model feels like you’re at a divergent, unstable point with respect to
user input - a saddle point in latent space - and how to concisely solve for
that. (For example: sometimes when you ask an LLM to output JSON, sometimes
it’ll do that consistently as you change parameters, and sometimes it’ll be
buggy. Don’t just use regenerating guardrails on the output if the latter
happens, that’s a brittle fix. Rethink the approach instead.)

It’s being an [AI sommelier](/home/2023/03/22/tuning) of different models, and
having particularly good hunches about what words are likely to lead to what
desired results.

Now the reason I feel like “prompt whispering” might be an overblown phrase is
that it’s just a knack. Being a horse whisperer means that you have a deep and
almost psychic empathy with horses. Being a prompt whisperer on the other hand
is only like being good at Google or effective at looking stuff up in
libraries using index cards or knowing how to avoid asking leading questions
when you are cross-examining a witness.

Yet… there is an intuitive component here? And people can indeed be noticeably
better and worse at prompting? The knack is in some part innate, in some part
trainable, and in some part reliant on personal mental models of how LLMs work
– whether or not those mental models are connected with the true technical
foundations.

And yes it does lend itself well to creative outputs, but it’s not limited to
that.

Is it _useful_ to have these overlapping but different concepts of engineering
and whispering?

I think so. It feels pretty likely that prompting or chatting with AI agents
is going to be a major way that we interact with computers into the future,
and whereas there’s not a huge spread in the ability between people who are
not super good at tapping on icons on their smartphones and people who are,
when it comes to working with AI it seems like we’ll have a high dynamic
range. Prompting opens the door for non-technical virtuosos in a way that we
haven’t seen with modern computers, outside of maybe Excel.

_(And outside creative software and video games, and I’m sure I’ll think of
more exceptions… the day-to-day and business computing “world” then.)_

Giving this trainable knack a name, however tongue in cheek, makes it a skill
we can work to develop: what would a class in prompt whispering look like?

Divorce yourself from the need to say that an LLM is “just” an autocompleting
stochastic parrot, and allow yourself to riff off the [Waluigi
Effect](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-
mega-post) because although it might not be “correct” to say that an AI model
is a superposition of simulated realities, sculpted down by the prompt, you
can personally get better results to take that perspective.

_Large language models hate this one weird trick._

Anyway.

Best of luck completing the rest of your GenAI textbook, and I’m glad to hear
that you’re considering including prompt whispering in addition to the more
industry-normal prompt engineering.

Please do send me a copy of the chapter when you’re done! I’d be happy to
offer comments on your next draft if that would be useful.

Best

Matt
