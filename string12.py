# Python program to count number of vowels using sets in given string

vowel=set("aeiouAEIOU")
count=0
struser=input("input your string")
for i in struser:
    if i in vowel:
        count = count + 1
print(count)

