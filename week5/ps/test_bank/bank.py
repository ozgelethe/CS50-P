def main():
    #get a greeting
    greeting = input("Greeting: ")
    value1 = value(greeting)
    print(f"${value1}")

def value(greeting):
    new_g = greeting.lower().strip()

    #check the answer is hello
    if 'hello' in greeting:
        return 0
    #then give $20 for answers that start with'h'
    #strings are zero-based, so h is 0. word
    elif 'h' == greeting[0]:
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
