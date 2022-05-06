# Test if tuple is distinct
# initialize tuple
test_tup = (1, 4, 5, 6, 1, 4)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Test if tuple is distinct
# Using loop
res = True
temp = set()
for ele in test_tup:
    if ele in temp:
        res = False
        break
    temp.add(ele)

# printing result
print("Is tuple distinct ? : " + str(res))