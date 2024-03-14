#!/usr/bin/env python
# Skriv endast definitioner här på denna indenteringsnivå! Det är viktigt att du
# namnger funktioner, klasser och variabler exakt med de namn som står i
# beskrivningen.
import argparse

# import greppo_logic


def main():
    # Skriv din argparse-kod här samt anropet till greppo_logic-funktionen i
    # greppo_logic.py här.
    parser = argparse.ArgumentParser(
        prog="Greppo", description="A python implementation of grep -Hv"
    )
    parser.add_argument("files", nargs="+", help="Space-separated filenames")
    parser.add_argument("--search", nargs="+", help="Space-separated search-strings.")
    parser.add_argument("-n", "--line-number", help="Show line-numbers.")
    # parser.add_argument("-v", "--invert-match", help="Invert selection.")
    # parser.add_argument("-q", "--quiet", "--silent", help="Only show exit-code.")

    test = parser.parse_args()

    print(parser)
    print(test)
    # greppo_logic.nånfunktion(typ args)


if __name__ == "__main__":
    main()  # Anropar main-funktionen när skriptet körs direkt.

    # Eftersom den här if-satsen är upptagen av att anropa main-funktionen så
    # får du skriva din testkod på annat vis. Se [test.py](test.py). Funktionen
    # greppo_logic i filen greppo_logic.py kan däremot testas "som vanligt" inom
    # filens if-sats.
