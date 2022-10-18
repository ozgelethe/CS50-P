import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    sys.exit(1)

#you can then get a list of available fonts with code like this:
figlet.getFonts()

if isRandomFont == False:
    try:
        #you can set the font with code like this, wherein f is the font’s name as a str:
        figlet.setFont(font=sys.argv[2])

    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())

msg = input("Input: ")

print("Output: ")
print(figlet.renderText(msg))