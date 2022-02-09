# A program that returns the factorial of a number, n.

# n is the number that's going to get factorial
n = 3

# a is the factorial base
a = 1

if n < 0:
    print("Factorial doesn't exists in negative numbers.")
elif n == 0 or n == 1:
    print("The factorial is 1.")
else:
    while n > 1:
        a *= n
        n -= 1
    print(f"The factorial is {a}.")
