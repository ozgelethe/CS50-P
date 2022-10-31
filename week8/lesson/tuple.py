#1

def main():
    name, house = get_student()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    #the code on the upside will give error when user give us an house
    #other than "Raveclow". because tuples cant be changed..
    print(f"{student[0]} is from {student[1]}")

def student():
    name = input("name: ")
    house = input("house: ")
    return (name, house)
    # "return (name, house)" is a tuple. whole thing is a tuple and inside of this tuple
    # there is 2 values.
    # tuples are immutable, meaning we cannot change those values. Immutability is a way
    # by which we can program defensively. and it can prowide us bugs, mistakes.
if __name__ == "__main__":
    main()

#2

### IF we dont want to receive an error mesage and write with true value, we dont use
### tuple with "()" we use a list with "[]"
### BUT while you are accessing the value in tuple or list you use "[]" like student[0]

def main():
    student = get_student()
    print(f"{student[0]} is from {student[1]}")

def student():
    name = input("name: ")
    house = input("house: ")
    return [name, house]

if __name__ == "__main__":
    main()

#3

### IN DICTIONARY
### you must be careful you use student['name'] not student["name"]
### however "" in the outside and inside of dictionary values are gonna interfere

def main():
    student = get_student()
    print(f"{student['name']} is from {student['house']}")

def student():
    student = {}
    student["name"] = input("name: ")
    student["house"] = input("house: ")
    return student

if __name__ == "__main__":
    main()

### OR

def main():
    student = get_student()
    if student["name"] == "Padma":
        sstudent["house"] = "Ravenclaw"
    print(f"{student['name']} is from {student['house']}")

def student():
    name = input("name: ")
    house = input("house:
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()

