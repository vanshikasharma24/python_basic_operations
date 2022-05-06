#reversing first and last element of the list 
list=[5,8,10,30,39]

x=list[0]
list[0]=list[4]
list[4]=x
print(list)
