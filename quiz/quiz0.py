"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


def weight(n):
    """This function ask for a parameter for a weight on earth and prints the equivalent weight on moon."""
    # function weight
    #   moon weight equals to earth weight * 0.165
    #   print moon weight
    moon = n * 0.165
    print(f"The weight of the object in moon is {moon} .")


# weight(40)


"""
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Jupiter = weight on Earth * 2.528

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


def planet_weight(weight, planet):
    """Takes in weight and planet parameter and returns the equivalent weight on the indicated planet."""
    moon = weight * 0.165
    mars = weight * 0.378
    jupiter = weight * 2.528
    if planet == "moon":
        return moon
    elif planet == "mars":
        return mars
    elif planet == "jupiter":
        return jupiter
    else:
        return "I don't know."


print(planet_weight(44, "moon"))
print(planet_weight(44, "mars"))
print(planet_weight(44, "jupiter"))
print(planet_weight(44, "something"))
