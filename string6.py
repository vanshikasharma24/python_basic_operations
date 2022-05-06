# Python program to print even length words in a string
user_input = input("input a string of words")
splitted_input = user_input.split()
for words in splitted_input:
    if len(words)%2==0:
        print(words)
    else:
        pass
