def main():
    n = int(input("n: "))
    for i in range(n):
        print("🐑" * i)

if __name__ == "__main__":
    main()

#########

def main():
    n = int(input("n: "))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return "🐑" * n

if __name__ == "__main__":
    main()


########333


def main():
    n = int(input("n: "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()


#########3