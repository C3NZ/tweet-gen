from lib.utils.file import extract_json

def extract_jokes(joke_list):
    title_list = []
    joke_list = []
    for joke in joke_list:
        title_list.append(joke['title'])
        punchline_list.append(joke['body'])

def main():
    joke_list = extract_json()
    title_list, punchline_list = extract_jokes()

if __name__ == '__main__':
    main()
