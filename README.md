# Uppgift 9 - Skapa CLI-verktyget "greppo" för textfiltrering

# Syfte

I den här uppgiften kommer du att skapa ett terminalverktyg med Python. Du
kommer att lära dig hur man läser filer, bearbetar text och använder `argparse`
för att hantera kommandoradsparametrar. Det här är användbart för att skapa
program som hjälper till med dataanalys och automatisering.

# Inför uppgiften

För att bli redo att lösa uppgiften bör du lära dig följande:

1. Läsa in filer

   - Lär dig hantera filer i Python. Det inkluderar att öppna en fil, läsa
     innehållet rad för rad och sedan stänga filen. Python-dokumentationen har
     avsnitt om filhantering som är bra att börja med.

2. Söka i strängar

   - Bekanta dig med hur man söker efter specifika ord eller fraser inom
     strängar i Python. Det finns flera metoder för detta, inklusive användning
     av `in`-operatorn, reguljära uttryck eller strängmetoder som `find()` och
     `index()`.

3. Använda argparse
   - Argparse är ett bibliotek i Python för att hantera kommandoradsargument.
     Det gör det möjligt att skapa användarvänliga kommandoradsgränssnitt, och
     det är centralt för ditt skript. Gå igenom den officiella dokumentationen
     och Argparse-tutorialen för att förstå hur du definierar argument, hur du
     läser in dessa argument i ditt program, och hur du använder dem.

Att ha en god förståelse för dessa områden kommer att ge dig ett bra utgångsläge
för att lösa uppgiften. Använd Python Library Reference och de officiella
tutorialsen för att lära dig mer om dessa ämnen.

# Beskrivning

Skapa ett CLI verktyg vid namn `greppo.py` för att söka efter textsträngar i
filer.

## Skriptet `greppo.py`

### Argument

- Positionella argument
  - Ett eller flera filnamn
- Optioner
  - `--search S` ger träff på strängen `S` i filerna. Optionen kan ges flera
    gånger och ger då träffar på alla söksträngarna.
  - `-n` eller `--line-number` visar radnummer för varje träff enligt formatet:
    `filnamn:R:T` där `R` är radnumret och `T` radens innehåll.
  - `-v` eller `--invert-match` inverterar sökningen så att träffar istället ges
    för de rader som inte matchar någon söksträng.
  - `-q`, `--quiet`, eller `--silent` stänger av utskrifter, men fortfarande ges
    exit code.

### Utskrift

Den enda utskrift som ges är för träffar är enligt formatet `F:R:T` där `F` är
filnamnet, `R` är radnumret om flaggan för radnummer angavs och `T` radens
innehåll. Förutom detta så skrivs ingen ut alls.

Om flaggan för att stänga av utskrifter angavs så ska inget skrivas ut.

### Exit code

`0` om sökningen gav någon träff, annars `1`.

### Exempel

```bash
$ cat filnamn1
one
two
three
four
five
$ cat filnamn2
boat
car
airplane
helicopter
rocket
$ python greppo.py --search one --search two filnamn1
filnamn1:one
filnamn1:two
$ python greppo.py --search o filnamn1
filnamn1:one
filnamn1:two
filnamn1:four
$ python greppo.py --search o -n filnamn2
filnamn2:1:boat
filnamn2:4:helicopter
filnamn2:5:rocket
$ python greppo.py --search e -nv filnamn1 filnamn2
filnamn1:2:two
filnamn1:4:four
filnamn2:1:boat
filnamn2:2:car
```

## Använd de två filerna `greppo.py` och `greppo_logic.py`

Verktyget delas upp i två delar för att hålla kodstrukturen klar och tydlig:
skriptfilen `greppo.py` och modulen `greppo_logic.py`.

`greppo.py` är huvudfilen som användaren interagerar med. Den använder
`argparse` för att tolka och hantera användarinput i form av
kommandoradsparametrar. Dess detaljär är beskrivna ovan. Huvudsyftet med filen
är att fungera som en bro mellan användaren och programmets logik, utan att
själv dyka ner i detaljerna av textbearbetningen.

`greppo_logic.py` innehåller logiken för greppo och är fokuserad på att
genomföra de specifika uppgifterna. Det är där texten i filerna söks igenom
utifrån de olika och resultatraderna genereras. Den är oberoende av hur
programmet körs, vilket gör det möjligt att återanvända koden i olika
sammanhang. Dess detaljer är beskrivna nedan.

## Funktionen `greppo_logic`

- Signatur: `greppo_logic(search_terms, filenames, invert_match, show_linenumbers)`

  - `search_terms`: Lista med strängar att söka efter.
  - `filenames`: Lista med filnamn att söka i.
  - `invert_match`: Boolsk flagga för om sökningen ska inverteras.

- Utskrift: Inget!

- Returvärde: `(exit_code, matches)`

  - `exit_code` är `0` om någon match hittades (eller vid inverterad sökning, om
    någon rad inte matchade), annars `1`.
  - `matches` är en lista med strängar som representerar de matchande raderna.

Det är viktigt att notera att flaggan som gör att skriptet inte ska ge någon
utmatning inte hanteras i `greppo_logic`. Vi gör så för att dela upp ansvaret en
del mellan vad filerna.

### Exempel

Innehållet i filerna `filnamn1` och `filnamn2` kan ses i de tidigare exemplen
för hela skriptet.

1. Anrop: `greppo_logic(["one", "two"], ["filnamn1"], False, False)`

   - Utskrift: Inget!

   - Returvärde: `(0, ["filnamn1:one", "filnamn1:two"])`

2. Anrop: `greppo_logic(["o"], ["filnamn1"], False, False)`

   - Utskrift: Inget!

   - Returvärde: `(0, ["filnamn1:one", "filnamn1:two", "filnamn1:four"])`

3. Anrop: `greppo_logic(["o"], ["filnamn2"], False, True)`

   - Utskrift: Inget!

   - Returvärde: `(0, ["filnamn2:1:boat", "filnamn2:4:helicopter", "filnamn2:5:rocket"])`

4. Anrop: `greppo_logic(["e"], ["filnamn1", "filnamn2"], True, True)`

   - Utskrift: Inget!

   - Returvärde: `(0, ["filnamn1:2:two", "filnamn1:4:four", "filnamn2:1:boat", "filnamn2:2:car"])`

5. Anrop: `greppo_logic(["flower"], ["filnamn1", "filnamn2"], False, True)`

   - Utskrift: Inget!

   - Returvärde: `(1, [])`

### Tips

- `grep` fungerar som ett praktiskt exempel på vad vi vill uppnå. `greppo.py`
  skiljer sig genom att det tar emot sökord med optionen `--search`. Övriga
  optioner som `greppo.py` ska hantera är sådana `grep` också förstår.
- För att göra uppgiften enklare, dela upp den i två delar: hantera kommandon
  med `argparse` och utför sökningen i filerna. Lös dessa steg för sig och
  kombinera dem sedan.
- Använd [sys.exit](https://docs.python.org/3/library/sys.html#sys.exit) för att
  avsluta med en statuskod.

# Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. Använda Github Classroom och klona ditt uppgiftsrepository:

   - Om du läser det här i `README.md` har du redan börjat med uppgiften genom
     att klicka på en länk från din utbildare och klonat ditt
     uppgiftsrepository.

2. Lös uppgiften:

   - Din lösning ska skapas genom att ändra i de filer som nämns i
     uppgiftsbeskrivningen. Följ instruktionerna där för var du ska lägga in din
     kod.

3. Lämna in med Git:

   - När du är klar, använd `git add .`, `git commit` och sedan `git push` för
     att skicka in ditt arbete till GitHub.

4. Automatiska "smoke tests":

   - När du skickar in din kod körs "smoke tests" automatiskt. En grön bock
     betyder att de gick igenom, medan ett rött kryss betyder att något gick
     fel. Om du får ett rött kryss, kolla på GitHub varför testerna
     misslyckades.

5. Feedback och granskning från utbildaren:

   - När dina "smoke tests" får en grön bock väntar du på feedback från din
     utbildare. Utbildaren kan vilja att du ändrar något eller godkänna din
     uppgift direkt. Vänta med att slå ihop din kod ("Merge") tills uppgiften är
     godkänd.

   - Om utbildaren vill att du ändrar något, läs noggrant och gör de ändringar
     som behövs.

   - När uppgiften är godkänd och det inte finns mer att diskutera, kan du göra
     "Merge" med din "Feedback"-pull request. Men, vänta alltid tills du har
     fått ett godkännande.

6. Starta diskussioner i "Feedback"-pull requesten:

   - Utnyttja möjligheten att diskutera uppgiftens kod i din "Feedback"-pull
     request. Det är ett bra sätt att lära sig genom att ställa frågor, be om
     förklaringar eller diskutera lösningar och respons med din utbildare.

# Anteckningar

För att tydliggöra arkitekturen ytterligare så hade vi kunnat:

1. Separera användarinteraktion från logik

   - Låt `greppo.py` hantera filinläsningen och interaktionen med användaren.
     Denna fil ska öppna och läsa innehållet i filerna, och sedan skicka den
     inlästa datan till `greppo_logic.py`.

2. Rena datatyper i `greppo_logic`

   - Modifiera `greppo_logic` så att den returnerar data i en mer generell form,
     som inte är bunden till hur resultatet ska visas. Använd `True` och `False`
     istället för 0 och 1 för att ange sökresultat, och returnera resultat som
     en lista av tuplar med radnummer och radinnehåll, exempelvis `[(radnummer, radinnehåll)]`.

3. Låt `greppo.py` bestämma presentation

   - `greppo.py` ska bestämma hur resultatet presenteras för användaren baserat
     på datan från `greppo_logic`. Detta gör det lättare att ändra
     presentationen utan att påverka logiken.

Genom att tydligt skilja på "kommunikation med användaren" och "det programmet
ska göra", ökar du kodens återanvändbarhet och gör det enklare att underhålla
och utveckla vidare.

Eftersom uppgiften redan är satt och inte kommer att ändras, erbjuder de
föreslagna förbättringarna ovan ett bra tillfälle för reflektion och diskussion
i pull requesten.
