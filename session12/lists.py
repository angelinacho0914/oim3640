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

