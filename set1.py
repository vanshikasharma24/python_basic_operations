# Find the size of a Set in Python
import sys
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}
print(sys.getsizeof(Set1))
print(sys.getsizeof(Set2))
print(sys.getsizeof(Set3))