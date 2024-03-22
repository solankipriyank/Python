''' Write a Python program to count the occurrences of each word in a
given sentence.'''

a="the quick brown fox jumps over the lazy dog."
b=a.split()
print (dict((c,b.count(c))for c in b))
