import sys
import csv


def main():
    # Error case treatement
    if len(sys.argv) != 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if not ".csv" in sys.argv[1]:
        print("Not a CSV file")
        sys.exit(1)

    if not ".csv" in sys.argv[2]:
        print("Not a CSV file")
        sys.exit(1)

    # Recover the table with first, last and house values
    students = infile_treatement()

    # Create header table for DictWriter
    headers = ["first", "last", "house"]

    # Write into the new file
    with open(sys.argv[2], "w") as csvoutfile:
        writer = csv.DictWriter(csvoutfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students)

    csvoutfile.close()


def infile_treatement():
    students = []
    try:
        with open(sys.argv[1], "r") as csvinfile:
            reader = csv.DictReader(csvinfile)
            for row in reader:
                # Take the first value and split to first and last name
                word = row["name"]
                word = word.replace(" ", "")
                words = word.split(",")
                students.append(
                    {"first": words[1], "last": words[0], "house": row["house"]}
                )
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    csvinfile.close()

    return students


if __name__ == "__main__":
    main()
