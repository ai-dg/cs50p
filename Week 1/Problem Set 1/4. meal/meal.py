def main():
    time = input("What time is it? ")
    time_int = convert(time)

    if time_int >= 7 and time_int <= 8:
        print("breakfast time")
    elif time_int >= 12 and time_int <= 13:
        print("lunch time")
    elif time_int >= 18 and time_int <= 19:
        print("dinner time")


def convert(time):
    times = time.split(":")

    hours = int(times[0])
    minutes = float(times[1])
    minutes = minutes / 60

    real_time = hours + minutes

    return real_time


if __name__ == "__main__":
    main()
