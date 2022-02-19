# The following functions are all supposed to check whether a str
    # contains any lowercase letters.
# Describe what the function actually does.

# This function checks if "s" string is completely lower case.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# This function returns 'True' string all the time because 'c' is lowercase.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


# This function returns whether the last letter of s string is lowercase(true) or not(false).
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


# This function returns true if the last letter in string s is lowercase.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


# Return False if last letter of s string is not lowercase, else return true.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
