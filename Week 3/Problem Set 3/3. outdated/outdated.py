# Global variable declaration
months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def main():
    while True:
        date = input("Date: ")
        # Find the correct format treatment
        if "/" in date:
            # Case error if the formats aren't correct
            if first_format(date) == True:
                break
        if "," in date:
            if second_format(date) == True:
                break

# First format to treat MM/DD/YYYY
def first_format(d):
    numbers = d.split("/")
    # Try if the variables can be convert to integers
    try:
        months = int(numbers[0])
        days = int(numbers[1])
        years = int(numbers[2])
    except ValueError:
        return False
    # Checking if the variables have values off limits
    if months > 12 or months < 0:
        return False
    if days > 31 or days < 0:
        return False
    if years < 0:
        return False
    print(f"{years}-{months:02}-{days:02}")
    return True

# Second format to treat Month days, years
def second_format(d):
    global months
    # Erase the "," character
    d = d.replace(",", "")
    words = d.split()
    # Find the month and his value
    if words[0] in months:
        month = months[words[0]]
    else:
        return False
    try:
        days = int(words[1])
        years = int(words[2])
    except ValueError:
        return False
    if days > 31 or days < 0:
        return False
    if years < 0:
        return False
    print(f"{years}-{month:02}-{days:02}")
    return True

main()
