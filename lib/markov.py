from queue import Queue
from lib.CSsource.dictogram import Dictogram
from lib.utils.file import extract_words, serialize_markov, deserialize_markov
from lib.histograms.sample import weighted_sample, markov_weighted_sample

import random

class Markov(dict):
    def __init__(self, word_queue=None, order=2):
        super(Markov, self).__init__()
        self.types = 0
        self.tokens = 0
        self.empty = True
        self.order = order

        if word_queue is not None:
            self.create_markov(word_queue)

    def save_markov(self, path_to_file):
        '''
            Save the markov chain to a file
            assumes that path_to_file is a string containing the file to save
        '''
        serialize_markov(path_to_file, self)

    @staticmethod
    def load_markov(path_to_file):
        '''
            Load the markov chain from a file
            assumes that path_to_file is a string containing the file to save
        '''
        return deserialize_markov(path_to_file)

    def create_markov(self, word_queue):
        '''
            create the markov chain model/data structure
            assumes word_queue is a queue containing your corpus
        '''
        list_len = word_queue.list_length
        context = word_queue.iterate(self.order + 1)
        context = context[1:]
        counter = self.order + 1
        words_left = True
        
        while words_left:
            if counter < list_len:
                next_type = word_queue.dequeue()
                # Check if the next type is stop so we can get the value that comes after it 
                if next_type == 'STOP':
                    counter += 2
                    if counter < list_len: 
                        word_queue.dequeue()
                        next_type = word_queue.dequeue()
                    else:
                        words_left = False

                counter += 1

                current_type = tuple(context)
                context.pop(0)
                context.append(next_type)
                self.add_token(current_type, next_type)
            else:
                words_left = False

    def add_token(self, current_type, next_type):
        '''
            Add tokens into our markov chain regardless of the order
        ''' 
        if self.empty:
            self.empty = False
            self[current_type] = Dictogram([next_type])
            self.types += 1
        else:
            if current_type in self:
                self[current_type].add_count(next_type)
            else:
                self.types += 1
                self[current_type] = Dictogram([next_type])

        self.tokens += 1

    def generate_sentence(self, sentence_length=100):
        '''
            Generate a sentence given the current state of the markov chain
            Assumes that sentence_length is an integer the length of the sentence
            you want.
            Returns a list of strings
        '''
        output_list = []
        random_type = markov_weighted_sample(self)
        next_words = list(random_type[1:])
        output_list.extend(word for word in random_type)
        counter = self.order

        sentence_ended = False

        while not sentence_ended:
            dictogram = self[random_type]

            next_word = weighted_sample(dictogram)

            if next_word != 'STOP':
                next_words.append(next_word)
                counter += 1
            else:
                random_type = markov_weighted_sample(self)
                next_words = list(random_type[1:])
                output_list.extend(word for word in random_type)
                counter += self.order
                continue
            print(random_type)
            print(dictogram)
            print(next_word)
            output_list.append(next_word)

            if next_word[-1] in '.?':
                if counter >= sentence_length:
                    sentence_ended = True

            random_type = tuple(next_words)

            next_words = next_words[1:]

        return output_list

def main():
    word_queue = Queue()
    extract_words('corpus/corpus.txt', word_queue)
    markov = Markov(word_queue)
    sentence = markov.generate_sentence()
    print(" ".join(sentence))
    print(markov.tokens)
    print(markov.types)

if __name__ == '__main__':
    main()
