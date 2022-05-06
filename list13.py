list1 = [10, 21, 4, 45, 66, 93]
count=0
# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 != 0:
        print(num, end=" ")
        count=count+1
print(count)