def process_text(histogram, word):
    '''
        Processes a word into a list based histogram
        Assumes that the histogram is a list and word is a string
    '''
    word = word.lower()
    if len(histogram) == 0:
        histogram.append([word, 1])
    else:
        word_found = False
        for item in histogram:
            current_word = item[0]

            if current_word == word:
                item[1] += 1
                word_found = True
                break

        if not word_found:
            histogram.append([word, 1])


def histogram(source_text, is_file=True):
    '''
        Generates a list based histogram.
        Assumes that source_text is a string containing text or a file
    '''
    histogram = []

    if is_file:
        file = open(source_text, 'r')
        for line in file:
            for word in line.split():
                process_text(histogram, word)
    else:
        words = source_text.split()
        for word in words:
            process_text(histogram, word)

    return histogram

def unique_words(histogram):
    '''
        Get the unique words from a list based histogram
        Assumes histogram is a multi-dimensional list
    '''
    return len(histogram)

def frequency(histogram, word):
    '''
       Finds the amount of times a word appears inside of the histogram.
       Assumes that histogram is a list and that word is a string
    '''
    word = word.lower()
    for item in histogram:
        current_word = item[0]
        if word == current_word:
            return item[1]
    return 0
