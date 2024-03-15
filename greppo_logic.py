# Todo - Error-handling
    # Error states:
    # File not found.
    # Empty search_terms. Should no search_terms match nothing? Should the inversion of that match everything?

# Extra - Color search_terms?
# Extra - Relative filepaths? ~, ., ..?
# Extra - -r flag for recursive filesearch?

# Todo - Lines with multiple matches repeat...use a set?

import re
from collections import Counter


def greppo_logic(search_terms, filenames, invert_match: bool, show_line_numbers: bool) -> tuple:
    """Returns lines matching strings in search_terms."""

    match_lines = list()

    # This evaluates to True if search_terms is not empty...but is it more correct to do len(search_terms) >= 1 for more readability?
    if search_terms:
        pass
    else:
        search_terms = ''

    for file in filenames:
        try:
            with open(file, "r", encoding="utf-8") as fp:
                reader = fp.readlines()
        except FileNotFoundError:
            continue
            
        # This is not readable tbh.
        for index, line in enumerate(reader):
            if invert_match:

                    # Reset search_word tracker.
                    search_word_dict = dict((i, False) for i in search_terms)

                    # Flip keys to True if match is found.
                    search_word_dict = {key:True for key in search_word_dict.keys() if re.search(rf"\b{key}\b", line)}

                    # Line above is equivalent to:
                    #for key in search_word_dict.keys():
                    #    # Returns a match object. True if a match is found.
                    #    if re.search(rf"\b{key}\b", line):
                    #        search_word_dict[key] = True

                    # Returns False if any value in search_word_dict is True. Check length of string to not add empty strings. (\n counts as a char)
                    if not any(search_word_dict.values()) and len(line) > 1 and line not in match_lines:
                        match_lines.append(rf"{file}:{str(index) + ":" if show_line_numbers else ''}{line.strip()}")

            else:
                print("LINE: ", line.strip())
                print("MATCH: ", match_lines)
                for i in search_terms:
                    if line.strip() in match_lines:
                        print("TRUE")
                    if re.search(rf"\b{i}\b", line):
                        match_lines.append(f"{file}:{str(index) + ":" if show_line_numbers else ''}{line.strip('\n')}")
                #match_lines.extend(
                #    [
                #        f"{file}:{str(index) + ":" if show_line_numbers else ''}{line.strip('\n')}"
                #        for x in search_terms
                #        if re.search(rf"\b{x}\b", line) and line 
                #    ]
                #)

    """It's never gonna match...because .strip() changes the string. And match_lines has the filename etc. in it."""

    """I guess this is needed because the list comprehension only checks the validity on the first loop or something?"""
    """Removing repeat lines from match_lines"""
    # .count() vs Counter https://stackoverflow.com/a/23909767
    #match_count = Counter(match_lines)
    #for key, value in match_count.items():
    #    if value != 1:
    #        match_lines.remove(key)

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    if len(match_lines) == 0:
        exit_code = 1
    else:
        exit_code = 0

    return (exit_code, match_lines)


if __name__ == "__main__":
    pass
