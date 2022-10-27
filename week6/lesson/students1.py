import csv

students = []

with open("students.csv") as file:

    # reader = csv.reader(file)
    reader = csv.DictReader(file)

    for row in reader:

        # students.append({"name": name, "hometown": hometown})
        # students.append({"name": row["name"], "hometown": row["hometown"]})
        students.append(row)

    # for row in reader:
    #     students.append({"name": row[0], "hometown": row[1]})


for student in sorted(students, key=lambda student: student["name"]):

    print(f"{student['name']} is from {student['hometown']}")