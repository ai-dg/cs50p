from validator_collection import validators, checkers


def main():
    print(check_email(input("What's your email address? ")))


def check_email(s):
    try:
        email = validators.email(s)
    except ValueError:
        return "Invalid"

    checker_email = checkers.is_email(email)

    if checker_email == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
