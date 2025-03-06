import inflect
import datetime
from datetime import date
import re

p = inflect.engine()


def check_and_get_date(str):

    years = None
    months = None
    days = None

    pattern = r"(?P<years>[0-9]{4})-(?P<months>([0][1-9]|[1][0-2]))-(?P<days>([0][1-9]|[1-2][0-9]|[3][0-1]))"

    matches = re.search(pattern, str)

    if matches:
        years = matches.group("years")
        months = matches.group("months")
        days = matches.group("days")

        if not years or not months or not days:
            raise ValueError
    else:
        raise ValueError

    return int(years), int(months), int(days)


def main():

    str = input("Date of Birth: ")

    try:
        years, months, days = check_and_get_date(str)
    except ValueError:
        print("Invalid date")
        exit(1)

    date1 = datetime.date(years, months, days)
    date2 = datetime.date.today()
    time = abs(date2 - date1)
    total_minutes = time.total_seconds() / 60
    words = p.number_to_words(int(total_minutes), andword="").capitalize()
    print(words + " minutes")


if __name__ == "__main__":
    main()
