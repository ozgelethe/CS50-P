#create menu dict
menu = {
     "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#set current price to 0
total_amount = 0

#make a while loop
while True:

    try:
        #get user input
        item = input("Item: ").title()

        #check if item is already in dictionary
        if item in menu:

            #add the item price to currentt price
            total_amount += menu[item]

            #print current price
            print("Total: $", end="")
            print("{:.2f}".format(total_amount))

    except EOFError:
        #print a new line and stop the loop
        print()
        break

