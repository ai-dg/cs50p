def main():
    # Loop to take and check the values
    while True:
        fraction = input("Fraction: ")
        words = fraction.split("/")
        try:
            value1 = int(words[0])
            value2 = int(words[1])
            result = float(value1 / value2)
            if result > 1:
                continue
        # Reprompt again in error case
        except (ValueError, ZeroDivisionError):
            continue
        # if all values are ok, it breaks the loop
        else:
            break
    # Transform the float to percent format
    result = result * 100
    # Round sup the value
    if result - int(result) >= 0.5:
        result = int(result) + 1\
    # Display result cases
    if result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        result = int(result)
        print(f"{result}%")


main()
