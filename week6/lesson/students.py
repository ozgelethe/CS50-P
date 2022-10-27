# with open("students.csv") as file:
#     for line in file:
#       # name, hometown = line.rstrip().split(",")
#         row = line.rstrip().split(",")
#       # print(f"{name} is in {hometown}")
#         print(f"{row[0]} is in {row[1]}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, hometown = line.rstrip().split(",")
#         students.append(f"{name} is in {hometown}")

# for student in sorted(students):
#     print(student)

#[] creates a empty list
#{} creates a empty dictionary

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, hometown = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["hometown"] = hometown
#         student = {"name": name, "hometown": hometown}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['hometown']}")


students = []

with open("students.csv") as file:
    for line in file:
        name, hometown = line.rstrip().split(",")
        student = {"name": name, "hometown": hometown}
        students.append(student)
#lambda function is a anonymous function. you can use for a function
#that you are gonna use just once
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['hometown']}")