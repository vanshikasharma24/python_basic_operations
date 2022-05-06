# Count the Number of matching characters in a pair of string
str1=input("enter sting 1")
str2=input("enter sting 2")
str1_set=set(str1)
str2_set=set(str2)
matched_char=str1_set & str2_set
print(matched_char)
print("no of matched char",len(matched_char))