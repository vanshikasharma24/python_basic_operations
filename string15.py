# Find words which are greater than given length k
userlen=int(input("input an integer length"))
string=[]
userstr=input("input a string")
splited_words=userstr.split(" ")
for words in splited_words:
    if len(words)>userlen:
        string.append(words)
print(string)



