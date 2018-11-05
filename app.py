from flask import Flask

from .challenges.histograms.distogram import histogram
from .challenges.histograms import sample

app = Flask(__name__)

def create_histogram():
    return histogram('moby.txt')

distogram = create_histogram()

def generate_text(histogram, word_count=10):
    output_list = sample.weighted_sample(histogram, word_count)
    return " ".join(output_list)

@app.route('/')
def hello_world():
    return generate_text(distogram)


