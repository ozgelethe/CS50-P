# get a expression from user
expression = input("Expression: ")

#convert this into variables
x, y, z = expression.split(" ")

#change the type of variables x and z to float
new_x = float(x)
new_z = float(z)

#calculate floats
if y == "+":
    result = new_x + new_z

if y == "-":
    result = new_x - new_z

if y == "*":
    result = new_x * new_z

if y == "/":
    result = new_x / new_z

print(round(result, 1))

