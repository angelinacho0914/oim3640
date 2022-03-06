from audioop import reverse


grades = dict()

grades['John'] = 90
grades['Smith'] = 85
print(grades)

grades = {'Andrea': 87, 'George': 83}
print(grades)

'Andrea' in grades # only check the keys, not values
'Andrea' in grades.keys()

90 in grades.values() # check the values

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = histogram('Bookkeeper')
print(h)

number_of_e = h.get('e', 0)
number_of_a = h.get('a', 0)
print(number_of_e)
print(number_of_a)


# Looping and dictionaries
def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('Massachusetts')
print_hist(h)

for key in sorted(h):
    print(key, h[key])


# Reverse lookup
def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()     # Raise statement causes an exception, LookupError, which is a built-in exception used to indicate that a lookup operation failed.

h = histogram('Massachusetts')
key = reverse_lookup(h, 2)
print(key)


# Dictionaries and lists
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)


# Memo fibonacci - Exercise 2 and 3
known = {0:0, 1:1}     # Keep track of the Fibonacci numbers we alr know.

def fibonacci(n):      # When this is called it checks known, it it's new value, add it to dictionary, and return it
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res     # res is a global variable and it's different in a way that known is kept as a memo, while res is modified for the result
    return res

for i in range(10):
    print(fibonacci(i), end=", ")
