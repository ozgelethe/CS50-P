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