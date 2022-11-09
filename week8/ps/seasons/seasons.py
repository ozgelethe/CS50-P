from datetime import date
import re
import sys
import inflect

p = inflect.engine()

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

def main():
    born = input("Date of Birth: ")
    try:
        year, month, day = get_date(born)
    except:
        sys.exit("Invalid Date")
    birthday = date(int(year), int(month), int(day))
    today = date.today()
    diff = today - birthday
    minutes = diff * 24 * 60
    output = p.number_to_words(minutes.days, andword="")
    print(output.capitalize() + " minutes")

def get_date(born):
    if re.search(r"^([0-2]?...)-([0-1][0-9])-([0-3][0-9])", born):
        year, month, day = born.split("-")
        return year, month, day

if __name__ == "__main__":
    main()