# reversing words of a string

def reverse_string(a):
    words =  a.split(' ')
    reverse_sentence=' '.join(reversed(words))
    return reverse_sentence
string="all is well"
print(reverse_string(string))