def main():
    #get a input from user
    msg = input("Input: ")
    msg1 = shorten(msg)
    #print shorter
    print("Output: ", msg1)

def shorten(word):
    msg1 = ""
    #loop through every letter
    for letter in word:
        #check if letter is avowel
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            msg1 += letter
    #carefull!!!! return is in end of for loop
    return msg1

if __name__ == "__main__":

    main()
