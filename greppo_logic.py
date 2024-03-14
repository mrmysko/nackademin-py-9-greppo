# Skriv endast definitioner här på denna indenteringsnivå! Det är viktigt att du
# namnger funktioner, klasser och variabler exakt med de namn som står i
# beskrivningen.


def greppo_logic(search_terms, filenames, invert_match: bool, show_line_numbers: bool):
    # Collect matching lines in some thing...

    """for file in filenames:
    with open(file, 'r', encoding=utf-8) as fp:
        # read lines, looking for lines, or if inverted look for not lines
        use .readlines() and an iterator to keep track of which lines contain matches?
        save iterator and line in like a tuple or something?"""

    # saves tuple of index and line with match.
    """for file in filenames:
        with open(file, "r") as fp:
            reader = fp.readlines()

            for index, line in enumerate(reader):
                if invert_match == 1:
                    if not search_terms in line:
                        if show_line_numbers == 1:
                            print(f"{file}:{index}:{line}", end="")
                        else:
                            print(f"{file}:{line}", end="")
                else:
                    if search_terms in line:
                        if show_line_numbers == 1:
                            print(f"{file}:{index}:{line}", end="")
                        else:
                            print(f"{file}:{line}", end="")"""
    some_list = list()

    for file in filenames:
        with open(file, "r") as fp:
            reader = fp.readlines()

            match_lines = [
                line
                for x in search_terms
                for index, line in enumerate(reader)
                if x in line
            ]

            for i in match_lines:
                print(i, end="")

            # for index, line in enumerate(reader):
            #    match_lines = [line for x in search_terms if x in line for index, line in enumerate(reader)]
            #    some_list.extend(match_lines)
    # print(some_list)

    # for index, line in enumerate(reader):

    # print(match_lines)

    #   if any(x in line for x in search_terms):
    #        print(line, end="")

    # Ok, it prints. Now return a tuple with exit code instead.

    """Det här matchar ju t.ex. for i fortnite, alternativt använd re för att kolla 
    efter match object och printa hela strängen om en match hittas?
    """

    """Also, få bort alla nested ifs, måste finnas snyggare sätt att modifiera en loop om ett condition uppfylls."""


if __name__ == "__main__":

    greppo_logic(["for"], ["file.txt", "file2.txt"], 1, 1)
