import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b[u|U][m]\b"
    matches = re.findall(pattern, s)
    return len(matches)


if __name__ == "__main__":
    main()
