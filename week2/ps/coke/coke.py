#variable to keep track
amount_due = 50

#loop until price is greater than 0
while amount_due > 0:

    #print the amunt due
    print("Amount Due: ", amount_due)

    #ask user to insert coin
    insert_coin = int(input("Insert Coin: "))

    #check if coin is 25, 10 or 5 cents
    #if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
    if insert_coin in [25, 10, 5]:

        #substract value from amount_due
        amount_due -= insert_coin

#the abs() function returns the absolute value of the specified number.
# x = abs(-7.25)
# print(x)

#calculate changed_owed
change_owed = abs(amount_due)


#print the result
print("Change Owed: ", change_owed)