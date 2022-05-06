# Python | Sort Python Dictionaries by Key or Value
dict={}
dict[1]=56
dict[2]=3
dict[3]=90
dict[5]=23
dict[4]=78
dict[6]=2
print(dict)
for i in sorted(dict.values()):
    print(i,end=" ")
for i in sorted(dict.keys()):
    print(i,end=" ")