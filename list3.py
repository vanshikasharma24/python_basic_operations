# Swap elements in String list
strlist=['i','am','vanshika','sharma']
print(strlist)
#string comprehension
res=[sub.replace('a','-').replace('m','a').replace('-','m') for sub in strlist]
print(res)