# Todo - Error-handling - FIXED
    # Error states:
    # File not found.
    # Empty search_terms. Should no search_terms match nothing? Should the inversion of that match everything?
# Todo - Lines with multiple matches repeat - FIXED

# Extra - Color search_terms?
# Extra - Relative filepaths? ~, ., ..?
# Extra - -r flag for recursive filesearch?

# Refactoring - Do I actually need a dict to keep track of matches in the invert case?...If even one value is True, break that iteration without an append.

import re


def greppo_logic(search_terms, filenames, invert_match: bool, show_line_numbers: bool) -> tuple:
    """Returns lines matching strings in search_terms."""

    match_lines = list()

    # Handles empty search_terms without raising an exception.
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
                full_line = f"{file}:{str(index) + ":" if show_line_numbers else ''}{line.strip('\n')}"
                for i in search_terms:
                    if re.search(rf"\b{i}\b", line) and full_line not in match_lines:
                        match_lines.append(full_line)

                #match_lines.extend(
                #    [
                #        f"{file}:{str(index) + ":" if show_line_numbers else ''}{line.strip('\n')}"
                #        for x in search_terms
                #        if re.search(rf"\b{x}\b", line) and line 
                #    ]
                #)

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    if len(match_lines) == 0:
        exit_code = 1
    else:
        exit_code = 0

    return (exit_code, match_lines)


if __name__ == "__main__":
    pass
