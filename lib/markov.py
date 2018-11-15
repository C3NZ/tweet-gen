from CSsource.dictogram import Dictogram
from utils.file import extract_words
from histograms.sample import weighted_sample, markov_weighted_sample

class Markov(dict):
    def __init__(self, word_list=[]):
        super(Markov, self).__init__();
        self.types = 0
        self.tokens = 0
        self.empty = True
        if len(word_list):
            self.create_markov(word_list)

    def create_markov(self, word_list):
        list_len = len(word_list)
        for i in range(0, list_len):
            if i + 1 < list_len:
                current_type = word_list[i]
                next_type = word_list[i + 1]
                self.add_word(current_type, next_type)


    def add_word(self, current_type, next_type):
        if self.empty:
            self.empty = False
            self.types += 2
            self.tokens += 2
            self[current_type] = Dictogram([next_type])
        else:
            self.tokens += 1
            if current_type in self:
                self[current_type].add_count(next_type)
            else:
                self.types += 1
                self[current_type] = Dictogram([next_type])
        print(self)

    def generate_sentence(self, sentence_length=10):
        output_list = []
        word = markov_weighted_sample(self)
        output_list.append(word)
        print(self[word])
        for i in range(0, sentence_length - 1):
            word = weighted_sample(self[word])
            output_list.append(word)

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
    print("".join(sentence))

if __name__ == '__main__':
    main()
