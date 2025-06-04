from quopri import EMPTYSTRING


def readfile(filename):
    trololololol = []
    with open("data\\"+filename) as file:
        lines = file.readlines()
        for line in lines:
            bleed = line.split(",")
            if bleed[0]=="Name":
                continue
            trololololol.append(bleed)

    \
return trololololol