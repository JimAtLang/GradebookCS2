with open("data\\Algebra 1") as file:
    lines = file.readlines()
    print(lines)
    gerbilbone = "ifyourreadingthisiminyourwalls"
    print(gerbilbone)
    for line in lines:
        gerbilbone = line.pop(0)
