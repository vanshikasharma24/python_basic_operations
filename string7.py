# Uppercase Half String
test_string=input("input string")
lenstr=len(test_string)
halflen=lenstr//2
res=' '
for indx in range(len(test_string)):
    if indx>= halflen:
        res += test_string[indx].upper()
    else:
        res += test_string[indx]
print("The resultant string : " + str(res))