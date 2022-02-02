# This class is about Functions

# Infinite loop
def gd():
    print("Beginning of Groundhog day...")
    import time

    time.sleep(1)
    print("End of Groundhog day.")
    time.sleep(2)
    gd()


gd()
# Use Ctrl + C to interrupt an infinite loop

# To check whether the year is a leap year
year = 2020
print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# True and True and False

# Calculate the area of circle by inputing radius
# docstring is ''' ''' to create a hover definition
def area_of_circle(x):
    """print the area of a circle, given the radius"""
    ans = 3.14 * x ** 2
    return ans


print(area_of_circle(5))


def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")


print(type(print_lyrics))  # Type: function
print_lyrics()  # Call function


def repeat_lyrics():
    print_lyrics()
    print("Na na na na na, na na na na")
    print_lyrics()


repeat_lyrics()

# Parameters and arguments
def print_twice(name):
    print(name)
    print(name)


print_twice("Babson")

my_name = "Angelina"
print_twice(my_name)

# Functions with return values
def give_me_a_break():
    str1 = "break"
    return str1


print(give_me_a_break())


# pass statements are used when we do not have code but just wanna make it run
def nop():
    pass


age = int(input())
if age >= 18:
    pass  # without pass, you will see error


import math


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
