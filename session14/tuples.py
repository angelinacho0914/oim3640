# Tuples are like lists but immutable
from re import A


t = 'a', 'b', 'c', 'd', 'e'
# OR t = ('a', 'b', 'c', 'd', 'e')

# t = tuple('Babson')
print(t[0])
print(t[1:3])


# Bc tuples are immutable, you can't modify the elements, but you can replace one tuple with another
t = ('A',) + t[1:]  # Makes a new tuple and then makes t refer to it


# Tuple assignment
a = 10
b = 90
a, b = b, a # Swap the values of two variables

email = 'ycho5@babson.edu'
id, domain = email.split('@')
print(id)
print(domain)


# Typles as return values
t = divmod(7, 3)  # Takes two arguments and returns a tuple of two values, the quotient and remainder
print(t)


# A parameter name that begins with * gathers arguments into a tuple
def printall(*args):
    print(args)

printall(1, 2.0, '3', None, True)

t = 7, 3
divmod(*t) # divmod(t) wouldn't work because divmod() needs 2 arguments


# Lists and tuples
s = 'abc'
t = [0, 1, 2]
print(zip(s, t))
# Takes two or more sequences and returns a list of tuples, where each tuple contains one element from each sequence
# The result is a zip object that knows how to iterate through the pairs
# The most common use of zip is in a for loop:
for pair in zip(s, t):
    print(pair)
# Zip object is a kind of iterator, which is any object that iterates through a sequence
print(list(zip(s, t)))  # Turning a zip to a list

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True   # Returns True if there is at least one try
    return False

damn = [2, 7, '2']
what = [3, 4, '3']
print(has_match(damn, what))

# Iterates a sequence of paris, each pair contains an index (from 0) and an element from the given sequence
for index, element in enumerate('abc'):
    print(index, element)


# Dictionaries and tuples
d = {'a':0, "b":1, "c":2}
t = d.items()  # .items() returns a sequence of tuples, where each tuple is a key-value pair
t
for key, value in d.items():
    print(key, value)


# Sequence of sequences
# Different kinds of sequences (strings, lists, and tuples) can be used interchangeably
# Strings are more limited than other sequences because the elements have to be characters. Immutable. If need the ability to change the characters in a string (as opposed to creating a new string), you might want to use a list of characters instead.
# Lists are more common than tuples, bc they are mutable. But there are few cases where you might prefer tuples:
# 1. In some contexts, it is syntactically simpler to create a tuple than a list.
# 2. If want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string.
# 3. If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.

# Tuples are immutable, they don't provide methods like sort and reverse, which modifies the lists.
# But sorted takes any sequence and returns a new list with the same elements in sorted order, and reversed, which takes a sequence and returns an iterator that traverses the list in reverse order.
