# Calculate the sum of integers from 1 to 10.
n = 0
for i in range(11):
    n += i
    print(n)

iteration = 0
a = 0
while iteration < 11:
    a += iteration
    iteration += 1
    print(a)


# Calculate the sum of integers from 1 to 1000.
m = 0
for i in range(1001):
    m += i
    print(m)

iteration = 0
a = 0
while iteration < 1001:
    a += iteration
    iteration += 1
    print(a)


# Calculate the sum of all the odd numbers from 1 to 1000
num = 0
for i in range(1000):
    if i % 2 != 0:
        num += i
    else:
        i += 1
    print(num)

iteration = 0
a = 0
while iteration < 1000:
    if iteration % 2 != 0:
        a += iteration
    else:
        iteration += 1
print(a)
