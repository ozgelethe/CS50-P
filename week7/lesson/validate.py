import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w\.)?\w.+\.(edu|com|net|org)$", email):
    print("Valid")
else:
    print("Invalid")