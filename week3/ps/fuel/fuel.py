#make a while loop
while True:

    #get user input
    fuel = input("Fraction: ")

    #the try block lets you test a block of code for errors
    #the except block lets you handle the error
    #the else block lets you execute code when there is no error
    #the finally block lets you execute code,
    # regardless of the result of the try- and except blocks

    try:

        #try to split the fuel
        numerator, denominator = fuel.split("/")

        #convert into integers
        new_numerator = int(numerator)
        new_denominator = int(denominator)

        #calculate the percentage
        f = round(new_numerator / new_denominator, 2)

        #chech if its less than 1 and stop the loop
        if f <=1:
            break

    except (ValueError, ZeroDivisionError):
        pass

#multiply percentence by 100
p = int(f * 100)
#check if percentence is less than 1, print E
if p <= 1:
    print("E")
#check if percentence greater than 99, print F
elif p >= 99:
    print("F")
#otherwise, print the %
else:
    print(f"{p}%")

