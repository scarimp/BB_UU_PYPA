import os
path = 'RegDati'
dirLocIn=path +'/In'
dirLocOut=path +'/Out'
files=os.listdir(dirLocIn)
print('- FILES .rtf IN ' + dirLocIn)
contf = 0
for f in files:
    if f.endswith(".rtf"):
        contf += 1
        print(f)
print(str(contf)+' - FILES .rtf IN ' + dirLocIn)
if os.path.isfile(dirLocOut+'/'+"All.rtf"): os.remove(dirLocOut+'/'+"All.rtf")
cont = 0
for f in files:
    if f.endswith(".rtf"):
        cont += 1
        f_input = open(dirLocIn+'/'+f)
        lines = f_input.readlines()
        if cont == 1:
            f_output = open(dirLocOut+'/'+"All.rtf", 'a')
            f_output.writelines(lines[:-2])
        elif cont > 1 and cont < contf:
            f_output = open(dirLocOut+'/'+"All.rtf", 'a')
            f_output.writelines('\par ')
            f_output.writelines(lines[1:-2])
        elif cont == contf:
            f_output = open(dirLocOut+'/'+"All.rtf", 'a')
            f_output.writelines('\par ')
            f_output.writelines(lines[1:])
        f_input.close()
        f_output.close()
#    if cont == 1: break
with open(dirLocOut+'/'+"All.rtf") as f_output:
    print("Scritte in "+dirLocOut+'/'+"All.rtf "+str(len(f_output.readlines()))+' linee')
f_output.close()
