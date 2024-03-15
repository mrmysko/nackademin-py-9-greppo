# Todo - Error-handling
# Todo - Less ifs

import re


def greppo_logic(search_terms, filenames, invert_match: bool, show_line_numbers: bool):
    """Returns lines matching items in search_terms."""

    match_lines = list()

    for file in filenames:
        with open(file, "r", encoding="utf-8") as fp:
            reader = fp.readlines()

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
                        match_lines.append(rf"{file}:{str(index) + ":" if show_line_numbers else ''}:{line.strip()}")
                        """Now, hur kokar jag ner den här i en list comprehension?"""

            # This is not readable tbh.                
            # If note invert match, easier.
            else:
                match_lines.extend(
                    [
                        f"{file}:{str(index) + ":" if show_line_numbers else ''}{line.strip('\n')}"
                        for x in search_terms
                        for index, line in enumerate(reader)
                        if re.search(rf"\b{x}\b", line)
                    ]
                )

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    if len(match_lines) == 0:
        exit_code = 1
    else:
        exit_code = 0

    return (exit_code, match_lines)


if __name__ == "__main__":
    pass
