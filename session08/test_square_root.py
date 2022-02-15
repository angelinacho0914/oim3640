# # A function that prints a table like this:

# a   mysqrt(a)     math.sqrt(a)  diff
# -   ---------     ------------  ----
# 1.0 1.0           1.0           0.0
# 2.0 1.41421356237 1.41421356237 2.22044604925e-16
# 3.0 1.73205080757 1.73205080757 0.0

# The first column is a number, a
# the second column is the square root of a computed with mysqrt
# the third column is the square root computed by math.sqrt
# the fourth column is the absolute value of the difference between the two estimates.
import mysqrt
import math


def test_square_root():
    """
    Test how well mysqrt function is working.
    """
    print(f"a   mysqrt(a)     math.sqrt(a)  diff")
    print(f"-   ---------     ------------  ----")
    a = 1.0
    for i in range(10):
        b = round(mysqrt.mysqrt(a), 1)
        c = round(math.sqrt(a), 1)
        abs_num = round(abs(b - c), 1)
        print(f"{a} {b}           {c}           {abs_num}")
        a += 1


test_square_root()
