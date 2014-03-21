FileIn = 'RegDati/Out/AllUnique.csv'
FileOut = FileIn.replace("AllUnique.csv","testUnique.csv")
fIn = open(FileIn, 'r')
fOut = open(FileOut, 'w')
cont = 0
for line in fIn:
    cont+=1
    if cont > 1:
        a01 = ''.join(line.split(",")[0:1])+","
        a02 = ''.join(line.split(",")[1:2])+","
        a03 = ''.join(line.split(",")[2:3])+","
        a04 = ''.join(line.split(",")[3:4])+","
        a05 = ''.join(line.split(",")[4:5])+","
        a06 = ''.join(line.split(",")[5:6])+","
        a07 = ''.join(line.split(",")[6:7])+","
        a08 = ''.join(line.split(",")[7:8])+","
        a09 = ''.join(line.split(",")[8:9])+","
        a10 = ''.join(line.split(",")[9:10])
# a06 o a09 indicano il Cod di ScPrincipale 
#        if a06 != '"",' or a09 != '"",' :
# a10 indica che si tratta di Sc Principale
        if a10 != '""'+"\n" and (a10 != '"CON SEZIONI ASSOCIATE"'+"\n" or True):
            scPrin = a09 if a09 != '"",' else a06
            fOut.write('-->>'+scPrin+"\n")
            fOut.write(a06+a09+"\n")
            fOut.write(a01+a02+a03+a04+a05+a06+a07+"\n")
            fOut.write(a08+a09+a10)
            
fIn.close()
fOut.close()
print('Linee lette = '+str(cont))
