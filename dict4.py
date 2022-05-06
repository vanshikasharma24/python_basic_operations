# Python program to find the sum of all items in a dictionary
dict={'a':1,'b':20,'c':100}
list=[]
for items in dict:
    list.append(dict[items])
sum=sum(list)
print(sum)