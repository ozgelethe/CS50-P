def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))
            #1
            #get rid of x, else, break and return x;
            # return int(input("what's x? "))
        # except ValueError:
                # print("x is not an integer")

        except ValueError:
                print("x is not an integer")
        else:
            break
    return x

main()