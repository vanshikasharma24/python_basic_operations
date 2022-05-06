# Python – Records with Value at K index
test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
res=[]
element=3
for x,y,z in test_list:
    if y==element:
        res.append((x,y,z))
print(res)
