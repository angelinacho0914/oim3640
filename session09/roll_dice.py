# Roll a dice, random int 1-6
# Roll dice 100 times
# Repeat 10 times

# Part 1 - Roll 100 dice, add up the sum
# 1. Create a var to store the sum, sum, initialized at 0
# 2. Import random library
# 3. Repeat the following step(s) 100 times:
#    - Get a random int in range (1, 6)
#    - Add the random int to result
# 4. Print the result

# Part 2 - Repeat the simulation 10 times
# 1. Repeat Part 1 10 times


import random
from sre_parse import REPEAT_CHARS

def roll_dice(n):
    '''
    Takes 1 parameter, which is the number of times user
    wants to repeat the function, and print the sum of 100
    dice n times.
    '''
    for j in range(n):                  # Repeat the funtion 10 times
        sum = 0
        for i in range(100):            # Roll a dice 100 times and add sum
            dice = random.randint(1,6)
            sum += dice
        print(sum)


# Another way
def simulation():
    '''
    Return the sum of the random int between 1 to 6 100 times
    and the average value.
    '''
    sum = 0
    for i in range(100):            # Roll a dice 100 times and add sum
        dice = random.randint(1,6)
        sum += dice
    print(sum, sum/100)

def repeat_simulation(n):
    '''
    Repeat a function n times.
    '''
    for i in range(n):
        simulation()

def main():
    # roll_dice(10)
    # simulation() Testing Code
    repeat_simulation(100)

if __name__ == "__main__":
    main()