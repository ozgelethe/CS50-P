# Classes provide us to create our own type of data and give them names.
# A class is like a mold(kalıp) for a type of data – where we can invent our own
# data type and give them a name.
# We can modify our code as follows to implement our own class called "Student:"
# classes are mutable but we can make them immutable
class Student:
    ...

def main():
    student = get_student()
    # name and house are instance variables of this class
    print(f"{student.name} is from {student.house}")

def get_student():
    # in here "student" is a object of "Student" class
    student = Student()
    student.name = input("name: ")
    student.house = input("house: ")
    return student

if __name__ == "__main__":
    main()


### OR

class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()


###

class Student:
    # __init__ method, that determines the behavior of an object of class Student.
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


### OR we can force the users to give us what we wanted

class Student:
    # if you want that a variable like house is optional
  # def __init__(self, name, house=None):
    def __init__(self, name, house):
        if not name: # this equals to --> if name == ""
            #you can deside the error name like: CatError, NameError ets.
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

###

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    try:
        return Student(name, house)
    except Value:
        ...

if __name__ == "__main__":
    main()

###


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


### __str__
# __str__ is a special method that, if you define it inside of your class,
# Python will just automatically call this function for you any time some other function
# wants to see your object as a string.

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} is from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)

if __name__ == "__main__":
    main()


####

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} says {self.patronus}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

###

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} says {self.patronus}"

    def charm(self):
        match self.patronus:
            case "stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()
    print("expecto patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()


### ON THE OTHERHAND YOU CAN STILL MESS WITH INPUT AND IGNORE IT LIKE THIS:
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    #############################################
    student.house = "Number Four, Privet Drive"##
    #############################################
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

### PREVENT BUGS LIKE THIS;
# because of the getter and the setter we are gonna get a ValueError and have a
# chance to solve the bug by removing line279 "student.house = "Number Four, Privet Drive"
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # GETTER
    @property
    def house(self):
        return self._house
    # SETTER
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

####

print(type(...))

#### lets get_student into class

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