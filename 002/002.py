#!/usr/bin/env python

t1 = 1
t2 = 2

mysum = 0
while t2 < 4000000:
    if t2 % 2 == 0:
        mysum += t2
    tmp = int(t1)
    t1 = t2
    t2 = tmp + t2

print mysum
