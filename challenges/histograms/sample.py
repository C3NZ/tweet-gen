'''
Module for Stochastic sampling
'''
import random

import distogram

def random_sample(histogram):
    '''
        Randomly select a word from a histogram regardless of it's frequency in the histogram
        Assumes that histogram is a dictionary based histogram
    '''
    histogram_words = list(histogram)
    histogram_length = len(histogram_words)
    random_index = random.randint(0, histogram_length - 1)
    return histogram_words[random_index]

if __name__ == '__main__':
    histogram = distogram.histogram('Hi there hello there what is up there hands in the air i dont care', is_file=False)
    print(random_sample(histogram))

