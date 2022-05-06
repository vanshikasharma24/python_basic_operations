# Python program to find second largest number in a list
mylist=[30,3,5,10,20,24,12]
#by sorting
mylist.sort()
print(mylist)
print(mylist[1])
# Python program to print even numbers in a list
#even
mylist2=[30,3,5,10,20,24,12,39]
count=0
for item in mylist2:
    if item%2==0:
        print(item,end=" ")
        count=count+1
print(count)
#odd
