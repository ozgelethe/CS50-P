import sys

def main():
    get_file()
    #try to open file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()

    #if file doesnt exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    # checkthe lines for # and spaces
    count_lines = 0
    for line in lines:
        if check_line(line) == False:
            count_lines += 1
    print(count_lines)

def get_file():

    if len(sys.argv) > 2:
        sys.exit("Too manny command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()