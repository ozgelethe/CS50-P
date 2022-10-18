def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
                pass
#if you want to ignore except(false) answer, you can use "pass"
#pass key will chatch the error but does nothing, ignores it

main()