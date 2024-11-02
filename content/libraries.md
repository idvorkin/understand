# I hope libraries are snapshotting today’s awkwardly sourced AIs

I hope libraries are figuring out how to archive today’s absolutely remarkable
but potentially illicitly created AIs.

Large language models like GPT-3 are trained by hoovering up all the text on
the internet. Image synthesis AIs are a language model plus another AI trained
on all the images that are similarly hoovered up. It’s all pretty
indiscriminate.

FOR EXAMPLE: Andy Baio and Simon Willison built [an interactive explorer for
some of the training images in Stable
Diffusion](https://waxy.org/2022/08/exploring-12-million-of-the-images-used-
to-train-stable-diffusions-image-generator/) (exploring 12 million of the 2.3
billion included) - unsurprisingly there’s a lot of commercial art there. And
that’s why you can say _“in the style of David Hockney”_ or whatever in an
image prompt and it comes back looking like a previously-unknown Hockey print.

ASIDE:

Take a moment to visit Everest Pipkin’s project
[Lacework](https://unthinking.photography/articles/on-lacework) (2020) in
which they viewed, personally, _every single one_ of the one million 3 second
videos in the MIT Moments In Time dataset.\_

Very slowly, over and over, my body learns the rules and edges of the dataset.
I come to understand so much about it; how each source is structured, how the
videos are found, the words that are caught in the algorithmic gathering.

I don’t think anyone, anywhere will have such an understanding of what
constitutes an AI, and given the growth in datasets, I don’t think anyone
_could_ ever again.

"Repetition is devotional," says Pipkin.

It brings tears to my eyes. So good!

Who owns style?

When it comes to code the problem is even more pointed because code often
explicitly has a license attached. GitHub Copilot is an amazing code
autocompletion AI – it’s like pair programming. _(I can see a near-term future
where being a human engineer is more like being an engineering manager today,
and you spend your days briefing and reviewing pull requests from your team of
AI copilot juniors.)_

But it’s trained on GPL code. When code is licensed with GPL, the authors say
that it’s free to use, but any code based on it must also be licensed as GPL.
Viral freedom. Now, if I learn how to code by reading GPL code and then go on
to work on proprietary code, that’s fine. But used as AI training data?

[Legally GitHub Copilot is probably in the
clear](https://fossa.com/blog/analyzing-legal-implications-github-copilot/)
but it’s also probably not what the authors of the open source, GPL code would
have intended.

Simon Willison [talks about vegan
datasets](https://simonwillison.net/2022/Aug/29/stable-diffusion/): "I’m not
qualified to speak to the legality of this. I’m personally more concerned with
the morality." \- It’s a useful distinction.

There’s a lot to figure out. [Have I been
trained?](https://haveibeentrained.com) is a tool to bring some transparency:
as an artist you can search for your own work in the image synthesis training
data. It’s a first of a series of tools from a new organisation called
**Spawning,** also including _Source+:_

… Dryhurst and Herndon are developing a standard they’re calling Source+,
which is designed as a way of allowing artists to and opt into - or out of -
allowing their work being used as training data for AI. (The standard will
cover not just visual artists, but musicians and writers, too.)

Provenance, attribution, consent, and being compensated for one’s labour (and
being able to opt in/out of the market) are all important values. But I can’t
quite visualise the eventual shape of the accommodation. The trained AIs are
just too valuable; the voices of artists, creatives, and coders are just too
diffuse.

v buckingham calls this "copyright laundering," as previously discussed [in
this post about ownership](/home/2022/05/26/filtered), in which I also said:

Maybe there is a market for a future GPT-PD, where PD stands for public
domain, and the AI model is guaranteed to be trained only on public domain and
out-of-copyright works.

And litigiously cautious megacorporations like Apple will use GPT-PD for their
AI needs, such as autocomplete and auto-composing emails and how Siri has
conversations and so on.

The consequence will be that Gen Beta will communicate with the lilt and
cadence of copyright-expired Victorian novels, and anyone older (like us) will
carry textual tells marking us as born in the Pre Attribution Age.

Perhaps:

GPT-3 and the Laion-5b dataset, with their gotta-catch-em-all approaches to
hoovering up training data, will in the future be seen as just a blip.

ALSO we’re poisoning the groundwater.

Attribution or not, GPT-3, DALL-E, Stable Diffusion and the rest were trained
on an internet where synthesised text and images were mostly absent.

DALL-E at least watermarks its output with a rainbow telltale in the bottom
right, so these can be excluded from future sets of training data, but other
synthesisers don’t.

What freaky feedback loops come about when models are being trained on data
swept up monthly, but the data has a high proportion of output from previous
models?

Long story short, today’s AIs are unique, trained as they are on pure,
unethically harvested data.

Given all of the above, they are perhaps the most complete models we’ll _ever_
get? Future datasets will be edited and will be muddied.

And given _that:_ we have an obligation to save them, right? Troubling
provenance or no.

In a funny way I’m reminded of the [immortal cell line of Henrietta
Lacks](/home/2022/04/27/hela) – the moral framework wasn’t in place in 1951 to
see what we see clearly now: that it wasn’t ok to collect and appropriate
Lacks’ cells. But the HeLa cancer cell line has been used in all kinds of
advances over the years, and at the point where the moral framework _was_
established, the choice was made to _keep_ the cell line going. (I’d love to
learn more about the moral philosophy of this one.)

Tricky.

Anyway.

How does a library save a snapshot of the current DALL-E, the current GPT-3,
the current Stable Diffusion? Complete, usable, and frozen.

There’s going to be pressure to _not_ retain these AIs, given the stolen
words, art, and code inside them. If not that then the march of upgrades:
version 1.1, version 2, a database migration, and at a certain point the
mostly proprietary tooling to access the original version of the synthesis
models will be gone too. It won’t seem important.

How can they be kept for future research? And for just, you know, history.

I hope there are librarians and archivists working on this, today. I hope that
folks from the Internet Archive are already in conversation with OpenAI.

And:

What happens when we find, buried in the model weights, data that is as
culturally sensitive as - say - some of the objects appropriated and kept in
the British Museum? What arguments are there to be had about data, in
centuries to come?
