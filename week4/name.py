#command-line arguments

# import sys
# print("hello, my name is", sys.argv[1])

#while runnig the program dont forget to write your name xd
#to the terminal
#python name.py rukiye

#if you write sys.arg[0], output will be "hello, my name is name.py"

#if you dont write your name, you will receive an IndexError: list index out
# of range because the program try too accsesssome element that does not exist

# import sys
# try:
    # print("hello, my name is", sys.argv[1])
# except IndexError:
    # print("too few arguments")

import sys

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is", sys.argv[1])

#or

# import sys

# if len(sys.argv) < 2:
    # sys.exit("too few arguments")
# elif len(sys.argv) > 2:
    # sys.exit("too many arguments")

# print("hello, my name is", sys.argv[1])


# import sys

# if len(sys.argv) < 2:
    # sys.exit("too few arguments")
#for arg in sys.argv[1:]:
    # print("hello, my name is", sys.argv[1])

#it prints that the users write, starting from 1st element not from element 0

