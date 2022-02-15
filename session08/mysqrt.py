# A function, mysqrt, that takes a as a parameter, chooses
# a reasonablt value of x, and returns an estimate of the
# square root of a.


def mysqrt(a):
    """
    Takes a parameter and returns an estimate of the square
    root of a.
    """
    x = 3
    while True:
        y = (x + a / x) / 2
        epsilon = 0.000000000000001
        if abs(y - x) < epsilon:
            break
        x = y
    return x


def main():
    """Test here"""
    print(mysqrt(4))


if __name__ == "__main__":
    main()
