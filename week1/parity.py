#x = int(input("what's x? "))

#if x % 2 == 0:
#    print("even")
#else:
#    print("odd")

def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    #ya da tek satırda toplayabilirsin:
    #return True if n % 2 == 0 else False
    #ya da
    #return n % 2 == 0

# bool for boolean value, its just "True" or "False"

main()