

def main():
    phrase = input("")
    phrase2 = convert(phrase)
    print(phrase2)

def convert(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase


main()
