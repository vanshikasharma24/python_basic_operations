# Python program to accept the strings
# which contains all the vowels
vowel=set('aeiou')
s=set()
struser=input("user input")
for char in struser:
    if char in vowel:
        s.add(char)
    else:
        pass
if len(s)==len(struser):
    print("accepted")
else:
    print("not accepted")
