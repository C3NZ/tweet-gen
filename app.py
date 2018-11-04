from flask import Flask

from .challenges.histograms import distogram

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'
