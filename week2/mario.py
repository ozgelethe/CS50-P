#vertical mario
def main():
    print_column(3)

def print_column(height):
    #print("#\n" * height, end="")
    for _ in range(height):
        print("#")

main()

#horizontal
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()