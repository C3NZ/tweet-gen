from CSsource.dictogram import Dictogram
from utils.file import extract_words
from histograms.sample import weighted_sample

class Markov(dict):
    def __init__(self):
        super(dict, self).__init__();
        self.dictogram = Dictogram()

    def add_word(self, current_type, next_type):
        self.dictogram.add_count(current_type)
        self.dictogram.add_count(next_type)

        if current_type in self:
            self[current_type].add_count(next_type)
        else:
            self[current_type] = Dictogram([next_type])

    def generate_sentence(self, sentence_length=10):
        output_list = []
        word = weighted_sample(self.dictogram)
        output_list.append(first_word)

        for i in range(0, sentence_length - 1):
            word = weighted_sample(self[word])
            output_list.append(word)

        return output_list

    def get_tokens(self):
        return self.dictogram.tokens

    def get_types(self):
        return self.dictogram.types



def main():
    word_list = ['hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'bye', 'hello', 'there', 'is', 'tokens', 'and', 'words']
    list_len = len(word_list)
    markov = Markov()

    for i in range(0, list_len):
        if i + 1 < list_len:
            current_type = word_list[i]
            next_type = word_list[i + 1]
            markov.add_word(current_type, next_type)

    sentence = markov.generate_sentence()
    print("".join(sentencejjh))

if __name__ == '__main__':
    main()
