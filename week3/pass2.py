def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
                pass
#if you want to ignore except(false) answer, you can use "pass"
#pass key will chatch the error but does nothing, ignores it

main()