import sys


def main():
    word = input("Input: ")
    word_modified = shorten(word)
    print(f"Output: {word_modified}")


def shorten(word):
    vowels = "aeiouAEIOU"
    for v in vowels:
        if v in word:
            word = word.replace(v, "")

    return word


if __name__ == "__main__":
    main()
