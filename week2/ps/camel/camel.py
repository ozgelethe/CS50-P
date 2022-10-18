#get a camel name first
camelCase = input("camelCase: ")

#print snake_case
print("snake_case: ", end="")

#for item in str:
#for item in string the variable item receives the character directly,
#so you dont have to use the index. for example; if you have a variable s,
#that holds the value "buzz" and you want to print all the letters of the string
#each at a time we do s equals to "buzz" for "char" in s print chart.
#the word letter can be replaced by any other word or letter you desire.
#the main idea is taht this loop will give you every character at every
#iteration of the variable

# s = "buzz"
# for char in s:
    #print(char)

#loop through every letter
for letter in camelCase:

    #the isupper() method returns True if all the characters are in upper case,
    #otherwise, False. numbers, symbols and spaces are not checked, only alphabet
    #for example;
    # x = "APPLE"
    # print (x.isupper())
    #it's a True statement

    #check if letter is upper case
    if letter.isupper():

        #print undercores and the letter in lowercase
        print("_" + letter.lower(), end="")

    #otherwise, print letter
    else:
        print(letter, end="")

#print space in the end
print()