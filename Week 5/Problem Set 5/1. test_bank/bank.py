def main():
    greeting = input("Greeting: ")

    final_value = value(greeting)

    print(f"${final_value}")


def value(greeting):
    greeting = greeting.lower()
    greeting = greeting.strip()
    if greeting == "hello" or greeting[:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
