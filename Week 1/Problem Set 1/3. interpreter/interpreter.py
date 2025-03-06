def main():
    operation = input("Expression: ")
    words = operation.split()

    integer_1 = float(words[0])
    operation = words[1]
    integer_2 = float(words[2])

    result = 0

    match operation:
        case "+":
            result = integer_1 + integer_2
        case "-":
            result = integer_1 - integer_2
        case "*":
            result = integer_1 * integer_2
        case "/":
            result = integer_1 / integer_2


    print(f"{result:.1f}")

main()
