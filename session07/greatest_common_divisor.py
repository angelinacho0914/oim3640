# Find the greatest common divisor of two positive int
# It's the largest int that divides each of them without remainder
import math


# use the bigger of the two and subtract the other = c
# compare c with the smaller of the two
# express the original bigest as the bigger one minus the smaller one
# keep on doing this until a - b = c and b == c


def gcd(a, b):
    if a < b:
        smallest = a
    else:
        smallest = b
    for i in range(1, smallest + 1):
        if (a % i == 0) and (b % i == 0):
            answer = i
    return answer


print(gcd(48, 12))
