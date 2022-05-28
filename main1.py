# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from os import read


from cgitb import text
from typing import Text


def read_file_content(story):
    text=open("story.txt")
    print(text.read())
    text.close()
read_file_content("story.txt")


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    occurence = dict()
    for word in words:
        if word in occurence
            if not word.isnumeric()
                occurence{word} += 1
        else:
            if not word.isnumeric():
                occurence{word} = 1
    return occurence

print(count_words())

    return {"as": 10, "would": 20}

