#get a input from user
msg = input("Input: ")

#print shorter
print("Output: ", end="")

#loop through every letter
for letter in msg:

    #check if letter is avowel
    if not letter.lower() in ["a", "e", "i", "o", "u"]:
        print(letter, end="")

#print new message
print()