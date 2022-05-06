# Handling missing keys in Python dictionaries
dict={'india':122,'japan':'4893'}
print(dict.get('japan','not found'))
print(dict.get('pakistan','not found'))
dict.setdefault('nepal','not found')
print(dict['nepal'])
