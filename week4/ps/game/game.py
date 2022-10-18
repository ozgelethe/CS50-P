import random

#get a level from user

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
            pass

#set random number
i = random.randint(1, level)

#get guess and check
while True:
    try:
        guess = int(input("Guess: "))
        if i == guess:
            print("Just right!")
            break
        elif i < guess:
            print("Too large!")
        else:
            print("Too small!")
    except:
            pass