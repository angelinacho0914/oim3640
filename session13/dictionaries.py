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