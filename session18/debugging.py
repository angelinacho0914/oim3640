# If we can predict what error we are going to get we can do this
try:
    number = int(input("Please enter a number: "))
    result = 2022 / number
    print(result)
except ZeroDivisionError:
    print("You've entered a zero")
except ValueError:
    print("You should enter a number")
finally:        # Always executed after try and except blocks
    print("No matter what happens, we will still get here")
