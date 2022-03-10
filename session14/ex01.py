'''
Write a function called sumall that takes any number of arguments and returns their sum. Note: you are not allowed to use any built-in function.
'''

def sumall(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print(sumall(3, 4, 10))