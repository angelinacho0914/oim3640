# This function only takes in integer or float numbers and result to an absolute number
# isinstance(obj, class info) function


def my_abs(x):
    if isinstance(x, int) == True or isinstance(x, float) == True:
        if x < 0:
            x = -x
        else:
            x = x
        return x
    else:
        return "You can only input an integer or decimal numbers."


print(my_abs(-4))
print(my_abs(4))
print(my_abs("4"))
