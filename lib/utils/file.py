def extract_words(path_to_file):
    '''
        extract words from a file and then return it as a list of strings
        Assumes path to file is a string containing the path to the file
        trying to be opened
    '''
    output_list = []
    with open(path_to_file) as current_file:
        lines = current_file.readlines()
        for line in lines:
            for word in line.split():
                output_list.append(word)

    return output_list
