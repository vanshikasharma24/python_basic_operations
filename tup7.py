# Python – Elements frequency in Tuple
from collections import Counter
test_tup=(4,4,5,5,6,6,7,7,8,8)
res=dict(Counter(test_tup))
print(res)