balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    print("Balance:", balance)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()


############

#Utilizing our powers from our experience with object-oriented programming,
# we can modify our code to use a class instead of a global variable.
# In the text editor window, code as follows:


class Account:

    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance +=n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

#Notice how we use account = Account() to create an account.
# Classes allow us to solve this issue of needing a global variable more cleanly
# because these instance variables are accessible to all the methods of this class utilizing self.