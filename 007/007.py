#!/usr/bin/env python

n = 120000
marked = {}
for i in range(2, n + 1):
    marked[i] = True

for i in range(2, int(n**.5)):
    if marked[i]:
        for j in range(i**2, n, i):
            marked[j] = False

count = 1
for i in marked:
    if marked[i]:
        if count == 10001:
            print(i)
            break
        count += 1
