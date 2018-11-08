def process_text(histogram, word):
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

def histogram(source_text, is_file=True):
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
                process_text(histogram, word)
    else:
        words = source_text.split()
        for word in words:
            process_text(histogram, word)
    return histogram

def unique_words(histogram):
    '''
        Returns all words used int the piece of the text
    '''
    return len(histogram)

def frequency(histogram, word):
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
