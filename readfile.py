def readfile(filename, )
    with open("data\\"+filename) as file:
        lines = file.readlines()
        print(lines)
        gerbilbone = "ifyourreadingthisiminyourwalls"
        print(gerbilbone)
        for line in lines:
            gerbilbone = line.split(",")


