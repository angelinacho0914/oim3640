# Define any class: Use the following methods:
# 1. __init__ method that initializes some attributes. One of the attributes has to be an empty list.
# 2. __str__ method that returns a string that reasonably represent the thing.


class Boba():
    """
    Class of Boba
    """
    def __init__(self, tea_name="boba tea", boba="Yes"):
        self.tea_name = tea_name
        self.boba = boba

    def __str__(self):
        '''
        
        '''
        return f'This is {self.tea_name}, and {self.boba} for Boba.'
    
    def order(self):
        self.tea_name = input("What is your order? Lychee Black Tea/Passion Fruit Tea/Milk Tea")
        self.boba = input("Do you want Boba? Yes or No")

        return f'You have ordered {self.tea_name} and {self.boba} for Boba.'


boba_0 = Boba("Lychee Black Tea", "Yes")
print(boba_0)

boba_1 = boba_0.order()
print(boba_1)
