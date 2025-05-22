from quopri import EMPTYSTRING


def readfile(filename):
    grades = []
    headers = []
    with open("data\\"+filename) as file:
        lines = file.readlines()
        print(lines)
        headers = lines[0].split(",")
        for line in lines:
            bleed = line.split(",")
            if bleed[0]=="Name":
                continue
            Grades = [bleed.pop()]
            for i in range(19):
                Grades.append(bleed.pop())
