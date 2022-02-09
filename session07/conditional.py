# Conditional
age = 3
if age >= 18:
    print("Your age is", age)
    print("adult")
else:
    print("Your age is", age)
    print("teenager")

age = 3
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")


# Recursion
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(3)


def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)


# Infinite recursion
def recurse():
    recurse()
