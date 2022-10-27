import sys
import csv
from tabulate import tabulate

def main():
    check_arg()

    table = []

    #try to open file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)

    # #if file doesnt exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    #print the menu
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

#check arguments
def check_arg():

    if len(sys.argv) > 2:
        sys.exit("Too manny command-line arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()