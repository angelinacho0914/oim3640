from BabsonPerson import BabsonPerson
from Student import Student
from Person import Person


class Professor(BabsonPerson):
    """"""
    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def speak(self, newutterance):
        utterance = "In course " + self.course + " we say "
        return BabsonPerson.speak(self, utterance + newutterance)

    def __str__(self):
        return f'Professor {self.name} is teaching {self.course}.'


def main():
    p1 = Professor('Zhi Li', 'OIM 3640')
    print(p1)
    print(p1.id)
    # Checking if p1 object is any of the class mention
    print(isinstance(p1, BabsonPerson))
    print(isinstance(p1, Person))
    print(isinstance(p1, Student))
    print(isinstance(p1, Professor))

    print(p1.speak("Python is awesome!"))


if __name__ == "__main__":
    main()
