def process_text(histogram, word):
    '''
        Process text into a histogram
        Assumes histogram is a count based histogram and word a string that is trying to be
        inserted into the histogram
    '''
    word = word.lower()

    if len(histogram) == 0:
        histogram.append((1, [word]))
    else:
        count = 0
        word_found = False

        for tup in histogram:
            frequency = tup[0]
            selected_words = tup[1]

            if word_found and count == frequency:
                selected_words.append(word)
                return
            else:
                if word in selected_words:
                    count = frequency + 1
                    word_found = True
                    selected_words.remove(word)

        if not word_found:
            histogram[0][1].append(word)
        else:
            histogram.append((count, [word]))

def remove_empties(histogram):
    '''
        Remove empty count tuples from a histogram
        Assumes that histogram is a count based histogram
    '''
    for i in range(0, len(histogram) - 1):
        current_item = histogram[i]

        if not len(current_item[1]):
            histogram.pop(i)

def histogram(source_text, is_file=True):
    '''
        Create a count based histogram, where items are stored into tuples based on count
        Assumes that source_text is a string containing a file path or story based upon
        the is_file flag
    '''
    histogram = []

    if is_file:
        file = open(source_text, 'r')
        lines = file.readlines()
        for line in lines.split():
            for word in line:
                process_text(histogram, word)
    else:
        words = source_text.split()
        for word in words:
            process_text(histogram, word)

    remove_empties(histogram)
    return histogram

def unique_words(histogram):
    '''
        Get the all unique words that are in the body of text (words that have been seen one or more times)
        Assumes that histogram is a count based histogram
    '''
    unique_count = 0

    for item in histogram:
        unique_count += len(item[1])

    return unique_count

def frequency(histogram, word):
    '''
        Get the frequency of a specific word inside the histogram
        Assumes that histogram is a count based histogram and that word is a string
    '''
    frequency = 0
    word = word.lower()

    for item in histogram:
        word_list = item[1]
        for current_word in word_list:
            if word == current_word:
                frequency = item[0]
                return frequency

    return frequency

