def readfile(files: str, line_num=0, invert=0):
    """Does grep on a string in a single file"""

    invert = 1
    line_num = 1

    for file in files:
        with open(file, "r") as fp:
            reader = fp.readlines()

        for index, line in enumerate(reader):
            if invert == 1:
                if not "for" in line:
                    if line_num == 1:
                        print(f"{file}:{index}:{line}", end="")
                    else:
                        print(f"{file}:{line}", end="")
            else:
                if "for" in line:
                    if line_num == 1:
                        print(f"{file}:{index}:{line}", end="")
                    else:
                        print(f"{file}:{line}", end="")
        # print(reader)
        # if len(matches) != 0:
        #    return tuple(matches, 1)

    """Det här matchar ju t.ex. for i fortnite, alternativt använd re för att kolla 
    efter match object och printa hela strängen om en match hittas?
    """

    """Also, få bort alla nested ifs, måste finnas snyggare sätt att modifiera en loop om ett condition uppfylls."""


if __name__ == "__main__":
    readfile("file.txt")
