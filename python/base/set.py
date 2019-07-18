
char_list=['a','b','c','c','d','d']
sentence='Welcome Back to This Tutorial'
print(set(char_list))
print(set(sentence))
unique_char=set(char_list)
unique_char.add('x')
#unique_char.clear()
print(unique_char)
unique_char.remove('x')
print(unique_char)
print(unique_char.discard('y'))

