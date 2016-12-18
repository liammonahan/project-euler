#!/usr/bin/env python

n = 120000
marked = {}
for i in range(2, n + 1):
    marked[i] = True

for i in range(2, int(n**.5)):
    if marked[i] == True:
        for j in range(i**2, n, i):
            marked[j] = False

count = 1
for i in marked:
    if marked[i] == True:
        if count == 10001:
            print i
            break
        count += 1
        
print count