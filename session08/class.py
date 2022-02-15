# Import and run the codes
# def main():
#     print(my_abs(-42))


# if __name__ == "__main__":
#     main()

# Swapping two variables
from unicodedata import name


a = 10
b = 20
a, b = b, a  # To swap two variables
print(a)
print(b)


# iteration
for letter in name:
    print(letter)

# Square root
a = 4
x = 3
y = (x + a / x) / 2  # Newton's method to compute square root
print(y)

# Each iteration makes the estimate more exact
x = y
y = (x + a / x) / 2
print(y)

# Repeating...
x = y
y = (x + a / x) / 2
print(y)

# A loop that starts with an initial estimate, x, and
# improves it until it stops changing
while True:
    print(x)
    y = (x + a / x) / 2
    if y == x:
        break
    x = y


while True:
    print(x)
    y = (x + a / x) / 2
    epsilon = 0.000000000000001
    if abs(y - x) < epsilon:
        break
    x = y
