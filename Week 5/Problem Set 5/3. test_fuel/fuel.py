def main():
    # Loop to take and check the values
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
        # Reprompt again in error case
        except (ValueError, ZeroDivisionError):
            continue
        # if all values are ok, it breaks the loop
        else:
            break

    output = gauge(percentage)
    print(f"{output}")


def convert(fraction):
    words = fraction.split("/")
    try:
        x = int(words[0])
        y = int(words[1])
    except ValueError:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    result = (x / y) * 100
    return round(result)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        percentage = int(percentage)
        return f"{percentage}%"


if __name__ == "__main__":
    main()
