import sys


def main():
    if len(sys.argv) != 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if not ".py" in sys.argv[1][-3:]:
        print("Not a Python file")
        sys.exit(1)

    lines_of_code = count_lines()
    print(f"{lines_of_code}")


def count_lines():
    lines_of_code = 0
    try:
        with open(sys.argv[1], "r") as file:
            for lines in file:
                to_count = lines.lstrip()
                if not to_count or to_count.startswith("#") == True:
                    continue
                lines_of_code += 1

    except FileNotFoundError:
        print("File doest not exist")
        sys.exit(1)

    return lines_of_code


if __name__ == "__main__":
    main()
