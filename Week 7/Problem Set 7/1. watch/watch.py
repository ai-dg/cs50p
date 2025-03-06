import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern = r'src="(?P<URL>(?:https|http)://(?:www\.)?(?:youtube\.com/embed)/[^"]+)"'

    match = re.search(pattern, s)

    if match:
        url = match.group("URL")

        url = url.replace("www.youtube.com/embed", "youtu.be")
        url = url.replace("youtube.com/embed", "youtu.be")
        url = url.replace("http", "https")
        url = url.replace("httpss", "https")

        return url
    else:
        return "None"


if __name__ == "__main__":
    main()
