import argparse
import greppo_logic

def main():
   
    parser = argparse.ArgumentParser()    
    parser.add_argument('filename', nargs='*') 
    parser.add_argument('--search', action='append') 
    parser.add_argument('-n', '--line-number',action='store_true')
    parser.add_argument('-v', '--invert-match',action='store_true')
    parser.add_argument('-q', '--quiet', '-silent', action='store_true')
    
    args = parser.parse_args()
    
    filename=  args.filename
    search_term = args.search
    invert_match = args.invert_match 
    show_linenumber = args.line_number
    
    matches, exit_code = greppo_logic.greppo_logic(search_term,filename,invert_match,show_linenumber) 
    
    if args.quiet:
        print(exit_code)
    else:
        for match in matches:
            print(match)
        

if __name__ == "__main__":
    main()  # Anropar main-funktionen när skriptet körs direkt.

    # Eftersom den här if-satsen är upptagen av att anropa main-funktionen så
    # får du skriva din testkod på annat vis. Se [test.py](test.py). Funktionen
    # greppo_logic i filen greppo_logic.py kan däremot testas "som vanligt" inom
    # filens if-sats.
