#!/usr/bin/env python

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# * * *   *   *     +  *     *     +     *     *

myrange = list(range(1, 21))

num = 2520 * 11 * 13 * 16 * 17 * 19 // 8
print(num)
mynum = 1

for i in myrange:
    if num % i != 0:
        print("%s not disvisible by %s" % (i, num))
