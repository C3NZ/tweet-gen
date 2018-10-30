'''
    An interactive game of madlibz 
'''
import requests

def parse_madlib(madlib):
    '''
        Returns the blanks and values as values in a tuple
    '''
    return (madlib['blanks'], madlib['value'])

def get_madlib():
    '''
        Retrieve a random madlib, parse it from JSON, and then return it to the user.
    '''
    request = requests.get('http://madlibz.herokuapp.com/api/random')
    return parse_madlib(request.json())

def get_input(prompt):
    '''
        Get user input based on the prompt
    '''
    return input("Enter in a(n) " + prompt + ":")

def generate_madlib(prompts, values):
    '''
        Generate madlib for the user 
    '''
    madlib = ''
    for i in range(0, len(prompts)):
        current_sentence = values[i]
        user_input = get_input(prompts[i])
        madlib += current_sentence + user_input

    return madlib

if __name__ == '__main__':
    '''
        Playing some madlibs!
    '''
    prompts, values = get_madlib()
    play_game = str(input("Are you ready to play some madlibs? (y/n)"))

    if play_game == 'yes' or play_game == 'y':
        print(generate_madlib(prompts, values))
    else:
        print('See you later!')

