# Uppgift 9 - Skapa CLI-verktyget "greppo" för textfiltrering

## <a name='Syfte'></a>Syfte

Syftet med den här uppgiften är att ge praktisk erfarenhet av att utveckla ett
kommandoradsverktyg i Python som hanterar filinläsning, textbearbetning, och
avancerad argumenthantering, vilket förbereder för skapandet av effektiva och
användarvänliga skript och verktyg för dataanalys och automatisering.

<!-- vscode-markdown-toc -->

- [Syfte](#Syfte)
- [Förberedelser](#Frberedelser)
  - [Förberedelser](#Frberedelser-1)
- [Beskrivning](#Beskrivning)
  - [Detaljer](#Detaljer)
    - [Tekniska Krav:](#TekniskaKrav:)
    - [greppo.py](#greppo.py)
    - [greppo_logic.py](#greppo_logic.py)
    - [Exempel](#Exempel)
  - [Inlämningsinstruktioner](#Inlmningsinstruktioner)
- [Anteckningar](#Anteckningar)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Frberedelser'></a>Förberedelser

### <a name='Frberedelser-1'></a>Förberedelser

Innan du börjar med uppgiften bör du fokusera på följande tre viktiga
förberedelser:

1. **Förståelse för filhantering**: Bekanta dig med hur man [öppnar, läser, och hanterar filer](https://docs.python.org/3/tutorial/inputoutput.html#tut-files)
   i Python. Detta är en grundläggande färdighet för uppgiften eftersom du
   kommer att behöva läsa innehållet i en eller flera filer för att söka efter
   specifika textsträngar. Se till att du förstår hur man använder
   `open`-funktionen och kontextmanagers (`with`-satsen) för att effektivt
   hantera filer.

2. **Bli bekant med argparse-modulen**: Eftersom ditt CLI-verktyg kommer att ta
   emot argument och flaggor från användaren, är det viktigt att du förstår hur
   man använder [`argparse`-modulen](https://docs.python.org/3/library/argparse.html) för att tolka dessa kommandoradsargument. Gå igenom [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
   eller åtminstone läs igenom den övergripande dokumentationen för att få en
   bra överblick över hur man definierar argument, hur man skapar en parser, och
   hur man hämtar argumentvärdena i ditt program.

3. **Grundläggande kunskap om strängmanipulation och sökning**: Eftersom
   uppgiften innebär att söka efter och eventuellt modifiera textsträngar, är
   det viktigt att du är bekväm med strängmanipulation i Python. Detta
   inkluderar att veta hur man utför operationer som att söka efter substrängar,
   jämföra strängar, och använda strängmetoder för att bearbeta text.

Genom att fokusera på dessa tre förberedelser kommer du att lägga en stark grund
för att framgångsrikt slutföra uppgiften och skapa ett användbart och effektivt
CLI-verktyg.

## <a name='Beskrivning'></a>Beskrivning

Skapa CLI-verktyget greppo för att söka efter textsträngar i filer. Användare
specificerar söksträngar och filer, och greppo visar matchande rader.

### <a name='Detaljer'></a>Detaljer

Kommandots utskrifter när det skriver ut något ska motsvara hur `grep -Hv`
fungerar. Det är sådana utskrifter i exemplen som följer.

#### <a name='TekniskaKrav:'></a>Tekniska Krav:

1. **Argumenthantering med argparse**: Använd `argparse`-modulen för att hantera
   kommandoradsargument.
2. **Funktionsuppdelning**: Dela upp programmet i två filer: `greppo.py` för
   kommandoradsinterfacing och `greppo_logic.py` för själva söklogiken.

#### <a name='greppo.py'></a>greppo.py

- Filen `greppo.py` ska hantera användarinput och skriva ut resultatet av
  sökningen.
- Använd `argparse` för att tolka följande argument:
  - Filnamn (en eller flera).
  - `--search` för söksträngar, kan anges flera gånger.
  - `-n` eller `--line-number` för att inkludera radnummer i utskriften.
  - `-v` eller `--invert-match` för att invertera sökningen (matcha rader som
    inte innehåller söksträngarna).
  - `-q`, `--quiet`, eller `--silent` för att undertrycka utskrift (endast
    exitkod).
- Funktionen `main` ska samla argumenten och anropa en funktion från
  `greppo_logic.py` med dessa.

#### <a name='greppo_logic.py'></a>greppo_logic.py

- Skapa en funktion `greppo_logic(search_terms, filenames, invert_match)`:
  - `search_terms`: Lista med strängar att söka efter.
  - `filenames`: Lista med filnamn att söka i.
  - `invert_match`: Boolsk flagga för om sökningen ska inverteras.
  - Funktionen ska returnera en tupel `(exit_code, matches)`, där `exit_code` är
    0 om någon match hittades (eller vid inverterad sökning, om någon rad inte
    matchade), annars 1. `matches` är en lista med strängar som representerar de
    matchande raderna.

#### <a name='Exempel'></a>Exempel

1. **Sök efter en sträng i en fil**

   ```bash
   $ python greppo.py --search "error" myfile.txt
   myfile.txt:this is an error
   myfile.txt:another error line
   ```

   - Förväntad utskrift: Visar alla rader som innehåller "error".
   - Förväntad exitkod: `0` om minst en rad innehåller "error", annars `1`.

2. **Sök efter flera strängar i flera filer med radnummer**

   ```bash
   $ python greppo.py --search "error" --search "warning" -n myfile.txt anotherfile.txt
   myfile.txt:2:this is an error
   myfile.txt:3:another error line
   anotherfile.txt:1:error something something
   anotherfile.txt:3:syntax error
   anotherfile.txt:4:yet another error
   ```

   - Förväntad utskrift: Visar alla rader som innehåller "error" eller
     "warning", inklusive radnummer.
   - Förväntad exitkod: `0` om minst en rad matchar sökningen, annars `1`.

3. **Inverterad sökning**

   ```bash
   $ python greppo.py --search "error" -v myfile.txt
   myfile.txt:warning something something
   myfile.txt:and a warning line
   myfile.txt:
   ```

   - Förväntad utskrift: Visar alla rader som **inte** innehåller "error".
   - Förväntad exitkod: `0` om minst en rad **inte** innehåller "error" (och
     därmed matchar den inverterade sökningen), annars `1`.

4. **Tyst läge**

   ```bash
   $ python greppo.py --search "error" -q myfile.txt
   ```

   - Ingen utskrift förväntas p.g.a. tyst läge.
   - Förväntad exitkod: `0` om minst en rad innehåller "error", annars `1`.

### <a name='Inlmningsinstruktioner'></a>Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. **Använda Github Classroom:**

   - Du har troligen redan accepterat uppgiften via en länk som tillhandahålls
     av utbildaren och gjort en `git clone` av det tilldelade repositoriet då du
     läser denna text. Det är i detta repository du kommer att hitta `README.md`
     med ytterligare instruktioner.

2. **Modifiera `greppo.py` och `greppo_logic`:**

   - Din lösning på uppgiften ska skrivas i `greppo.py` samt `greppo_logic`.

3. **Lämna in med Git:**

   - När du är klar med din uppgift, använd kommandona `git add .`, `git commit`
     följt av `git push` för att skicka in dina ändringar till GitHub.

4. **Automatiska "smoke tests":**

   - Efter att du har pushat din kod kommer automatiska "smoke tests" att köras.
     Dessa tester indikeras med en grön bock om de passerar, eller ett rött
     kryss om de misslyckas. Om du får ett rött kryss, är det viktigt att du
     klickar dig fram i GitHub tills du kan se varför testerna inte passerade.

5. **Feedback och granskning från utbildaren:**

   - Om dina tester passerar med en grön bock, kan du invänta feedback från din
     utbildare. Utbildaren kan antingen sätta "Request Changes" om ytterligare
     förändringar behövs, eller "approve" om uppgiften är godkänd som den är.
     Det är viktigt att du inväntar någon av dessa innan du väljer Merge.
   - Vid "Request Changes" är det viktigt att noggrant granska feedbacken och
     göra de nödvändiga justeringarna baserat på utbildarens anvisningar för att
     säkerställa att din uppgift uppfyller alla krav.
   - Efter att utbildaren har gjort "Approve" på din inlämning, får du göra en
     "Merge" av din "Feedback"-pull request, men inte förrän ett godkännande har
     erhållits.

6. **Initiera diskussioner i "Feedback"-pull requesten:**

   - Som student är du uppmuntrad att aktivt delta i processen genom att
     initiera diskussioner i din "Feedback"-pull request. Detta är en viktig del
     av inlärningsprocessen, där du kan ställa frågor, begära förtydliganden
     eller diskutera lösningar och feedback med din utbildare. Att engagera sig
     i dessa diskussioner ger dig möjlighet att djupare förstå uppgiftens krav
     och förbättra din kod baserat på interaktionen.

## <a name='Anteckningar'></a>Anteckningar

- **Exitkod 0** indikerar vanligtvis att programmet har utfört sin uppgift
  framgångsrikt och att de önskade villkoren uppfyllts (t.ex., minst en
  matchning hittades).
- **Exitkod 1** används för att signalera att programmet har utfört sin uppgift,
  men de önskade villkoren inte uppfyllts (t.ex., ingen matchning hittades),
  eller att ett fel inträffade.
