# Count occurrences of an element in a list
mylist=[2,1,2,4,10,2,6,2,8,8,10]
userinput=int(input("enter a number from list whose occurance you want to find"))
count = 0
for item in mylist:
    if userinput == item:
        count=count+1
print(count)


