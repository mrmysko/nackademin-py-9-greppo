# Extra - Relative filepaths? ~, ., ..?
# Extra - -r flag for recursive filesearch?

# Bug - --search "" and --search . produces some weird results.

# Ok, buggen med "" är att "" matchar en tom rad, och sen byts den ut till...en annan tom rad?
# Den orginella tomma raden är 0 bytes, men "" raden är 23 bytes.
# Så, den matchar ok, men kan man ha en dict med nyckeln ""?
# If-satsen under lägger till alla rader för att any() blir true i varje loop.

"""Punkt-buggen - I rader med punkt matchar . alla karaktärer på nått sätt och byter ut allt till .
    Men hur? \b.\b borde vara 1 char-wordbound?
    Ger upp på det här, ett match pattern på f'\b\.\b' hade matchat bara en punkt, men då förstörs andra saker.
    Blir för mycket conditionals så tillåter inte en punkt som sökterm itället.
    Grep hanterar en punkt som en char och matchar allt, verkar dumt tbh."""

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

    # Special case, dont allow a dot as search term.
    [search_terms.remove(term) for term in search_terms if term == "."]

    match_lines = list()

    for file in filenames:
        try:
            with open(file, "r", encoding="utf-8") as fp:
                reader = fp.readlines()
        except FileNotFoundError:
            continue

        for index, line in enumerate(reader, start=1):

            search_word_dict = dict()
            line = line.strip()

            for term in search_terms:

                # Flip keys to True if match is found.
                # Match only full words. "for" in "fortnite" == False
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
                if not any(search_word_dict.values()) and len(line) > 1:
                    match_lines.append(full_line)

            elif any(search_word_dict.values()):
                match_lines.append(full_line)

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
