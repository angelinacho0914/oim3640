# A program that computes the Fibonacci number of an int, n

# 0 = 0, 1= 1+0
def fibonacci(n):
    a = 0
    b = 1
    # if n is less than 0 print incorrect
    # if n is equals to 0 return 0
    # if n is 1 then return 1 (b)
    # else return for loop 1, n
    # c = a + b
    # a = b
    # b = c
    # return b
    if n < 0:
        print("Negative numbers doesn't exists in Fibonacci sequence.")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


print(fibonacci(5))
