'''
    Module for rearranging the arguments passed into this module or function

    randomize_args - Randomizes the output of the args passed into it
'''
import sys
import random

def randomize_args(args):
    '''
        Takes the arguments and randomly selects which one to print
        Assumes args is a list with n items.
    '''
    new_list = []
    original_length = len(args)

    for _ in range(0, original_length):
        random_num = random.randint(0, len(args) - 1)
        new_list.append(args.pop(random_num))

    return new_list

if __name__ == '__main__':
    '''
        Checks to see if module was run directly
    '''
    arguments = sys.argv[1:]
    print(" ".join(randomize_args(arguments)))
