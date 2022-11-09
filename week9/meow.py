for i in range(3):
    print("meow")

#######

MEOWS = 3

for i in range(MEOWS):
    print("meow")


#########

class Cat:
    MEOWS = 3
    def meow(self):
        for i in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()

########## mypy meow.py

def meow(n: int):
    for i in range(n):
        print("meow")

number: int = int(input("number: "))
meow(number)

###### str error

def meow(n: int) -> None:
    for i in range(n):
        print("meow")

number: int = int(input("number: "))
meows: str = meow(number)
print(meows)

############3

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("number: "))
meows: str = meow(number)
print(meows, end="")

###############

import sys

if len(sys.argv) == 1:
    print("meow")

elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")

# to the terminal:
#python meow.py -n 3

####################3

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")