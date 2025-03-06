def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = d
    dollars = d.strip("$")
    d_float = float(dollars)
    return d_float


def percent_to_float(p):
    percent = p
    percent = percent.strip("%")
    p_float = float(percent) / 100
    return p_float


main()
