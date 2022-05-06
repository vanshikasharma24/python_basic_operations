# Python program to find smallest number in a list
mylist=[30,3,5,10,20,24]
min=mylist[1]
for item in mylist:
    if min > item:
        min = item
print(min)
# Python program to find largest number in a list
mylist=[30,3,5,10,20,24,12]
max=mylist[1]
for item in mylist:
    if max < item:
        max = item
print(max)

