def main():
    # get a message from user
    message = input("what's your message? ")
    # call convert function
    result = convert(message)
    # print the result
    print(result)

def convert(message):
    # replace :) for smiley
    msg1 = message.replace(":)", "🙂")
    #replace :( for sadd
    msg2 = msg1.replace(":(", "🙁")
    # return string
    return msg2

main()
