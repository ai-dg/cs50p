from PIL import Image
from PIL import ImageOps
import sys


def main():
    check_values()

    try:
        # Open first image and shirt.png
        with Image.open(sys.argv[1]) as profile:
            with Image.open("./shirt.png") as tshirt:
                # Recover tshirt size
                size = tshirt.size
                # Fit profile to tshirt size
                profile = ImageOps.fit(profile, size)
                # Paste tshirt image and mask put the correct position to the muppet
                profile.paste(tshirt, (0, 0), mask=tshirt)
                profile.save(sys.argv[2])

    except FileNotFoundError:
        print("Could not find the image file")
        sys.exit(1)


def check_values():
    if len(sys.argv) != 3:
        print("Too few command-line arguments")

    # Recover files extension from the arguments
    first_extension = sys.argv[1][-4:]
    second_extension = sys.argv[2][-4:]

    if check_extensions(first_extension) == False:
        print("Invalid input")
        sys.exit(1)

    if check_extensions(second_extension) == False:
        print("Invalid input")
        sys.exit(1)

    if first_extension != second_extension:
        print("Input and output have different extensions")
        sys.exit(1)


# Find the correct extensions with match
def check_extensions(extension):
    match extension:
        case ".jpg":
            return True
        case ".jpeg":
            return True
        case ".png":
            return True
        case _:
            return False


if __name__ == "__main__":
    main()
