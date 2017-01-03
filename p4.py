# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
#  9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

answer = 0


def isPalindrome(x):
    s = str(x)
    return s == s[::-1]


for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if isPalindrome(product):
            answer = max(answer, product)

print(answer)
