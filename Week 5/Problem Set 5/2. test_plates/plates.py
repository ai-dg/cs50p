def main():
    # Initialize plate user value
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)
    # Length condition plates
    if length > 6 or length < 2:
        return False
    # If the first two letters is alpha
    if not s[:2].isalpha() == True:
        return False
    # Find the index of the first numeric character
    index = 0
    for c in s:
        if c.isnumeric() == True:
            break
        index += 1
    # if numeric character is found, check all conditions of the numbers and positions
    if index > 0 and index != length:
        if s[index:].isnumeric() == False:
            if s[index:].isalpha() == False:
                return False
        if s[index] == "0":
            return False
    return True


if __name__ == "__main__":
    main()
