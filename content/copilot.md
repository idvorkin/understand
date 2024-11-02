# AI-generated code helps me learn and makes experimenting faster

It’s one thing to keep tabs on generative AI, [speculating about it
here](/home/tagged/gpt-3) and in private client work – it’s another to
experience the whoa moment for myself.

_Code._ I can take or leave AI art. [ChatGPT](https://chat.openai.com) mostly
leaves me cold. But code!

[GitHub Copilot](https://github.com/features/copilot) is "your AI pair
programmer" – it’s smart, code-aware autocomplete. Ok I get that. But let me
try to explain what I experienced earlier this week…

I’m building a basic in-browser prototype so I can explore the UX around
computing vision, gestures, and attention, just a lightweight personal
investigation [on the topics from yesterday](/home/2023/01/26/room).

The tech isn’t rocket science, but it isn’t something I know already. From
experience this means that I probably need a day or so to learn enough to ask
the right questions of StackOverflow and Google. Absorbing a domain like this
means reading tutorials, specs, examples, etc. I can bully my way through most
code given time.

I signed up for the Copilot 60 day free trial because why not. Installed the
plug-in etc.

I opened my vanilla React project. I made an empty component that displayed
“Hello, World!” in my browser preview, just to check everything was working.

Then I wrote a comment at the top of the file:

// A react component that activates the user’s webcam and displays the stream
in a video element

And waited for the autocomplete: a bunch of code. And accepted it. And hit
save. Less than half a second.

The browser preview refreshed – asked for webcam access – then I saw my own
face staring back at me.

I got that feeling of the floor dropping away.

Look, I _know_ the code isn’t rocket science. I know I could do this,
eventually, and you could probably smash this out without looking, but I don’t
really know React - I can’t write it idiomatically - and I don’t know about
webcams in the browser, and I don’t know about the MediaStream API.

So this was a day of work in 10 minutes.

What is meant was that I could spend that day integrating hand pose detection
and noodling with the actual micro-interactions. And now I have opinions about
all of that!

Now, none of that Copilot-supplied code remains in my app.

What happened what that it helped me frame my problem. I was able to rapidly
explore the edges of my knowledge, and figure out how to structure my
questions and what I need to learn. My learning requirement is not obviated
obviously…

…but as an epistemic journey my interaction with Copilot is insanely more
efficient than doing it on my own.

So, [after Tom Stafford](/home/2022/05/24/epistemic), Copilot is an epistemic
agent: it’s not query/response, which is a model which presupposes that I do
not change; it scouts ahead and helps me build knowledge. I have a better
mental model of my domain, _I know more,_ than I did before I started.

btw when I refreshed the browser and saw my face there, the code working as-
wished but not necessarily as-expected, my laptop felt _haunted._ I closed the
lid to stop the face looking at me.

Then I opened it again to check the screen. Then took a breather. Then came
back to write this.

Github Copilot radically lowers the cost of experimenting. That’s the value to
me.

_On ChatGPT for a sec because I dunked on it at the top:_

Generated text is meh. It all reads like vapid SEO traffic-farming blog
content. Automating away people’s jobs is… ugh, fine I guess? but let’s try to
be more original. Stochastic text collisions can stimulate new ideas, sure,
that’s another use… but if that’s your goal then flip a coin or use Oblique
Strategies or the I Ching or something. [Prompt injection
attacks](https://simonwillison.net/2022/Sep/12/prompt-injection/) are funny
and the engineering to avoid them will probably open up more interesting
possibilities than the reverse. But not yet.

Ok but I still love large language models so why? I’ve been asking myself
that. So here are five large language model applications that I find
intriguing:

Between those starting points (which I should unpack I know), and spotting
second-order effects where cheaper UX experiments is one such example, that’s
where I’m spending my cycles rn.
