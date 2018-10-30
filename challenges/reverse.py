'''
    Module for reversing a stringß
'''
import sys

def reverse(string):
    '''
        Reverses a string
        Assumes string is a string object to be reversed
    '''
    return string[::-1]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Incorrect usage of the program")
        print("Example usage: python3 reverse.py hello")
        print("output: olleh")
    else:
        print(reverse(sys.argv[1]))

