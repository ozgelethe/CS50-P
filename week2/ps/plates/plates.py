def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


def is_valid(s):
    #vanity plates may contain a maximum of 6 characters(letters or number)
    #and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    #the isalpha() medhod returns True if all the characters are alphabet letters
    #string.isalpha()
    #all vanity plates must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    #numbers cannot be used in the middle of a plate; they must come at the end
    #the first number cannot be a "0"

            # i = 1
            # while i < 9:
                # print(i)
                # if i == 1:
                    # break
                # i +=1
            #this while loop's output is just a "1" because it broke after 1st loop

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    #numbers cannot be used in the middle of a plate
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    #no periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False


    #if we pass all the tests, return true
    return True

main()