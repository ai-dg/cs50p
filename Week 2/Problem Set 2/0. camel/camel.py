def main():
    camel = input("camelCase: ")
    for _ in camel:
        if _.isupper() == True:
            camel = camel.replace(_, "_" + _.lower())
    print(f"snake_case: {camel}")

main()
