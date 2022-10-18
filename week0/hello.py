#ask their name
name = input("whats your name? ")

#remove whitespaces from str
name = name.strip()

#capitalize users name
name = name.capitalize()

#split users name into first name and last name
first, last = name.split(" ")

#capitalize users name
#name = name.title()
#combinate both or more
#name = name.strip().title()
#name = input("whats your name? ").strip().title()


#say hello to user
print(f"hello, {first}")
