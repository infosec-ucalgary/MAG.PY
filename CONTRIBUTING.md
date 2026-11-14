# Contributing to MAG.PY

## READ THIS READ THIS READ THIS READ THIS
This document is meant to answer the who, what, where, why, and how of making contributions to MAG.PY.
- `WHO can contribute?` Anyone! This is a public repository, and is organized like an open-source project
- `WHAT should we contribute?` Refactors and restructures of common Discord bot applications, written with a focus on privacy and security
- `WHERE do I ask questions?` You should DM **CYBERSEC** executives[^1], professors, or just ask programmers in general if you're lost
- `WHY should I contribute?` You get to make meaningful contributions to a real application, and this familiarizes you with the software development workflow
- `HOW can I contribute?` That's the purpose of this document. We need to go over the following:
  - Knowledge check
  - Baby steps

## Lost?
When in doubt, ask[^1] a **CYBERSEC** executive! If you're a club member or just a random person on the internet *outside our internal executive team*, you can easily reach the execs on our official, public Discord server.

# Knowledge check

***YOU DO NOT NEED TO ACTUALLY KNOW ANYTHING!*** You just have to be willing to ask questions.[^1] Otherwise, we assume that at a minimum, potential contributors are enrolled in a programming course of some sort, or have spent some time personally invested in programming. Check your knowledge below:

1. Do I know how to use Git?
   - Do I know how to clone a repo?
   - Do I know how to update? Pull? Commit? Push?
   - Do I know how to checkout a branch?
   - Do I know how to create a pull request?
2. Can I apply object-oriented programming principals to Python programming?
   - Do I know what an object/class is?
   - Do I know what `__init__` is?
   - Do I know what `super()` is?
   - Do I know what a library/package is?
   - What is `pip install`?
   - What is a decorator?
   - What is `async` and `await`?
3. Do I know what "*privacy-focused*" means?
   - What is personally-identifiable information (PII)?
   - What are good privacy design principals? Do I know what psychological acceptability is?
   - What user data storage policies exist?
   - Do I know *the law*?

Again if you have any questions, **ASK[^1] A CYBERSEC EXEC**.

# Getting started

If you passed everything in that knowledge check and don't need a CYBERSEC exec (that you should ask[^1] if you're ever lost!) then here's your instructions:
1. Stop reading this and get started
   - If you know OOP and how to make a PR, then what are you waiting for? CYBERSEC execs will review your pull requests.

# Getting started but *I'd like more instructions please*

1. Clone `master` or fork the repository
2. Checkout your own development branch (or fork)
3. Make changes locally (and test them)
4. Push to your development branch (or fork)
5. Create a pull request (PR)
6. Request a review if no one gets to you within a week

## I vaguely remember learning about Git; how does it differ here?
The difference is that you *probably* learned to use Git for the sake of a solo (or duo) project in a *private* repository, where each contributor has equal authority. Here, **CYBERSEC** owns this *public* repository, so the onus is on us that any code that is shipped is vetted and reviewed. The contribution process is as follows:

1. Contributors make their own development branch/fork
2. They work on that branch/fork and get their thing to work as intended
3. Then, they push their changes to their branch/fork
4. Last, they create a pull request to merge their changes into `master`, and request review from the project leads

The `master` branch is protected, because it is "live" code. We can't have anyone randomly pushing stuff there for fun. Instead, you should clone the repository, make (and test!) your contributions locally, then make *pull requests* (PR), which is like submitting your assignment for review; except it's an actual contribution to something real.

## I *"know"* how to code in Python, but I'm still confused!
That's because the intro to computer science courses (CPSC231/CPSC217) only go over Python basics; enough to actually get you 90% of the way to becoming a proper developer, but there are still some things that you take for granted. If you are still a first-year or second-year at the University of Calgary, then chances are:
- You have never seen `@` decorators
- You have never seen `async`
- You haven't worked with many libraries outside of basic ones like `numpy`
- You haven't worked on a **real**[^2] group project

If you want a run-down that isn't overly verbose, ask[^1] a **CYBERSEC** exec.

[^1]: I can't stress this enough: just ask a **CYBERSEC** executive if you're lost. Tech VPs and presidents are all regularly available. You have no excuse.

[^2]: Being forced to make a meaningless game in a University course is different from actually making something cool with others. You're probably used to your own coding style and formatting, or making things from scratch so you know where everything is and what everything does, so it can be daunting picking up where someone else left off. That's why you should just ask a **CYBERSEC** exec for help!