def readfile(file: str):
    """Does grep on a string in a single file"""
    with open(file, "r") as fp:
        reader = fp.readlines()

    for index, line in enumerate(reader):
        if "for" in line:
            print(index)
    # print(reader)


if __name__ == "__main__":
    readfile("file.txt")
