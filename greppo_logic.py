# Todo - Error-handling
# Todo - Less ifs
# Todo - Only match actual search_terms, not "for" in "fortnite"
# Todo - Invert seems to match empty lines.


def greppo_logic(search_terms, filenames, invert_match: bool, show_line_numbers: bool):
    """Returns lines matching items in search_terms."""

    match_lines = list()

    for file in filenames:
        with open(file, "r", encoding="utf-8") as fp:
            reader = fp.readlines()

            # This is not readable tbh.
            if invert_match:
                if show_line_numbers:
                    match_lines.extend(
                        [
                            f"{file}:{index}:{line.strip('\n')}"
                            for x in search_terms
                            for index, line in enumerate(reader)
                            if x not in line
                        ]
                    )
                else:
                    match_lines.extend(
                        [
                            f"{file}:{line.strip('\n')}"
                            for x in search_terms
                            for line in reader
                            if x not in line
                        ]
                    )
            else:
                if show_line_numbers:
                    match_lines.extend(
                        [
                            f"{file}:{index}:{line.strip('\n')}"
                            for x in search_terms
                            for index, line in enumerate(reader)
                            if x in line
                        ]
                    )
                else:
                    match_lines.extend(
                        [
                            f"{file}:{line.strip('\n')}"
                            for x in search_terms
                            for line in reader
                            if x in line
                        ]
                    )

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    if len(match_lines) == 0:
        exit_code = 1
    else:
        exit_code = 0

    return tuple((match_lines, exit_code))

    """Det här matchar ju t.ex. for i fortnite, alternativt använd re för att kolla 
    efter match object och printa hela strängen om en match hittas?
    """

    """Also, få bort alla nested ifs, måste finnas snyggare sätt att modifiera en loop om ett condition uppfylls."""


if __name__ == "__main__":
    pass
