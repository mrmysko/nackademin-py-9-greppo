# Todo - Error-handling
# Todo - Less ifs
# Todo - Only match actual search_terms, not "for" in "fortnite" - DONE
# Todo - Invert seems to match empty lines.

"""Do I need to collect all the lines, and then iterate AGAIN over matched lines and remove them?
        Or maybe do a key,value pair updating 0/1 if the word is found and then save the line if either any are found, or invert none is."""

import re


def greppo_logic(search_terms, filenames, invert_match: bool, show_line_numbers: bool):
    """Returns lines matching items in search_terms."""

    search_word_dict = dict((i, False) for i in search_terms)
    match_lines = list()

    for file in filenames:
        with open(file, "r", encoding="utf-8") as fp:
            reader = fp.readlines()

            for line in reader:

                # Reset search_word tracker.
                search_word_dict = dict((i, 0) for i in search_terms)

                # Iterate over keys, looking for matches. If a match is found, flip that key to True.
                for key, value in search_word_dict.items():
                    if key in line:
                        search_word_dict[key] = True

                # Returns False if any value in search_word_dict is True.
                if not any(search_word_dict.values()) and len(line) > 1:
                    match_lines.append(rf"{file}:{line.strip()}")
                else:
                    pass
                """Now, hur kokar jag ner den här i en list comprehension?"""

                # print(search_word_dict)

    print(match_lines)

    # This is not readable tbh.
    # When invert looks for lines not containing "for", it matches lines containing "banan"...
    # but then when it looks for not "banan", it matches lines containing "for".
    # """if invert_match:
    #    if show_line_numbers:
    #        match_lines.extend(
    #            [
    #                f"{file}:{index}:{line.strip('\n')}"
    #                for x in search_terms
    #                for index, line in enumerate(reader)
    #                if not re.search(rf"\b{x}\b", line)
    #            ]
    #        )
    #    else:
    #        match_lines.extend(
    #            [
    #                f"{file}:{line.strip('\n')}"
    #                for x in search_terms
    #                for line in reader
    #                if not re.search(rf"\b{x}\b", line)
    #            ]
    #        )
    # else:
    #    if show_line_numbers:
    #        match_lines.extend(
    #            [
    #                f"{file}:{index}:{line.strip('\n')}"
    #                for x in search_terms
    #                for index, line in enumerate(reader)
    #                if re.search(rf"\b{x}\b", line)
    #            ]
    #        )
    #    else:
    #        match_lines.extend(
    #            [
    #                f"{file}:{line.strip('\n')}"
    #                for x in search_terms
    #                for line in reader
    #                if re.search(rf"\b{x}\b", line)
    #            ]
    #        )"""

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    # if len(match_lines) == 0:
    #    exit_code = 1
    # else:
    #    exit_code = 0

    # return (exit_code, match_lines)

    """Also, få bort alla nested ifs, måste finnas snyggare sätt att modifiera en loop om ett condition uppfylls."""


if __name__ == "__main__":
    pass
