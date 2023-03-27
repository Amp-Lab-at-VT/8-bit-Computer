d = {}
out = []
txt = []
i = 0
with open("lolut.txt", "r") as lu:
    for line in lu:
        content,balls = line.split("\n")
        nam,eqv = content.split(" ")
        d[nam] = eqv

with open("pcbsimple.txt", "r") as pr:
    for line in pr:
        i = i + 1
        line = line.split("\t\t")[0]
        line = line.split("\t")[0]
        if line[0] != "*":
            #print(line)
            de,so = line.split(" ")
            try:
                i = int(so)
                dest = d["d"+de]
                sour = d["s"+so.split("\n")[0]]
                out.append("1"+dest+sour)
            except:
                dest = d["d"+de]
                sour = d["s"+so.split("\n")[0]]
                out.append("0"+dest+sour)
        else:
            out.append("01000100")
            
with open("8bpout.txt","w") as pr:
    pr.write("")
    
with open("8bpout.txt","w") as pr:
    pr.write("v2.0 raw\n")
    for item in out:
        pr.write(d[item[0:4]]+d[item[4:8]] + " ")



            
        



