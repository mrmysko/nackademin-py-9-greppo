# Skriv endast definitioner här på denna indenteringsnivå! Det är viktigt att du
# namnger funktioner, klasser och variabler exakt med de namn som står i
# beskrivningen.


def greppo_logic(search_terms, filenames, invert_match):
    # Collect matching lines in some thing...

    """for file in filenames:
    with open(file, 'r', encoding=utf-8) as fp:
        # read lines, looking for lines, or if inverted look for not lines
        use .readlines() and an iterator to keep track of which lines contain matches?
        save iterator and line in like a tuple or something?"""

        # saves tuple of index and line with match.
        for index, line in enumerate(fp.readlines()):
            for item in search_terms:
                if item in line:
                    match.append((index, line))

    print("Greppo logic.")


if __name__ == "__main__":
    # Här kan du skriva testkod som bara körs när du kör filen direkt och inte
    # när den importeras som modul i en annan fil.
    #
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
    #
    # Exempel:
    # minklass = Klass()
    # print(klass.leet("hejsan")
    pass  # Ta bort denna rad när du skriver din kod
