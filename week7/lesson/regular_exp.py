# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m, n} m-n repetitions

import re

email = input("what's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("valid")
else:
    print("invalid")

#Notice how we utilize the “escape character” or \
# as a way of regarding the . as part of our string
# instead of our validation expression. Testing your code,
# you will notice that malan@harvard.edu is regarded as valid,
# where malan@harvard?edu is invalid.

......


# ^   matches the start of the string
# $   matches the end of the string or
#  just before the newline at the end of the string

......


# []    set of characters
# [^]   complementing the set

import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

#Notice that ^ means to match at the start of the string.
# All the way at the end of our expression, $ means to
# match at the end of the string. [^@]+ means any character
# except an @. Then, we have a literal @. [^@]+\.edu means
# any character except an @ followed by an expression ending in
# .edu. Typing in malan@@@harvard.edu is now regarded as invalid.

#We can still improve this regular expression further. It turns
# out there are certain requirements for what an email address can be!
# Currently, our validation expression is far too accomodating. We might
# only want to allow for characters normally used in a sentence.
# We can modify our code as follows:

import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_].+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

#WHAT THE FUCKING FUCK
#^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$

