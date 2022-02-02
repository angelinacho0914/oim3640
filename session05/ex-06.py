import math

def quadratic(a, b, c):
    if a == 0:
        print("This is not a quadratic solution.")
    else:
        check1 = b * b - 4 * a * c # Calculate discriminant
        check2 = math.sqrt(abs(check1))

        if check1 > 0:
            print((-b + check2)/(2 * a))
            print((-b - check2)/(2 * a)) 
        elif check1 ==0:
            print(-b / (2 * a))
        else:
            print(- b / (2 * a), " + i", check2)
            print(- b / (2 * a), " - i", check2)

quadratic(1, 10, -12)