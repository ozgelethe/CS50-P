import sys
import csv
from PIL import Image, ImageOps

def main():
    check_arg()
    check_ext()
    #open image
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    #open shirt
    shirt = Image.open("shirt.png")
    #get the size of the shirt
    size = shirt.size
    #resize muppet image to fit shirt
    muppet = ImageOps.fit(image, size)
    #paste shirt in muppet
    muppet.paste(shirt, shirt)
    #create output image
    muppet.save(sys.argv[2])

#check arguments
def check_arg():

    if len(sys.argv) > 3:
        sys.exit("Too manny command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

#check extention
def check_ext():
    if ".jpg" in sys.argv[1] and ".jpg" not in sys.argv[2]:
        sys.exit("Input and output have different extentions")

    if ".jpeg" in sys.argv[1] and ".jpeg" not in sys.argv[2]:
        sys.exit("Input and output have different extentions")

    if ".png" in sys.argv[1] and ".png" not in sys.argv[2]:
        sys.exit("Input and output have different extentions")

    if (".jpg" not in sys.argv[1] or ".jpg" not in sys.argv[2]) and (".png" not in sys.argv[1] or ".png" not in sys.argv[2]) and (".jpeg" in sys.argv[1] and ".jpeg" not in sys.argv[2]):
        sys.exit("Invalid Input")

if __name__ == "__main__":
    main()