from CSsource.dictogram import Dictogram
from queue import Queue
from utils.file import extract_words
from histograms.sample import weighted_sample, markov_weighted_sample
import random

class Markov(dict):
    def __init__(self, word_list=[], order=1):
        super(Markov, self).__init__();
        self.types = 0
        self.tokens = 0
        self.empty = True
        self.queue = Queue()
        self.order = order
        if len(word_list):
            self.create_markov(word_list)

    def create_markov(self, word_list):
        '''
            create the markov chain model/data structure
            assumes word_list is a list of words
        '''
        list_len = len(word_list)

        for i in range(0, list_len):
            if i + 1 + self.order < list_len or i + 1 + self.order == list_len:
                current_type = tuple(word for word in word_list[i: i + self.order])
                next_type = tuple(word for word in word_list[i + 1: i + 1 + self.order])
                self.queue.enqueue_multiple([current_type, next_type])
                self.add_token(current_type, next_type)

    def add_token(self, current_type, next_type):
        '''
            Add tokens into our markov chain 
        ''' 
        if self.empty:
            self.empty = False
            self[current_type] = Dictogram([next_type])
            self.tokens += 1
            self.types += 1
        else:
            if current_type in self:
                self[current_type].add_count(next_type)
            else:
                self.types += 1
                self[current_type] = Dictogram([next_type])

            self.tokens += 1

    def generate_sentence(self, sentence_length=10):
        output_list = []
        random_type = markov_weighted_sample(self)
        output_list.append(" ".join(random_type))
        for i in range(0, sentence_length - 1):
            dictogram = self[random_type]
            random_type = weighted_sample(dictogram)

            if random_type not in self:
                random_type = markov_weighted_sample(self)
            output_list.append(random_type[self.order - 1])

        return output_list

    def get_tokens(self):
        return self.tokens

    def get_types(self):
        return self.types



def main():
    word_list = ['hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'bye', 'hello', 'there', 'is', 'tokens', 'and', 'words']
    print(word_list)
    markov = Markov(word_list)
    sentence = markov.generate_sentence()
    print(" ".join(sentence))
    for key, value in markov.items():
        print(key)
        print(value)
    print(markov.tokens)
    print(markov.types)

if __name__ == '__main__':
    main()
