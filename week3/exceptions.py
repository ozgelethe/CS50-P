# 1
#SyntaxError
#undeterminated string literal : başlanan bir kod bitirilmemiş. öreneğin ;

# print("hello, world)


#2
#ValueError
#invalid literal for int() with base: if user give us a valua that dont match
#with wanted value type. For example if user write "cat" as a input in the code,

# x = int(input("what's x? "))
# print(f"x is {x}")

#we're going to get a value error. so, we have to prevent this error.
#we can fix this with keyword "try" and "except" like this;

# try:
#   # x = int(input("what's x? "))
    # print(f"x is {x}")
# expect ValueError:
    # print ("x is not an integer")


# 3
#NameError
#name error tends to your code, like you are doing something with the name
#of a variable that you shouldn't.
#for example if user write "cat" as a input in the code,

# try:
#   # x = int(input("what's x? "))
# except ValueError:
    # print ("x is not an integer")

# print(f"x is {x}")

#we're going to a get a NameError: name "x" is not defined.
#we can fix this with keyword "try", "except", and "else" like this;

# try:
#   # x = int(input("what's x? "))
# except ValueError:
    # print ("x is not an integer")
# else:
    # print(f"x is {x}")

#in a nutshell about "try", "except", and "else" ;
#in first python is going to try to execute try lines
#if something goes wrong, it's going to execute except lines to handle that value error
#however, if you try and this codee succeeds, then there is no exception to handle.
#so, you're going to execute else lines.


while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
