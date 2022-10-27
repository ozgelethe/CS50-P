# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello", line.rstrip())


# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

#for not alphabetical, but reverse alphabetical:
# for name in sorted(names, reverse=True):

for name in sorted(names):
    print(f"hello, {name}")

# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())
