# String and List
# 1. String to List
name = 'Angelina Mia'
lst = name.split()
print(lst)
another_way = list(name)
print(another_way)

# 2. List to string
' '.join(lst)
print(lst)


# String and dict
name = 'Angelina Mia'
d = {}
for l in name:
    d[l].get(l, 0) + 1

# This helps count the amount of times a character shows up
from collections import Counter
counter = Counter(name) # Works with string
counter = Counter(lst)  # Also works with list


# List and set
s = set(lst)       # Create a list that only have an element a time

# Only immutable things can be used as a key