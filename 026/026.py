# https://pballew.blogspot.com/2022/08/repeating-decimal-periods-and-patterns.html

# The length of the repetend is the smallest k such that 10^k == 1 (mod n)
# This is equivalent to finding the order of 10 mod n
# note this only works for primes
def repetend_length(n):
    for k in range(1, n):
        if pow(10, k, n) == 1:
            return k


longest = 0
longest_d = -1
d = 5

while d < 1000:
    repetend_len = repetend_length(d)
    if repetend_len and repetend_len > longest:
        longest = repetend_len
        longest_d = d
    d += 1

print(longest_d)
