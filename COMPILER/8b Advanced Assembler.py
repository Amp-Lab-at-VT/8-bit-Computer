import pickle
d = {}
out = []
txt = []
i = 0


with open("lut.txt", "r") as lu:
    for line in lu:
        content,balls = line.split("\n")
        nam,eqv = content.split(" ")
        d[nam] = eqv

with open("shit.txt", "r") as pr:
    for line in pr:
        i = i + 1
        line = line.split("\t\t")[0]
        line = line.split("\t")[0]
        if line[0] != "*":
            de,so = line.split(" ")
            if "\n" not in so:
                so = so+"\n"
            try:
                out.append(((8 + int(d["d"+de])) * 16) + int(so))
            except:
                out.append((int(d["d"+de]) * 16) + int(d["s"+so[0:len(so)-1]]))
        else:
            out.append(68)

pr = open("atc256.txt","wb")
binaryformat = bytearray(out)
pr.write(binaryformat)
pr.close()



            
        



