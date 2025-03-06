import requests
import sys


def main():
    check_args()
    is_float()

    # Int cas to the user input
    n_bitcoins = float(sys.argv[1])

    # Take the content of the file json
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    # Take the response to an dict json
    object = response.json()

    # Dictionnary in 2D, the value of bitcoin has to be find in the keys and sub-keys
    value_float = float((object["bpi"]["USD"]["rate_float"]))

    total_command = value_float * n_bitcoins

    # Print total command dollar format
    print(f"${total_command:,.4f}")


# Check the quantity of arguments in cmd-l
def check_args():
    if (len(sys.argv) != 2):
        print("Missing command-line argument")
        sys.exit(1)
    # if (sys.argv[1].replace(".", "").replace(",", "").isnumeric() == False):
    #     print("Command-line argument is not a number")
    #     sys.exit(1)

# Check if the string is a float
def is_float():
    try:
        float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

main()
