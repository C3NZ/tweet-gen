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
    while len(args) > 0:
        print(args.pop(random.randint(0, len(args) - 1)), end=" ")
    print()

if __name__ == '__main__':
    '''
        Checks to see if module was run directly
    '''
    arguments = sys.argv[1:]
    randomize_args(arguments)
