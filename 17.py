'''Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
'''

def chars(a,b):
    A=b[:2]+a[2:]

    B=a[:2]+b[2:]

    return A+' '+B

print(chars('abc','xyz')) 
