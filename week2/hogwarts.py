#variables
students = ["hermione", "harry", "ron"]

#print(students[0])
#print(students[1])
#print(students[2])

#for student in students:
#    print(student)
#student in here, is just a variable. you can use "_" or "i" ets

for i in range(len(students)):
#range() sıralama
#len() function give the length of the list
#and we can list our students with range(), after we get to know the lenght of list
    print(i + 1, students[i])

