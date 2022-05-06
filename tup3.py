# Update each element in tuple list
tuplist=[(1,2,3),(4,5,6),(7,8,9)]
add_ele=4
res=[tuple(j+add_ele for j in sub)for sub in tuplist]
print(res)
# Multiply Adjacent elements
test_tup=(1,2,3,4,5)
print("The original tuple : " + str(test_tup))
res=tuple(i*j for i,j in zip(test_tup,test_tup[1:]))
print(res)