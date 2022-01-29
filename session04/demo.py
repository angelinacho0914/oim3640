import math
import random

# Lists use square brakets, equivalent of an array
# Dictionaries {'key1': 'value1', 'key2: value2'}
# Tuples are immutable, you can't change the values inside them.
# Files uses open('eggs.txt')
# Sets uses set('name'), {'value1', 'value2', 'value3'}
# doesn't allow duplicated values

print(len(str(2**1000000)))

print(math.pi)

print(random.random())

print('I\'m \"ok\".') # The backward slash makes the quotation mark after it neutral.
print('I\'m learning\n Python.') # The \n gives a line.
print('\\\n\\') # Two backward slash represents 1 slash when printed.
print('\\\t\\') # The \t gives a tab between the two slashes printed.
print(r'\\\t\\') # The r'' avoids the function of back slash.

print('''line1
... line2
... line3''') # Instead of \n, we could use '''...''' to display multiple lines.

print(5 > 3)  # Prints out a True value
print(3 > 5)  # Prints out a False value
print(not 1 > 2)  # Double negative and prints out True

# If else statement
# General rule: arithmetic > comparison > not > and/or
age = 31
if age >= 21:
    print('Yes, you can.')
else:
    print("Sorry, you can't.")