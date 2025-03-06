# name = input("What's your name? ").strip().title()

# first, last = name.split(" ")

# print(f"Hello, {first} {last}")





def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)





main()
