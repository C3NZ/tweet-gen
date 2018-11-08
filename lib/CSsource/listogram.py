#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        listogram_len = len(self)
        if not listogram_len:
            self.types += 1
            self.tokens += count
            self.append((word, count))
        else:
            word_index = self._index(word)

            if word_index is None:
                #The word couldn't be found, update the types and token count  
                self.types += 1
                self.tokens += count
                self.append((word, count))
            else:
                #retrieve the word freq and update the tuple/token count
                word_freq = self[word_index][1]
                self.tokens += count
                self[word_index] = (word, word_freq + count)

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for word_count_list in self:
            current_word = word_count_list[0]
            word_freq = word_count_list[1]

            if word == current_word:
                return word_freq

        return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for word_count_list in self:
            current_word = word_count_list[0]
            if word == current_word:
                return True

        return False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        index = 0

        for word_count_tup in self:
            current_word = word_count_tup[0]

            if target == current_word:
                return index

            index += 1

        return None

def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
