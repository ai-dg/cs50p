import sys
import csv
from tabulate import tabulate


def main():
    # Check number of arguments and extend file .csv
    if len(sys.argv) != 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if not ".csv" in sys.argv[1]:
        print("Not a CSV file")
        sys.exit(1)

    # Initialize variables
    pizzas = {}
    headers = []
    table = []
    # Extract all data from .csv file into a Dict
    pizzas = file_treatement(headers)

    # Put values into a table
    for pizza, sizes in pizzas.items():
        row = (pizza, sizes["Small"], sizes["Large"])
        table.append(row)

    # Print table with tabulate library
    print(
        tabulate(table, headers=[headers[0], headers[1], headers[2]], tablefmt="grid")
    )


def file_treatement(headers):
    pizzas = {}
    try:
        # Read the file with csv library
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            # Update headers list
            headers.extend(reader.fieldnames)
            # Update Dict
            for row in reader:
                pizzas.update(
                    {
                        row[headers[0]]: {
                            "Small": row[headers[1]],
                            "Large": row[headers[2]],
                        }
                    }
                )
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    csvfile.close()
    return pizzas


if __name__ == "__main__":
    main()
