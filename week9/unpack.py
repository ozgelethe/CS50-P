first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")

###########

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50, 25), "Knuts")

############

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "Knuts")

###########3 DICTIONARY

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")


########### ===

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")

###########3


def f(*args, **kwargs):
    print("positional: ", args)

f(100, 50, 25, 5)

############33

def f(*args, **kwargs):
    print("named: ", kwargs)

f(galleons=100, sickles=50, knuts=25)

########3#######