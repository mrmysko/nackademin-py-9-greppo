# Extra - Color search_terms matches red. re replace match with {red}{match}{white}?
# Extra - Relative filepaths? ~, ., ..?
# Extra - -r flag for recursive filesearch?

import re


def greppo_logic(
    search_terms,
    filenames,
    invert_match: bool,
    show_line_numbers: bool,
    exact: bool,
) -> tuple:
    """Returns lines matching strings in search_terms."""

    DEFAULT = "\033[0m"
    GREEN = "\033[92m"
    CYAN = "\033[94m"
    PURPLE = "\033[95m"

    match_lines = list()

    # Handles empty search_terms without raising an exception.
    # This evaluates to True if search_terms is not empty...but is it more correct to do len(search_terms) >= 1 for more readability?
    if search_terms:
        pass
    else:
        search_terms = ""

    for file in filenames:
        try:
            with open(file, "r", encoding="utf-8") as fp:
                reader = fp.readlines()
        except FileNotFoundError:
            continue

        # This is not readable tbh.
        for index, line in enumerate(reader, start=1):
            # The full formated string to append to match_lines.
            full_line = f"{PURPLE}{file}{CYAN}:{DEFAULT}{GREEN + str(index) + CYAN + ':' + DEFAULT if show_line_numbers else ''}{line.strip()}"

            # Flip keys to True if match is found.
            # Match only full words. "for" in "fortnite" == False
            if exact:
                search_word_dict = {
                    key: True for key in search_terms if re.search(rf"\b{key}\b", line)
                }
            # Match sub-strings. "for" in "fortnite" == True
            else:
                search_word_dict = {key: True for key in search_terms if key in line}

            if invert_match:

                # Returns False if any value in search_word_dict is True.
                if not any(search_word_dict.values()):
                    match_lines.append(full_line)

            else:
                if any(search_word_dict.values()):
                    match_lines.append(full_line)

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    # Anything in any(match_lines) returns True, and int(True) == 1, since we want to return 0 on matches tho we can do "not any()" which reverses it.
    return (int(not any(match_lines)), match_lines)

    def find_match(term, line):
        pass
        return False


if __name__ == "__main__":
    pass
