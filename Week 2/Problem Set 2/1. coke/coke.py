def main():

    # Initialize the initial amount due
    amount = 50

    # Loop to continuously ask for coin inputs until the amount is paid or exceeded
    while True:
        # Ask the user to insert a coin and convert it to an integer
        coin = int(input("Insert Coin: "))

        # Check if the coin is a valid denomination (5, 10, or 25)
        if coin == 5 or coin == 10 or coin == 25:
            amount = amount - coin

            # If the remaining amount is still positive, show how much is left to pay
            if amount > 0:
                print(f"Amount Due: {amount}")
            else:
                result = -(amount)
                print(f"Change Owed: {result}")
                break

        # Invalid coin input
        else:
            print(f"Amount Due: {amount}")

main()
