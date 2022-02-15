# A function named check_fermat that takes four parameters
# a, b, c, n - and checks to see if Fermat's theorem holds
# If n is greater than 2 and a^n + b^n = c^n program will
# print different things.
def check_fermat(a, b, c, n):
    """This function takes in 4 parameters and checks whether
    Fermat is wrong or not."""
    if a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


# check_fermat(1, 2, 3, 2)

# A function that prompts the user to input values for a, b,
# c, n, converts them to int, and uses check_fermat to check.
def fermat():
    '''
    This function takes 4 user inputs and checks whether Fermat is wrong or not.
    '''
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    c = int(input("Enter value 3: "))
    n = int(input("Enter a value: "))
    check_fermat(a, b, c, n)


# fermat()


# A function, calculate_bmi, takes two parameters, weight and height
def calculate_bmi(weight, height):
    """This function takes in weight and height and computes
    a BMI in USA system."""
    bmi = 703 * weight / height
    return bmi


# calculate_bmi(100, 5.1)

# A function, get_bmi_category, takes inputs and converts to float,
# uses calculate_bmi to calculte BMI value, returns BMI category
def get_bmi_category():
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    bmi = calculate_bmi(weight, height)
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi <= 24.9:
        return "Normal weight"
    elif 25 < bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"


print(get_bmi_category())
