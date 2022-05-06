# Python – Remove Tuples of Length K
test_list = [(4, 5),(8, 6, 7),(3, 4, 6, 7)]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# 1 liner to perform task
# filter just lengths other than K
# len() used to compute length
res = [sub for sub in test_list if len(sub) == K]

# printing result
print("Filtered list : " + str(res))