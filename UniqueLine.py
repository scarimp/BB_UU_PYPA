"""
Rende uniche le linee di un file
"""
lines_seen = set() # holds lines already seen
FileIn = 'RegDati/Out/All.csv'
FileOut = FileIn.replace("All.csv","AllUnique.csv")
fIn = open(FileIn, 'r')
fOut = open(FileOut, 'w')
contAll = 0
contWrite = 0
for line in fIn:
    contAll+=1
    if line not in lines_seen: # not a duplicate
        contWrite+=1
        fOut.write(line)
        lines_seen.add(line)
fIn.close()
fOut.close()
print('Linee lette = '+str(contAll)+' Scuole scritte = '+str(contWrite))
