'''
    Returning random dictionary words specified as an argument passed to the python script
'''

import random
import sys
import timeit
import linecache

def load_words(word_file):
    '''
        Load words from a file
        Assumes word_list is a string that is the path to the file trying to be loaded
    '''
    file = open(word_file, 'r')
    word_list = []

    for line in file:
        word_list.append(line)

    return word_list

def randomly_select(count, word_list):
    '''
        Randomly select words from a word list
        Assumes count is a integer being the count of how many words to select
        Assumes word_list is an array of words
    '''
    list_length = len(word_list)
    random_words = []

    for i in range(0, count):
        selected_word = word_list[random.randint(0, len(word_list) - 1)]
        random_words.append(selected_word.rstrip('\n'))

    return random_words

def fast_select(count):
    '''
        Uses fast load to pull lines out of the file
        Assumes count is an integer for how many words to select
    '''
    total_words = 235886
    selected_words = []

    for i in range(0, count):
        random_line = random.randint(0, total_words - 1)
        selected_word = linecache.getline("/usr/share/dict/words", random_line).rstrip('\n')
        selected_words.append(selected_word)

    return selected_words

if __name__ == '__main__':
    '''
        Handle running the module directly
    '''
    if len(sys.argv) != 2:
        print('Incorrect usage of the script')
        print('Example usage: python dictionary_words.py 10')
        sys.exit()
    else:
        if sys.argv[1] == 'test':
            '''
                Users can benchmark both functions for getting words
            '''
            #Slow test
            print('Getting 10 random words the slow way:')
            setup = 'from dictionary_words import load_words, randomly_select;'
            print('It took:', end=' ')
            print(timeit.timeit(stmt='randomly_select(10, load_words("/usr/share/dict/words"))', setup=setup, number=100), end=" ")

            print('Getting 10 random words the fast way:')
            setup = 'from dictionary_words import fast_select'
            print('It took:', end=' ')
            print(timeit.timeit(stmt='fast_select(10)', setup=setup, number=100), end=" ")
            print('seconds')
        else:
            count = int(sys.argv[1])
            selected_words = fast_select(count)

            for word in selected_words:
                print(word, end=' ')

            print()
