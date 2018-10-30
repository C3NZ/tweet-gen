'''
    Module for imitating cowsay
'''
import sys

def create_tux():
    tux =  '''
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
    '''
    return tux

def normalize_str(user_input):
    word_list = user_input.split()
    word_count = len(word_list);
    tux_line = 41
    words_per_line = word_count // tux_line
    normalized_list = ['-'*tux_line]
    current_line  = '< '
    counter = 0

    for i in range(0, word_count):
        counter += 1
        if words_per_line % counter != 0:
            current_line += word_list[i] + " "
        else:
            current_line += ' '*(tux_line - len(current_line) - 1) + ">\n"
            normalized_list.append(current_line)
    normalized_list.append('-'*41)
    return "".join(normalized_list)



def create_message(user_input):
    normalized_message = normalize_str(user_input)
    return normalized_message + create_tux()

if __name__ == '__main__':
    arguments = sys.argv[1:]
    if(len(arguments) == 1):
        print(create_message(arguments[0]))
    else:
        print("incorrect usage ")
