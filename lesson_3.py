#Lesson 3: For a certain integer n, write a program to create a dictionary containing (i, i*i) as integers from 1 to n (including 1 and n) and then print this dictionary.

n = 8
d = dict()
for i in range(1,n+1):
    d[i]=i*i

print (d)