import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern_core = r"([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    pattern = (
        rf"^{pattern_core}\."
        rf"{pattern_core}\."
        rf"{pattern_core}\."
        rf"{pattern_core}$"
    )
    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
