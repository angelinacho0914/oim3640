import random

class Covid():
    base_sequence = "abcd"
    """
    Covid class
    """
    def __init__(self, name="unknown covid", new_seq="###"):
        self.name = name
        self.extension = new_seq
        self.sequence = self.base_sequence + '.' + self.extension

    def replicate(self):
        '''
        Return a new covid instance by replicating itself
        '''
        return Covid(name = "Replicated " + self.name, new_seq = self.extension)


    # Special/magic method
    def __add__(self, another_covid):
        """
        Overloading the + operator
        Return a new Covid instance by mixing self and another covid.
        """
        new_seq = ''.join(random.choices(self.extension + another_covid.extension, k = 3))
        return Covid(name = 'New Covid from Mixing', new_seq=new_seq)


    def __str__(self):
        """
        This method makes print(object) available.
        Represent the instance in a human-readable format.
        """
        return f'{self.name}: {self.sequence}'



covid_0 = Covid("Ground zero")   # Creating an instance of Covid by invoking the initializing method, __init__
covid_1 = Covid(name = "second case", new_seq = "123")

print(covid_0)
print(covid_1)
covid_2 = covid_1.replicate()
print(covid_2)
# print(covid_2.mix(covid_0).sequence)
print(covid_0 + covid_2)