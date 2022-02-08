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
