import json
import pickle
import re

def extract_words(path_to_file, word_queue):
    '''
        extract words from a file and then return it as a list of strings
        Assumes path to file is a string containing the path to the file
        trying to be opened
    '''
    with open(path_to_file) as current_file:
 
        for line in current_file.readlines():
            for item in line.split():
                word_queue.enqueue(item)

                if word_queue.list_length >= 7000000:
                    break

def clean_words(path_to_file, output_file):
    '''
        Clean words from one file using regex and write those changes to the next
    '''
    output_str = []
    with open(path_to_file, 'r') as current_file:
        for line in current_file.readlines():
            output_str.extend(line.split())

    new_str = ''
    for word in output_str:
        word = re.sub('[^A-Za-z0-9]+', '', word)
        word = re.sub(' +', ' ', word)
        word = re.sub('\d{0,5}', '', word)
        new_str += ' ' + word

    with open(output_file, 'w+') as current_file:
        current_file.write(new_str)

    return new_str

def serialize_markov(path_to_file, markov):
    '''
        Serialize the markov to be written to file in a format we can later retrieve
        assumes that path_to_file is a string that contains the path to the output file
        and that markov is the Markov object to be serialized
    '''
    with open(path_to_file, 'wb') as current_file:
        pickle.dump(markov, current_file)

def deserialize_markov(path_to_file, markov):
    '''
        Deserialize the markov object that is stored in a file
        Assumes that path_to_file is a string that contains the path to the output file
        returns the markov object
    '''
    with open(path_to_file, 'rb') as current_file:
        return pickle.load(current_file)

class Test:
    def __init__(self, hi=45):
        self.hi = 45

if __name__ == '__main__':
    test = Test()
    lel = {}
    lel[('hi', 'hello')] = test
    lel[('hi,', 'helloo')] = 4
    serialize_markov('x.txt', lel);
    lel = deserialize_markov('x.txt', {})
    # y = extract_words('corpus/corpus.txt')
    x = clean_words('corpus/corpus.txt', 'clean.txt') 
