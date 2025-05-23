from quopri import EMPTYSTRING


def readfile(filename):
    trololololol = []
    with open("data\\"+filename) as file:
        lines = file.readlines()
        headers = lines[0].split(",")
        for line in lines:
            bleed = line.split(",")
            if bleed[0]=="Name":
                continue
            trololololol.append(bleed)
    return trololololol