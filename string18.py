# Python | Find all close matches of input string from a list
from  difflib import get_close_matches
def match(pattern,word):
    print(get_close_matches(word,pattern))
word="appeal"
pattern=['ape', 'apple', 'peach', 'puppy']
match(pattern,word)