def main():
    yell("this is cs50")

def yell(phrase):
    print(phrase.upper())

if __name__ == "__main__":
    main()

############3

def main():
    yell(["This", "is", "CS50"])

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()


#############3

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()


#########

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()


###################
#List comprehensions allow you to create a list on the fly in one elegant one-liner.
#We can implement this in our code as follows:

def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()