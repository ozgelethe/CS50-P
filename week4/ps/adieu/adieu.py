import inflect

p = inflect.engine()

#create list to keep track of names
names = []

#loop forever
while True:
    try:
        #get a input from user
        name = input("Name: ")
        names.append(name)
####
#the append() method appends(adds) an element to the end of the list.for example:

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)
#it prints; ["apple", "banana", "cherry", "orange"]
####

    except EOFError:
        print()
        break
        #create a new line and stop the loop


#printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)
