# def for define functions
# "to" is a parameter
# to="world" şeklinde sabitlenebilir

# def hello(to):
#     print("hello,", to)

# name = input("what's your name? ")
# hello(name)

def main():
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()