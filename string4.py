# Demonstrating Naive method to remove i’th char from string.
def removing(a):
    print("original string is"+" "+a)
    n=len(a)
    for i in a:
        if i==a[1]:
            continue
        print(i,end=" ")

string="mystring"
removing(string)
#length of a string
str="uuehkekfkfjlrklfvlkf"
lenstr=len(str)
print(lenstr)