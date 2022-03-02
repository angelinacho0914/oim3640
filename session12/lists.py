# List is immutable
# in operator also works in List
AFC_east = ['New England Patriots','Buffalo Bills', 'Miami Dolphins',
            'New York']
print('Buffalo Bills' in AFC_east)


# List can be nested
L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python',['Ruby','On Rail'],'PHP'],
    ['Adam','Bart','Lisa']
]

print(L[0][0])
print(L[2][2])
print(L[1][2][1])
print(L[1][2][1][2]) # Index of ' '


# Traversing a List
# Searching a List, can find a word inside a item using in operator
for team in AFC_east:
    print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2     # Times 2 on all the items

print(numbers)
# A very common mistake is that you thought you mutate the list but you didn't
for i in numbers:
    i = i ** 2
# Result is i = 81 but the numbers list didn't safe the changes


my_list = ['spam',1,['New England Patriots',\
                    'Buffalo Bills', 'Miami Dolphins', \
                    'New York Giants'], \
            [1, 2, 3]]
print(len(my_list))


# * operator is different by reference and by values
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # Will get a list of c = [1, 2, 3, 4, 5, 6]

a = [[0]]
a = a * 4
a = a[0] * 4
print(a)


t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x','y']
print(t)

# This function maps the function of the method capitalize
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


# An operation like "sum" that combines a sequence of elements into a single value is called "reduce"
t = [1, 2, 3]
print(sum(t))


# An operation like "only_upper" is called a filter because it selects some of the elements
# and filters out the others
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


# Deleting elements
t = ['a','b','c','d']
x = t.pop(1)  # pop modifies the list and returns the element that was removed
print(x)
print(t)

x = t.pop()   # If no index is provided, it deletes and returns the last element
print(x)
print(t)

# Another way to remove an item or items from a list is "del"
t = ['a','b','c','d','e']
del t[1:3]
print(t)

# If you know the element you want to remove, but not index, use "remove"
t = ['a','b','c']
t.remove('b')
print(t)


# List and strings
# To convert from a string to a list of characters, you can use "list":
team = "Patriots"
t = list(team)      # Avoid using list as variable name
print(t)            # Avoid l because it looks like 1

# Breaking a string into words
team = "New England Patriots"
t = team.split()
print(t)

# Optional argument called delimeter specifies which characters to use as word boundaries
# e.g. using hyphen as a delimeter
s = 'spam-spam-spam'
delimteter = '-'
t = s.split(delimteter)
print(t)

# join is the inverse of split
t = ['New', 'England', 'Patriots']
team = '!!'.join(t)
print(team)


# Objects and values
a = 'banana'
b = 'banana'

print(a is b) # Return whether they refer to the same string

a = [1, 2, 3]
b = [1, 2, 3]   # The two lists are equivalent but not identical,not the same object
print(a is b)

a = [1, 2, 3]
b = a
b is a
# A object with more than one reference has more than one name,
# so we say that the object is aliased.
b[0] = 'something else'
print(a)        # They refer to the same object, so if a is changed b will also change


# Common mistakes with lists
t = t.sort()    # Doesn't work, it only modify the argument and return None

t.append(x)
t = t + [x]
t += [x]

t.append([x])   # INCORRECT
t = t.append(x) # INCORRECT
t + [x]         # INCORRECT
t = t + x       # INCORRECT

# Make copies to avoid aliasing
t = [3, 1, 2]
t2 = t[:]
t2.sort()
print(t)
print(t2)