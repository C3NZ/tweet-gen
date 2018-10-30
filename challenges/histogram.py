'''
    Module for creating and analyzing bodies of text with histograms
'''

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
        Finds all the unique words inside of a dictionary histogram
        Assumes histogram is a dictionary
    '''
    return histogram.keys()


def frequency(histogram, word):
    '''
        Find the frequency of a word in a dictionary based histogram
        Assumes word is a string and histogram is a dictionary
    '''
    word = word.lower()
    if word in histogram:
        return histogram[word]
    else:
        return 0

def process_text_list(histogram, word):
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


def histogram_list(source_text, is_file=True):
    '''
        Generates a list based histogram.
        Assumes that source_text is a string containing text or a file
    '''
    histogram = []

    if is_file:
        file = open(source_text, 'r')
        for line in file:
            for word in line.split():
                process_text_list(histogram, word)
    else:
        words = source_text.split()
        for word in words:
            process_text_list(histogram, word)

    return histogram

def unique_words_list(histogram):
    '''
        Get the unique words from a list based histogram
        Assumes histogram is a multi-dimensional list
    '''
    return len(histogram)

def frequency_list(histogram, word):
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

def process_text_tup(histogram, word):
    '''
        Processes text into a tuple based histogram
        Assumes histrogram is a list and that word is a string
    '''
    if len(histogram) == 0:
        histogram.append((word, 1))
    else:
        word_found = False
        for i in range(0, len(histogram)):
            current_item = histogram[i]
            current_word = current_item[0]

            if word == current_word:
                histogram[i] = (word, current_item[1] + 1)
                word_found = True
                break
        if not word_found:
            histogram.append((word, 1))

def histogram_tup(source_text, is_file=True):
    '''
        Create a tuple based histogram
        Assumes that source_text is a string containing text or a file name based on the
        is_file flag being true or false
    '''
    histogram = []

    if is_file:
        file = open(source_text, 'r')
        for line in file:
            words = line.split()
            for word in words:
                process_text_tup(histogram, word)
    else:
        words = source_text.split()
        for word in words:
            process_text_tup(histogram, word)

def unique_words_tup(histogram):
    '''
        Returns all words used int the piece of the text
    '''
    return len(histogram)

def frequency_tup(histogram, word):
    '''
        Finds the frequency of a word in a piece of text
        Assumes histogram is a list of tuples and that word is a string
    '''
    word = word.lower()
    for item in histogram:
        current_word = item[0]
        if current_word == word:
            return item[1]
    return 0

if __name__ == '__main__':
    histogram = histogram('Hi there Hi bye hi hello bye bye bye hello', is_file=False)
    print(histogram)
    print(unique_words(histogram))
    print(frequency(histogram, 'HI'))

    histogram_list = histogram_list("hi there hi bye hi hello bye bye bye hello", is_file=False)
    print(histogram_list)
    print(unique_words_list(histogram_list))
    print(frequency_list(histogram_list, 'HI'))

    histogram_tup = histogram_tup("hi there hi bye hi hello bye bye bye hello", is_file=False)
    print(histogram_tup)
    print(unique_words_tup(histogram_tup))
    print(frequency_tup(histogram_tup, 'HI'))
