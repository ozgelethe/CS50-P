# to comment lines: CTRL + K + C
# to uncomment lines: CTRL + K + U

names = []

for _ in range(3):
    name = input("whats your name? ")
    names.append(name)
    #names.append(input("whats your name? "))

#function sorted() is returning a sorted version of that list
for name in sorted(names):
    print(f"hello, {name}")
