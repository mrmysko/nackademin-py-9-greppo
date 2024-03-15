#!/usr/bin/env python

# Skriv endast definitioner här på denna indenteringsnivå! Det är viktigt att du
# namnger funktioner, klasser och variabler exakt med de namn som står i
# beskrivningen.
import argparse
from greppo_logic import greppo_logic


def main():
    # Skriv din argparse-kod här samt anropet till greppo_logic-funktionen i
    # greppo_logic.py här.
    parser = argparse.ArgumentParser(
        prog="greppo.py", description="A python implementation of grep -Hv"
    )
    parser.add_argument("files", nargs="+", help="Space-separated filenames.")
    parser.add_argument("--search", action="append", help="string to search for.")
    parser.add_argument(
        "-n", "--line-number", help="show line-numbers.", action="store_true"
    )
    parser.add_argument(
        "-v", "--invert-match", help="invert selection.", action="store_true"
    )
    # parser.add_argument("-q", "--quiet", "--silent", help="Only show exit-code.")

    args = parser.parse_args()

    matches = greppo_logic(args.search, args.files, args.invert_match, args.line_number)

    if matches[0] != 0:
        print("No matches found.")
    else:
        for i in matches[1]:
            print(i)


if __name__ == "__main__":
    main()  # Anropar main-funktionen när skriptet körs direkt.

    # Eftersom den här if-satsen är upptagen av att anropa main-funktionen så
    # får du skriva din testkod på annat vis. Se [test.py](test.py). Funktionen
    # greppo_logic i filen greppo_logic.py kan däremot testas "som vanligt" inom
    # filens if-sats.
