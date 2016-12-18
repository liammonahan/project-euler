#!/usr/bin/env python

n = 2000100
marked = {}
for i in range(2, n + 1):
    marked[i] = True

for i in range(2, int(n**.5) + 2):
    if marked[i] == True:
        for j in range(i**2, n, i):
            marked[j] = False

mysum = 0
for i in marked:
    if marked[i] == True:
        if i < 2000000:
            mysum += i
        
print mysum