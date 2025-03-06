def main():
    # Initialize input fruit value
    fruit = input("Item: ")

    # Put all the characters in lower case
    fruit = fruit.lower()

    # Initalize Dictionnary with the values of calories
    fruits = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantoloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80",
    }

    # Iteration in the dictionnary to find the key fruit value
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")


main()
