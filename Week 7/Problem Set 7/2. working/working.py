import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    first_time, second_time = find_result(s)
    first_time, second_time = format_times(first_time, second_time)
    schedule = first_time + " to " + second_time
    return schedule


def format_times(first_time, second_time):

    first_times = first_time.split(" ")
    second_times = second_time.split(" ")

    check_minutes_and_hours(first_times[0], second_times[0])

    if first_times[1] == "PM":
        first_time = convert_to_PM(first_times[0])
    else:
        if not first_times[0].find(":") < 0:
            if (":") in first_times[0]:
                hours, minutes = first_times[0].split(":")
                if int(hours) == 12:
                    hours = 00
                first_time = f"{int(hours):02}:{minutes}"
        else:
            if int(first_times[0]) == 12:
                first_times[0] = "00"
            first_time = f"{int(first_times[0]):02}" + ":00"

    if second_times[1] == "PM":
        second_time = convert_to_PM(second_times[0])
    else:
        if not second_times[0].find(":") < 0:
            if (":") in second_times[0]:
                hours, minutes = second_times[0].split(":")
                if int(hours) == 12:
                    hours = 00
                second_time = f"{int(hours):02}:{minutes}"
        else:
            if int(first_times[0]) == 12:
                first_times[0] = "00"
            second_time = f"{int(second_times[0]):02}" + ":00"

    return first_time, second_time


def check_minutes_and_hours(first_times, second_times):
    times = first_times.split(":")
    hours = int(times[0])

    if hours > 12 or hours < 0:
        raise ValueError

    if len(times) > 1:
        minutes = int(times[1])
        if minutes > 59 or minutes < 0:
            raise ValueError

    times = second_times.split(":")
    hours = int(times[0])

    if hours > 12 or hours < 0:
        raise ValueError

    if len(times) > 1:
        minutes = int(times[1])
        if minutes > 59 or minutes < 0:
            raise ValueError


def find_result(s):

    pattern = r"(?P<first_time>(\d{1,2}:\d{1,2}|\d{1,2}) [APM]{2}) to (?P<second_time>(\d{1,2}:\d{1,2}|\d{1,2}) [APM]{2})"

    match = re.search(pattern, s)

    first_time = "None"
    second_time = "None"

    if match:
        first_time = match.group("first_time")
        second_time = match.group("second_time")
        return first_time, second_time

    if first_time == "None" or second_time == "None":
        raise ValueError


def convert_to_PM(s):
    times = s.split(":")
    to_convert = int(times[0])
    to_convert = to_convert + 12
    if to_convert == 24:
        to_convert = 12
    to_return = f"{str(to_convert):02}"
    if not len(times) == 1:
        to_return = to_return + ":" + times[1]
    else:
        to_return = to_return + ":00"
    return to_return


if __name__ == "__main__":
    main()
