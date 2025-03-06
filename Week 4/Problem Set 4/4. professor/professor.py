import random
import sys


def main():
    level = get_level()
    score = 0

    # Start 10 exercices
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        # Check if the answer is correct, if not, the loop breaks if the tries becomes 0
        tries = 3
        while tries > 0:
            try:
                result = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                tries -= 1
                continue

            true_result = x + y
            if result == true_result:
                score += 1
                break
            else:
                print("EEE")
                tries -= 1

        # Show the correct answer before continue to the next exercice
        if tries == 0:
            print(f"{x} + {y} = {true_result}")

    # Print the score at the end
    print(f"Score: {score}")


# Get the input correct value of level
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except ValueError:
            continue
    return level


# Get a random value for each specific level
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
