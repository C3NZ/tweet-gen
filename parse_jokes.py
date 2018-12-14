from lib.utils.file import extract_json
from lib.queue import Queue

def extract_jokes(joke_list):
    '''
        Extract both the joke titles and punchlines from the json data.
        Assumes joke_list is a list containing json objects
    '''
    title_list = []
    punchline_list = []
    for joke in joke_list:
        title_list.append(joke['title'])
        punchline_list.append(joke['body'])
    return (title_list, punchline_list)

def generate_sentence_lists():
    '''
        Generate both sentence lists from reddit_jokes.json
        returns a list of words setup with start and stop tokens to indicate the start
        and stop of a joke
    '''
    joke_list = extract_json('reddit_jokes.json')
    return extract_jokes(joke_list)

def clean_word(word):
    '''
        Small utility function to clean up the word of any special characters and spaces
    '''
    return ''.join(char for char in word if char.isalnum() or char in '?.,')

def generate_word_lists(sentence_list):
    word_list = []
    for sentence in sentence_list:
        word_list.append('START')
        for word in sentence.split():
            word = clean_word(word)
            if len(word) > 0:
                word_list.append(word)
        word_list.append('STOP')

    return word_list

def trim_list_to(index, word_list):
    '''
        There are 194,553 jokes in our joke list. For every joke, we add a start and stop token
        before and after every joke. This in a way keeps an index of jokes, and doing so allows
        us to strip x amount of jokes from the final corpus where x is the number of jokes we're
        going to be removing

        Assumes index is an integer being the index we want to grab up to and word_list is a 
        word list configured byour generate_word_lists function

        Returns a trimmed version of the word list where all the jokes match their punchlines
    '''
    counter = 0
    new_word_list = []
    for word in word_list:
        if word == 'STOP':
            counter += 1

        if counter < index:
            new_word_list.append(word)
        else:
            new_word_list.append('STOP')
            break

    return new_word_list

def get_word_lists(index=0):
    '''
        get the word lists from the our reddit_jokes json file.
        Assumes index is an integer to specify how many jokes we'd like to grab
    '''
    title_list, punchline_list = generate_sentence_lists()
    title_list = generate_word_lists(title_list)
    punchline_list = generate_word_lists(punchline_list)
    if index != 0:
        title_list = trim_list_to(index, title_list)
        punchline_list = trim_list_to(index, punchline_list)

    return (title_list, punchline_list)

def convert_to_queue(word_list):
    '''
        Helper function to convert a word_list into a queue 
    ''' 
    queue = Queue()

    for word in word_list:
        queue.enqueue(word)

    return queue


def get_word_queues(index=0):
    '''
        Get the word queues to use with our markov chain
    '''
    title_list, punchline_list = get_word_lists(index)
    title_list = convert_to_queue(title_list)
    punchline_list = convert_to_queue(punchline_list)

    return (title_list, punchline_list)
def main():
    joke_list = extract_json('reddit_jokes.json') 
    
    # Prove that jokes that have been extracted into two new word lists 
    title_list, punchline_list = get_word_lists(1)
    print(len(title_list))
    print(len(punchline_list))
    print(title_list)
    print(punchline_list)
    title_queue, punchline_queue = get_word_queues(1)
    print(title_queue)
    print(punchline_queue)

if __name__ == '__main__':
    main()
