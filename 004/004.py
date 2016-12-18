#!/usr/bin/env python

def pal(num):
    num = str(num)
    leng = len(num)
    first = num[:leng/2]
    second = num[leng/2:][::-1]

    if len(first) != len(second):
        return first == second[:-1]
    else:
        return first == second

n1 = 99
n2 = 99

matches = []

for n1 in reversed(range(100, 1000)):
    for n2 in reversed(range(100, 1000)):
        potential_palindrome = n1 * n2
        if pal(potential_palindrome):
            matches.append(potential_palindrome)

print max(matches)

