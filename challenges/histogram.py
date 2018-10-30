def process_text(histogram, word):
    '''
        Processes the text into the histogram.
        Assumes histogram is a dictionary, and word is a string
    '''
    
    word = word.lower()

    if word in histogram:
        histogram[word] += 1
    else:
        histogram[word] = 1

def histogram(source_text, is_file=True):
    '''
        Create the histogram based on the source text
        Assumes source_text is either a file name or string containing words depending on
        what is_file is set to.
    '''

    histogram = {}

    if is_file:
        file = open(source_text, 'r')
        for word in file:
            process_text(histogram, word)
    else:
        words = source_text.split()
        for word in words:
            process_text(histogram, word)

    return histogram

def unique_words(histogram):
    '''
        Finds all the unique words inside of a dictionary histogram
        Assumes histogram is a dictionary
    '''
    count = 0
    for key, value in histogram:
        if value == 1:
            count += 1

    return count


def frequency(word, histogram):
    '''
        Find the frequency of a word in a dictionary based histogram
        Assumes word is a string and histogram is a dictionary
    '''
    if word in histogram:
        return histogram[word]
    else:
        return 0


if __name__ == '__main__':
    histogram = histogram('Hi there Hi bye hi hello bye bye bye hello', is_file=False)
    print(histogram)
