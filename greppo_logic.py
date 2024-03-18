# Extra - Relative filepaths? ~, ., ..?
# Extra - -r flag for recursive filesearch?

# Bug - --search "" and --search . produces some weird results.

import re
import os


def greppo_logic(
    search_terms: list,
    filenames: list,
    invert_match: bool,
    show_line_numbers: bool,
    exact: bool,
    recursive: bool,
) -> tuple:
    """Returns lines matching strings in search_terms."""

    DEFAULT = "\033[0m"
    GREEN = "\033[92m"
    RED = "\033[0;91m"
    CYAN = "\033[94m"
    PURPLE = "\033[95m"

    match_lines = list()

    for file in filenames:
        try:
            with open(file, "r", encoding="utf-8") as fp:
                reader = fp.readlines()
        except FileNotFoundError:
            continue

        for index, line in enumerate(reader, start=1):

            search_word_dict = dict()

            # Flip keys to True if match is found.
            # Match only full words. "for" in "fortnite" == False
            for term in search_terms:
                if exact:
                    if re.search(rf"\b{term}\b", line):
                        search_word_dict[term] = True
                        line = re.sub(rf"\b{term}\b", f"{RED}{term}{DEFAULT}", line)

                # Match sub-strings. "for" in "fortnite" == True
                else:
                    if term in line:
                        search_word_dict[term] = True
                        line = re.sub(term, f"{RED}{term}{DEFAULT}", line)

            # This code loops over search terms twice, once for dict and once more for regex substitution.
            # if exact:
            #    search_word_dict = {
            #        key: True for key in search_terms if re.search(rf"\b{key}\b", line)
            #    }
            #    for term in search_terms:
            #        line = re.sub(rf"\b{term}\b", f"{RED}{term}{DEFAULT}", line)
            # Match sub-strings. "for" in "fortnite" == True
            # else:
            #    search_word_dict = {key: True for key in search_terms if key in line}
            #   for term in search_terms:
            #        line = re.sub(term, f"{RED}{term}{DEFAULT}", line)

            # The full formated string to append to match_lines.
            full_line = f"{PURPLE}{file}{CYAN}:{DEFAULT}{GREEN + str(index) + CYAN + ':' + DEFAULT if show_line_numbers else ''}{line.strip()}"

            if invert_match:

                # Returns False if any value in search_word_dict is True.
                if not any(search_word_dict.values()) and len(line.strip()) > 1:
                    match_lines.append(full_line)

            elif any(search_word_dict.values()):
                match_lines.append(full_line)

    # Why would invert return a 1 on matches? Isnt exit-code "decoupled" from logic? A '1' signifies an error or no matches tbh.
    # Anything in any(match_lines) returns True, and int(True) == 1, since we want to return 0 on matches tho we can do "not any()" which reverses it.
    return (int(not any(match_lines)), match_lines)


if __name__ == "__main__":
    pass


"""def traverse_filenames(filenames: list):
        for file in filenames:
            is os.path.isdir(file):
                traverse_filenames(<lista med filenames i file diren>)
        os.path.isdir(file)
        return filenames"""
