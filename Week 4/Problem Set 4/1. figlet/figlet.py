import sys
import random

from pyfiglet import Figlet


def identify_cases():
    case = "nothing"
    if len(sys.argv) == 1:
        case = "case_1"
    elif len(sys.argv) == 3:
        case = "case_2"
    return case


def main():
    # Checking if the number of args is ok
    if len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Invalid usage")
        sys.exit(1)

    # Identify the usage case
    case = identify_cases()

    # Case 1 for random font and case 2 for an defined font
    if case == "case_1":
        case_random()
    else:
        case_defined()


def case_random():
    # Figlet library usage
    figlet = Figlet()
    # Get font list
    list_fonts = figlet.getFonts()
    # Find a random value
    random_font = random.choices(list_fonts)
    # Put the string of the value, random_font is a list too
    figlet.setFont(font=random_font[0])
    # Input user asking
    text = input("Input: ")

    # Show the text modified
    print(f"Output: \n{figlet.renderText(text)}")

    sys.exit(0)


def case_defined():
    # Font text in argv[1] case 2
    font_text = sys.argv[1]
    # Check if "-f" or "-font" exist
    if font_text != "-f" and font_text != "-font":
        print("Invalid usage")
        sys.exit(1)
    font_type = sys.argv[2]

    # Figlet library
    figlet = Figlet()
    list_fonts = figlet.getFonts()

    # Trying if font_type exist
    try:
        list_fonts.index(font_type)

    except ValueError:
        print("Invalid usage")
        sys.exit(1)

    figlet.setFont(font=font_type)
    text = input("Input: ")

    print(f"Output: \n{figlet.renderText(text)}")

    sys.exit(0)


main()
