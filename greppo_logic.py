import os
import sys

def greppo_logic(search_terms, filenames, invert_match, show_linenumbers):
    
    matches = []
    exit_code = 1


    for file in filenames: # Loopar file genom filenames
        if os.path.exists(file): # Kollar om filen finns (True or False)
            with open(file, 'r') as content: # Öppnar filen som 'content'
                
                for index, line in enumerate(content, start=1): #Ger filen indexering som startar på 1
                    
                    line=line.strip() #För att listan matches inte ska få med end och whitespaces

                    if search_terms:
                        for search in search_terms:
                            
                            if invert_match: #Hantering vid inventering
                                    if search not in line: #kollar om sökorden finns i raderna
                                        if show_linenumbers: # Kollar om show_linenumbers är True
                                            matches.append(f"{file}:{index}:{line}") 
                                            exit_code = 0
                                            
                                        else:
                                            matches.append(f"{file}:{line}")
                                            exit_code = 0
                                            

                            else: #Hanterar sökningen i fallen där den inte ska inverteras. 
                                if search in line:    

                                    if show_linenumbers:

                                        matches.append(f"{file}:{index}:{line}")
                                        exit_code = 0

                                    else: 
                                        matches.append(f"{file}:{line}")
                                        exit_code = 0
                    
                return matches, exit_code

        else:
            print("File does not exist")

                            
                            
                            
                            
                                
                

                                  
                                

                            
                            
                            
                                    


                                            
                                        
                                
                
                    
                
        


            
                
    
    
    
    
    
    
    #2: SÖK EFTER EN STRÄNG I EN FIL

    #3: SÖKA EFTER FLERA STRÄNGAR I FLERA FILER MED RADNUMMER

    #4: VISA ALLA RADER SOM INTE INNEHÅLLER EN VISS TEXTSTRÄNG


    
    
    
    
    
    
    
    #5: TYST LÄGE (BORDE SKRIVAS DIREKT I ARGS)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    1:  search_terms: Lista med strängar att söka efter.
    
    2:  filenames: Lista med filnamn att söka i.
    
    3:  invert_match: Boolsk flagga för om sökningen ska inverteras.
    
    4:  show_linenumbers: Boolsk flagga för om radnummer ska finnas med i resultatet.
    
    5:  Funktionen ska returnera en tupel (exit_code, matches), där exit_code är 0 om någon match hittades (eller vid inverterad sökning, om någon rad inte matchade)
    , annars 1. matches är en lista med strängar som representerar de matchande raderna.
   
     """
    
    
    
    


if __name__ == "__main__":
    greppo_logic()
