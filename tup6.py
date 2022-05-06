# Python – Remove Tuples from the List having every element as None
test_list=[(None, 2), (None, None), (3, 4), (12, 3), (None, )]
res=[sub for sub in test_list if not all(ele==None for ele in sub)]
print(res)