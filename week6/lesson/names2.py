# in Python, there's this function called open whose purpose in life is to
# do just that, to open a file, but to open it up programmatically so that you,
# the programmer, can actually read information from it or write information to it.

name = input("whats your name? ")

#file = open("names.txt", "w")
# "w" open the names.txt file and even if there isnt a names.txt file,
# it creates one. but this is dangereus because it recreate everytime
# you run the program, so your earlier content will be gone.
# "a" for append

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
