#first ask your question
answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

#then say to 42s
if answer.strip() == "42":
    print("Yes")
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")