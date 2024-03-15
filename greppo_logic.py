# Todo - Error-handling
# Todo - Less ifs
# Todo - Only match actual search_terms, not "for" in "fortnite" - DONE
# Todo - Invert seems to match empty lines. - FIXED

"""Do I need to collect all the lines, and then iterate AGAIN over matched lines and remove them?
        Or maybe do a key,value pair updating 0/1 if the word is found and then save the line if either any are found, or invert none is."""

import re


def greppo_logic(search_terms, filenames, invert_match: bool, show_line_numbers: bool):
    """Returns lines matching items in search_terms."""

    match_lines = list()

    for file in filenames:
        with open(file, "r", encoding="utf-8") as fp:
            reader = fp.readlines()

            """OR...save filenames, and matches as separate strings, and if show_line_numbers is True, save that too.
            Then just do a ''.join() on those three parts and append to the list. Then I could cut down the code for line numbers."""

            if invert_match:
                for index, line in enumerate(reader):

                    # Reset search_word tracker.
                    search_word_dict = dict((i, False) for i in search_terms)

                    for key in search_word_dict.keys():
                        # Returns a match object. True if a match is found.
                        if re.search(rf"\b{key}\b", line):
                            search_word_dict[key] = True

                        # Returns False if any value in search_word_dict is True. Check length of string to not add empty strings. (\n counts as a char)
                        if not any(search_word_dict.values()) and len(line) > 1:
                            match_lines.append(rf"{file}:{index}:{line.strip()}")
                            """Now, hur kokar jag ner den här i en list comprehension?"""

            # This is not readable tbh.                
            # If note invert match, easier.
            else:
                match_lines.extend(
                    [
                        f"{file}:{str(index) + ":" if show_line_numbers == True else ''}{line.strip('\n')}"
                        for x in search_terms
                        for index, line in enumerate(reader)
                        if re.search(rf"\b{x}\b", line)
                    ]
                )

    for i in match_lines:
        print(i)

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    # if len(match_lines) == 0:
    #    exit_code = 1
    # else:
    #    exit_code = 0

    # return (exit_code, match_lines)

    """Also, få bort alla nested ifs, måste finnas snyggare sätt att modifiera en loop om ett condition uppfylls."""


if __name__ == "__main__":
    pass
