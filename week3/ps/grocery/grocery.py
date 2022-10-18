#create empty dictionary
grocery_list = {}

#loop forever
while True:

    try:
        #get user an input
        item = input().lower()

        #check if item is already in the dictionary
        if item in grocery_list:

            #if it is, add 1 in count
            grocery_list[item] +=1

        #otherwise, add the item for the first time
        else:
            grocery_list[item] = 1

    except EOFError:
        #print all the items in alphabetical order
        for key in sorted(grocery_list.keys()):
            print(grocery_list[key], key.upper())

        #stop the wile loop
        break
