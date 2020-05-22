import json
import difflib

data = json.load(open('data.json'))

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(difflib.get_close_matches(word, data.keys())) > 0:
        yn = input('Did you mean \'%s\' instead? Enter Y if yes, or N if no: ' % difflib.get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[difflib.get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return 'The word doesn\'t exist. Please double check.'
        else:
            return 'We didn\'t understand your entry.'
    else:
        return 'The word doesn\'t exists. Please double check.'

word = input('Enter word: ')

output = define(word)

if type(output) == list:
    for item in output:
        print('-', item)
else:
    print(output)
