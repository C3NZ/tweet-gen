'''
    Returning random dictionary words specified as an argument passed to the python script
'''

import random
import sys

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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Incorrect usage of the script')
        print('Example usage: python dictionary_words.py 10')
        sys.exit()
    else:
        word_list = load_words('/usr/share/dict/words')
        count = int(sys.argv[1])
        selected_words = randomly_select(count, word_list)

        for word in selected_words:
            print(word, end=' ')

        print()
