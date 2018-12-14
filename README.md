# Tweet-gen
## A markov chain based application that generates sentences via a corpus
In my instance, I am using a data set derived from r/jokes, a subreddit on reddit in which
people can post jokes on to. I currently utilize two markov chains, one for generating the joke
title or prompt, and then another for generating the punchline. Both markov chains are 4th order
and utilize corpuses of 100k+ words. A deployed version of the bot can be found [here](https://tweetgen-vm.herokuapp.com/)

## Setup
Assuming you have this repository installed on your computer and python 3.7, in the root directory
run:
`pip install -r requirements.txt`
