# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character

# A|B     either A or B
# (...)   a group
# (?:...) non-caputuring version

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.(edu|com|net|org)$", email):
    print("Valid")
else:
    print("Invalid")

##

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w\.)?\w.+\.(edu|com|net|org)$", email):
    print("Valid")
else:
    print("Invalid")

####
#Notice how we combine two lines of our code.
#The walrus := operator assigns a value from right to left
#and allows us to ask a boolean question at the same time.
#Turn your head sideways and you’ll see why this is called a walrus operator.

# "?" or "*" is for " "

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")