"""
File con una riga di testata seguita da una riga per scuola con i campi:
Prov, Comu, Dist,
Scuola, più due campi estratti da Scuola: CodScuola e CodSezAss1
Indirizzo (riga successiva alla scuola, talvolta NON è un indirizzo),
SezioneAssociata, più un campo estratto da SezioneAssociata: CodSezAss2
<SEDE AMMINISTRATIVA / SEDI CARCERARIE / SEZIONI ASSOCIATE / altro>: Con
"""
import re
FileIn = 'RegDati/Out/All.txt'
FileOut = FileIn.replace(".txt",".csv")
f = open(FileIn, 'r')
fOut = open(FileOut, 'w')
fOut.write('"Prov","Comu","Dist","Scuola","CodScuola","CodSezAss1","Indirizzo","SezioneAssociata","CodSezAss2","Con"'+"\n")
newline=pro=com=dis= ''
sc0=sc1=sc2=sc3=sc4=sc5=sc6= ''
indi= False
skip = 100
cont = 0
contWrite = 0
contAll = 0
for line in f:
    contAll+=1
    if line.strip() == 0: continue
  # CERCA PROVINCIA
    prov = re.match(r'^[A-Z0-9]{10}.*(PROVINCIA)\s+\w+\s+(.+)', line)
    if prov:
        if newline.count('"')== 12:
            newline = newline+',"'+sc3+'","'+sc4+'","'+sc5+'","'+sc6+'"'
            fOut.write(newline+"\n"); contWrite+=1
            sc0=sc1=sc2=sc3=sc4=sc5=sc6= ''; indi= False; dis=com= ''
        pro = prov.group(2).strip()
  # CERCA DISTRETTO
    md = re.match(r'^\b[A-Z,0-9]{10}\b.*\bDISTRETTO\b\s+(\w+)', line)
    if md:
        if newline.count('"')== 12:
            newline = newline+',"'+sc3+'","'+sc4+'","'+sc5+'","'+sc6+'"'
            fOut.write(newline+"\n"); contWrite+=1
            sc0=sc1=sc2=sc3=sc4=sc5=sc6= ''; indi= False
        dis = md.group(1).strip()
  # CERCA COMUNE
    comu = re.match(r'^\b[A-Z0-9]{10}\b.*(COMUNE)\s+\w+\s+(.+)', line)
    if comu:
        if newline.count('"')== 12:
            newline = newline+',"'+sc3+'","'+sc4+'","'+sc5+'","'+sc6+'"'
            fOut.write(newline+"\n"); contWrite+=1
            sc0=sc1=sc2=sc3=sc4=sc5=sc6= ''; indi= False
        com = comu.group(2).strip()       
  # CERCA SCUOLA        
    scuo = re.match(r'\t(\b[A-Z0-9]{10}\b).*', line)
    if scuo:
        if newline.count('"')== 12:
            newline = newline+',"'+sc3+'","'+sc4+'","'+sc5+'","'+sc6+'"'
            fOut.write(newline+"\n"); contWrite+=1
            sc0=sc1=sc2=sc3=sc4=sc5=sc6= ''; indi= False
        sc1 = scuo.group(1).strip()
        sc0 = scuo.group(0).strip().replace('"','').replace(',',''); cont+=1
        indi = True
     # CERCA SCUOLA ASSOCIATA IN RIGA -SCUOLA
        scuoAss = re.match(r'^\t(\b[A-Z0-9]{10}\b).*(\b[A-Z]{4}[0-9][A-Z0-9]{5}\b)', line)
        if scuoAss: sc2 = scuoAss.group(2).strip().replace('"','').replace(',','')
        else:       sc2 = ''
        newline = '"'+pro+'","'+com+'","'+dis+'","'+sc0+'","'+sc1+'","'+sc2+'"'
        if cont%skip == 0: print(str(cont)+' - '+str(contAll)+' - '+newline);
  # CERCA INDIRIZZO (riga successiva a scuola)
    ni = re.match(r'^\t\t.+$', line)
    if ni and indi:
        sc3 = ni.group(0).strip().replace('"','').replace(',','')
#        print('* '+sc3)
        indi = False
  # CERCA SCUOLA ASSOCIATA IN RIGA -SEZIONE ASSOCIATA
    nsa1 = re.match(r'^\t\t\bSEZIONE\b.+\bASSOCIATA\b.+(\b[A-Z0-9]{10}\b)', line)
    if nsa1:
        sc4 = nsa1.group(0).strip().replace('"','').replace(',','')
        sc5 = nsa1.group(1).strip()
#        print('** '+sc4+' - '+sc5)
  # CERCA SCUOLE ASSOCIATE IN RIGA -CON xxx : <almeno un CodScuola>
    nsan = re.match(r'^\t\t(\bCON\b\s+\b\w*\b\s+\b\w*\b).+:.+\b[A-Z]{4}[0-9][A-Z0-9]{5}\b', line)
    if nsan:
        sc6 = nsan.group(1).strip().replace('"','').replace(',','')
#        print('*** '+sc6)


    if cont == 999999: break

if newline.count('"')== 12:
    newline = newline+',"'+sc3+'","'+sc4+'","'+sc5+'","'+sc6+'"'
    fOut.write(newline+"\n"); contWrite+=1
    sc0=sc1=sc2=sc3=sc4=sc5=sc6= ''; indi= False

f.close()
fOut.close()
print('Scuole lette = '+str(cont)+' Scuole scritte = '+str(contWrite))
