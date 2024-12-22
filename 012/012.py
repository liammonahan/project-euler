import math


def count_divisors(number):
    divisors = 0
    sqrt_n = int(math.sqrt(number))
    for i in range(1, sqrt_n + 1):
        if number % i == 0:
            divisors += 2  # i and number / i
    if sqrt_n * sqrt_n == number:
        divisors -= 1  # Correct for perfect square
    return divisors


n = 0
triangle = 0

divisors = 0
while divisors <= 500:
    triangle += n
    n += 1

    if n % 2 == 0:
        divisors = count_divisors(n // 2) * count_divisors(n - 1)
    else:
        divisors = count_divisors(n) * count_divisors((n - 1) // 2)

print(triangle)
