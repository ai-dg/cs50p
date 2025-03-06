def main():
    # Initialize dictionnary with nothing
    grocery = {}
    while True:
        try:
            item = input("")
            # if there is no item to store, reprompt
            if item == "":
                continue
            # Check first if the item exist and +1 the quantity
            if item in grocery.keys():
                grocery[item] += 1
            # Update the dictionnary if the item doesn't exist
            else:
                grocery.update({item: 1})
        except EOFError:
            # Dictionnary sorted
            grocery = dict(sorted(grocery.items()))
            # Show all the items before to exit
            for _ in grocery:
                print(grocery[_], end=" ")
                print(_.upper())
            break;

main()
