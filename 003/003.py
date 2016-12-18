#!/usr/bin/env python

import sys

n = int(sys.argv[1])
i = 2

while i * i < n:
    while n % i == 0:
        n = n / i
    i += 1

print n
