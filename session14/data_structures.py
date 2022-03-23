# String and List
# 1. String to List
name = 'Angelina Mia'
lst = name.split()
print(lst)
another_way = list(name)
print(another_way)

# 2. List to string
''.join(lst)
print(lst)


# String and dict
# 1. String to dict
name = 'Angelina Mia'
d = {}
for l in name:
    d[l].get(l, 0) + 1      # Count the frequency of letters in the sting, key is letter, values are numbers

# This helps count the amount of times a character shows up
from collections import Counter
counter = Counter(name) # Works with string
counter = Counter(lst)  # Also works with list


# Sting and tuple
# 1. String to tuple
name = 'Angelina Mia'
t = tuple(name)
# Output: ('A','n','g','e','l','i','n','a',' ','M','i','a')
t = tuple(name.split()) # Split the string according to space and put them into a tuple
# Output: ('Angelina', 'Mia')
t = name.split()
# Output: ['Angelina', 'Mia']

# 2. Tuple to string
''.join(t)


# List and dict
name = 'Angelina Mia'
lst = name.split()  # Split the name into each characters
counter = Counter(lst)
# Output: Counter({'A': 1, 'n': 2, 'g': 1, 'e': 1, 'l': 1, 'i': 2, 'a': 2, ' ': 1, 'M': 1})


# List and tuple
t = tuple(lst)  # List to tuple
lst = list(t)   # Tuple to list


# String and set
name = 'Angelina Mia'
s = set(name)       # Create a list that only has a single appearance of an element


# List and set
s = set(lst)       # Create a list that only have an element a time
counter = dict(counter) #Change the counter into a dictionary

# Only immutable things can be used as a key


# Dict and tuple
lst = list(counter.keys())
# Output: ['A','n','g','e','l','i','a',' ','M']
lst = list(counter.values())
# Output: [1, 2, 1, 1, 1, 2, 2, 1, 1]

name = 'Angelina Mia'
d = {}
d = dict(Counter(name))
for k in counter.keys():
    print(k)
# Output: Iterate through the letters
for v in counter.values():
    print(v)
for k, v in counter.items():
    print(k, v)