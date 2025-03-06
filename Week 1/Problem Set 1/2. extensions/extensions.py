def main():
    extension = input("File name: ")
    extension = extension.lower()
    extension = extension.strip()
    index = extension.rfind(".")

    match extension[index:]:
        case ".gif":
            print("image/gif")
        case ".jpg":
            print("image/jpeg")
        case ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
