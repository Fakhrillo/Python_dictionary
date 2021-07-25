import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        closer = input("Did you mean %s instead? Write Y if yes, else N: " % get_close_matches(word, data.keys())[0])
        if closer == "Y" or closer == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif closer =="N" or closer == "n":
            return "The word does not exist. Please double check it."
        else: 
            return "-_- WE didn't understand your query."
    else:
        return "The word does not exist. Please double check it."

while True:
    word = input("Enter a word: ")
    if word == "q":
        break
    output = definition(word)

    k = 0
    if type(output) == list:
        for item in output:
            k += 1
            print("\n" + f"{k}. " + item)
        
        print("\n To quite please enter 'q' ")
    else: 
        print(output)
        