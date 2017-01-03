# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


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


primeCount = 0
answer = 2


while True:
    if isPrime(answer):
        primeCount += 1
        if primeCount == 10001:
            break
    answer += 1


print(answer)


