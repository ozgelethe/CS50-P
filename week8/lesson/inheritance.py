
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Inside of my student class, I now have a function called get.
    # It is, I shall claim, a class method what does that mean.
    # It just means I can call this method without instantiating a student object first.
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()


#########
#HAT.PY

# We may want, though, to run the sort function without creating a particular
# instance of the sorting hat (there’s only one, after all!). We can modify our
# code as follows:
import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")

#### OPERATOR OVERLOADING
# https://docs.python.org/3/reference/datamodel.html#special-method-names
#While we have just introduced inheritance, we have been using this all along
# during our use of exceptions. It just so happens that exceptions come in a
# heirarchy, where there are children, parent, and grandparent classes.
# These are illustrated below:
# BaseException
#  +-- KeyboardInterrupt
#  +-- Exception
#       +-- ArithmeticError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- KeyError
#       +-- NameError
#       +-- SyntaxError
#       |    +-- IndentationError
#       +-- ValueError
# learn more in Python’s documentation of exceptions: https://docs.python.org/3/library/exceptions.html

### WIZARD.PY

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
            self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

#### VAULT.PY

class Vault:
    def __init__(self, gold=0, dollar=0, cents=0):
        self.gold = gold
        self.dollar =dollar
        self.cents = cents

    def __str__(self):
        return f"{self.gold} Gold, {self.dollar} Dollar, {self.cents} Cents"

    def __add__(self, other):
        gold = self.gold + other.gold
        dollar = self.dollar + other.dollar
        cents = self.cents + other.cents
        return Vault(gold, dollar, cents)

potter = Vault(100,50,25)
print(f"potter: ", potter)

ron = Vault(25, 50, 100)
print(f"ron:", ron)

total = potter + ron
print(f"total: ", total)
