import inflect

# Initialize of inflect object
p = inflect.engine()


def main():
    # Init of a list called names
    names = []

    # Infinite loop to takes all the names, ctrl-d to get out
    while(True):
        try:
            name = input("Name: ")
            if (name):
                names.append(name)
        except EOFError:
            print("")
            break

    if (names):
        # join fonction to finish the phrase with names submitted
        message = "Adieu, adieu, to " + p.join(names)
        print(message)

main()
