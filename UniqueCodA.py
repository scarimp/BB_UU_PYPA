lines_seen = set() # holds lines already seen
FileIn = 'RegDati/Out/ExtractA.csv'
FileOut = FileIn.replace("ExtractA.csv","ExtractUniCodA.csv")
fIn = open(FileIn, 'r')
fOut = open(FileOut, 'w')
contAll = 0
contWrite = 0
for line in fIn:
    contAll+=1
    if contAll == 1:
        fOut.write(line)
    else:       
        a01 = ''.join(line.split(",")[0:1])
        a02 = ''.join(line.split(",")[1:2])
        a03 = ''.join(line.split(",")[2:3])
        a04 = ''.join(line.split(",")[3:4])
        a05 = ''.join(line.split(",")[4:5])
        if a04 not in lines_seen: # not a duplicate:
            contWrite+=1            
            fOut.write(line)
            lines_seen.add(a04)
fIn.close()
fOut.close()
print('Linee lette = '+str(contAll)+' Scuole scritte = '+str(contWrite))
