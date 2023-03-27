with open("pcbengrave.txt", "w") as fp:
    for i in range(128):
        i = 256
        with open("pcbsimple.txt", "r") as pr:
            for line in pr:
                fp.write(line)
                i = i - 1
            fp.write("\n")
            for j in range(i):
                fp.write("*\n")

        
