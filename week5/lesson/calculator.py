def main():
    x = int(input("whats x? "))
    print("x squared is,", square(x))

def square(n):
    return n * n


#And I'm doing this now proactively, because I want to make sure that
#when I import my square function, perhaps from another library,
#from another file, treating it as though it's a library,
#I want to make sure that main is not just automatically called itself.

if __name__ == "__main__":

    main()