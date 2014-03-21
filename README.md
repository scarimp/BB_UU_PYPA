BB_UU_PYPA
==========

Parser in Python per estrazioni codici scuole dai  Bollettini Ufficiali  forniti dal Miur.


1
MergRtfFile.py
Input: una cartella contenente più file sorgente .rtf ('RegDati/In')
output: un unico file .rtf contenente tutti i dati dei file sorgente ('RegDati/Out/All.rtf)
------------------------------
2
Da file All.rtf a All.txt 
Basta un copia incolla da WordPad a file di testo ('RegDati/Out/All.txt)
------------------------------
3
All_csv.py
Input: = RegDati/Out/All.txt
output: RegDati/Out/All.csv

Produce un file con una riga di testata seguita da una riga per scuola con i campi:
Prov, Comu, Dist,
Scuola, più due campi estratti da Scuola: CodScuola e CodSezAss1
Indirizzo (riga successiva alla scuola, talvolta NON è un indirizzo),
SezioneAssociata, più un campo estratto da SezioneAssociata: CodSezAss2
<SEDE AMMINISTRATIVA / SEDI CARCERARIE / SEZIONI ASSOCIATE / altro>: Con
4
UniqueLine.py
Input: = RegDati/Out/All.csv
output: RegDati/Out/AllUnique.csv

Rende uniche le linee del file 
------------------------------
5
TestFromUnique.py	Analizza i dieci campi presenti in AllUnique.csv
Input: = RegDati/Out/AllUnique.csv
output: RegDati/Out/testUnique.csv

Per controllare l' estrazione di ScuolaPrincipale e ConSezioniAssociate
------------------------------
6
ExtractFromUniqueA.py
Input: = RegDati/Out/AllUnique.csv
output: RegDati/Out/ExtractA.csv

File con una riga di testata seguita da una riga per scuola con i campi:
"Prov","Comu","Dist","CodScuola","ScAssiciataA","Indirizzo","ScPrincipaleCon"
------------------------------
6 bis
ExtractFromUniqueB.py	
Input: = RegDati/Out/AllUnique.csv
output: RegDati/Out/ExtractB.csv

File con una riga di testata seguita da una riga per scuola con i campi:
"Prov","Comu","Dist","CodScuola","Descrizione","ScAssiciataA","Indirizzo","ScPrincipaleCon"
------------------------------
7
UniqueCodA.py		Da: FileIn = '../LuzioCC/RegDati/Out/ExtractA.csv'	A: FileOut = FileIn.replace("ExtractA.csv","ExtractUniCodA.csv")
Input: = RegDati/Out/ExtractA.csv
output: RegDati/Out/ExtractUniCodA.csv

Rende unici i CodScuola. Se il codice si ripete prende la prima linea che trova.
------------------------------
7 bis
UniqueCodB.py		Da: FileIn = '../LuzioCC/RegDati/Out/ExtractB.csv'	A: FileOut = FileIn.replace("ExtractB.csv","ExtractUniCodB.csv")
Input: = RegDati/Out/ExtractB.csv
output: RegDati/Out/ExtractUniCodB.csv

Rende unici i CodScuola. Se il codice si ripete prende la prima linea che trova.

