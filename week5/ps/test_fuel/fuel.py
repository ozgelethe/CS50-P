def main():
    #get user input
    fuel = input("Fraction: ")
    converted = convert(fuel)
    output = gauge(converted)
    print(output)


def convert(fuel):
    while True:
        try:
            #try to split the fuel
            numerator, denominator = fuel.split("/")
            #convert into integers
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            #calculate the percentage
            f = round(new_numerator / new_denominator, 2)
            #chech if its less than 1 and stop the loop
            if f <=1:
                p = int(f * 100)
                return p
            else:
                fuel = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(p):
    #check if percentence is less than 1, print E
    if p <= 1:
        return "E"
    #check if percentence greater than 99, print F
    elif p >= 99:
        return "F"
    #otherwise, print the %
    else:
        return str(p) + "%"

if __name__ == "__main__":
    main()