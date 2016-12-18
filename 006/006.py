#!/usr/bin/env python

n = 100
sq_sum = (n*(n+1)/2)**2
for i in range(1, n+1):
    sq_sum -= i**2

print sq_sum
