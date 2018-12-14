'''
    Web Application for hosting our histogram and the main entry point into our app
'''

import os

from flask import Flask, render_template, jsonify

from lib.histograms.distogram import histogram
from lib.histograms import sample
from lib.markov import Markov

from parse_jokes import get_word_queues

app = Flask(__name__, template_folder='templates')

# All code for generating a markov chain.
# Will keep commented for now unless I have to create a new markov for loading
def create_markovs():
    app.word_queues = get_word_queues(15000)
    app.joke_markov = Markov(app.word_queues[0], order=4)
    app.punchline_markov = Markov(app.word_queues[1], order=4)
    app.joke_markov.save_markov('res/joke_markov')
    app.punchline_markov.save_markov('res/punchline_markov')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/joke')
def tell_joke():
    joke = app.joke_markov.generate_sentence(sentence_length=20)
    punchline = app.punchline_markov.generate_sentence(sentence_length=30)
    joke = "Okay... " + " ".join(joke)
    punchline = " ".join(punchline)
    return jsonify(joke=joke, punchline=punchline)


if __name__ == '__main__':
    create_markovs()
else:
    # Load markov from a file to save load up time
    app.joke_markov = Markov.load_markov('res/joke_markov')
    app.punchline_markov = Markov.load_markov('res/punchline_markov')


