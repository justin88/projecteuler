# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

import math

num = 600851475143
answer = -1


def isPrime(n: int):
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True


for i in range(2, math.ceil(math.sqrt(num))):
    if num % i == 0 and isPrime(i):
        answer = i


print(answer)

