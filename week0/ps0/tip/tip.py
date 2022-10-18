def main():
    dollars = dollars_to_float(input("how much was your meal? "))
    percent = percent_to_float(input("what percentage would like to tip? "))
    tip = dollars * percent
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    dlr = d.replace("$", "")
    return float(dlr)

def percent_to_float(p):
    per = p.replace("%", "")
    p_converted = float(per) / 100
    return p_converted

main()