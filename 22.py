'''Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.'''


s =str(input("Enter the string:"))
d=s[0:2]
a=s[-2:]
if len(s)>2:
   print(d+a)
else:
   print('empty')
