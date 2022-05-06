#python program to swap any 2 elements of the list
mylist=[3,4,5,1,8,10]
pos1=int(input("enter pos1"))
pos2=int(input("enter pos2"))
temp=mylist[pos1]
mylist[pos1]=mylist[pos2]
mylist[pos2]=temp
print(mylist)