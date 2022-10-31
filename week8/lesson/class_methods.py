# @classmethod

# Sometimes, we want to add functionality to a class itself, not to instances of
# that class. @classmethod is a function that we can use to add functionality to a
# class as a whole. Here’s an example of not using a class method.
# In your terminal window, type code hat.py and code as follows:

import random
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        # house = random.choice(self.house)
        # print(name, "is in", house)
        print(name, "is in", random.choice(self.houses))

hat = Hat()
hat.sort("Harry")

####

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

