import random
import sys


def main():

    # Recover input level value
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            continue

    # Rand int beetwen 1 and the level
    random_number = random.randint(1, level)

    # Check guess input conditions and his value with random_number
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            if guess == random_number:
                print("Just right!")
                sys.exit(0)
            elif guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
        except ValueError:
            continue


main()
