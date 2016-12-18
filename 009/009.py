#!/usr/bin/env python

import sys

for a in range(1, 1000):
    for b in range(2, 1000):
        c = a**2 + b**2
        c = c**0.5
        if a + b + c == 1000:
            print a*b*c
            print a
            print b
            print c
            sys.exit(0)