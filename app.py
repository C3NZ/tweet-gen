'''
    Web Application for hosting our histogram and the main entry point into our app
'''

import os

from flask import Flask, render_template

from lib.histograms.distogram import histogram
from lib.histograms import sample

app = Flask(__name__, template_folder='templates')

def create_histogram():
    '''
    Create the histogram
    '''
    return histogram('moby.txt')

# distogram = create_histogram()

def generate_text(histogram, word_count=10):
    '''
        Generate text to be sent to the user
    '''
    output_list = sample.weighted_sample(histogram, word_count)
    return " ".join(output_list)

@app.route('/')
def hello_world():
    return render_template('index.html', data='hi')

if __name__ == '__main__':
    port = os.getenv('PORT', 5000)
    app.run(port=port)
