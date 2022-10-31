class Vault:
    def __init__(self, gold=0, dollar=0, cents=0):
        self.gold = gold
        self.dollar =dollar
        self.cents = cents

    def __str__(self):
        return f"{self.gold} Gold, {self.dollar} Dollar, {self.cents} Cents"

    def __add__(self, other):
        gold = self.gold + other.gold
        dollar = self.dollar + other.dollar
        cents = self.cents + other.cents
        return Vault(gold, dollar, cents)

potter = Vault(100,50,25)
print(f"potter: ", potter)

ron = Vault(25, 50, 100)
print(f"ron:", ron)

total = potter + ron
print(f"total: ", total)