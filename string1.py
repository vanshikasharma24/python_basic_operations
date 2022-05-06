# Function to check whether the
# string is palindrome or not
def palindrome(a):
    mid =(len(a)-1)//2
    start = 0
    flag =0
    last=(len(a)-1)
    while(start<=mid):
        if (a[start]==a[last]):
            start=start+1
            last=last-1
        else:
            flag==1
            break
    if flag==0:
        print("string is a palindrome")
    else:
        print("string is not a palindrome")


string="weawe"
palindrome(string)
