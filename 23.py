'''Write a Python function to insert a string in the middle of a string.'''


s = 'Python'
s1 = s.rjust(8, '(')
s2 = s1.ljust(10, ')')
print(s2)
