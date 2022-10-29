#strip()
#Remove spaces at the beginning and at the end of the string
# txt = ",,,,,rrttgg.....banana....rrr"

# x = txt.strip(",.grt")

# print(x)
#it prints "banana"

import re

name = input("whats your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

matches = re.search(r"^(.+), *(.+$)", name)
if matches:
# if matches := re.search(r"^(.+), *(.+$)", name):

    name = matches.group(2) + " " + matches.group(1)
    # last, first = matches.groups()
    # name = f"{first} {last}"
print(f"hello, {name}")