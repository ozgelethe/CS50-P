re.sub(pattern, repl, string, count=0, flags=0)
#The signature of the sub method is as follows
#Notice how pattern refers to the regular expression we are
#looking for. Then, there is a repl string that we can replace
#the pattern with. Finally, there is the string that we want to
#do the substitution on.

import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)


print(f"Username: {username}")