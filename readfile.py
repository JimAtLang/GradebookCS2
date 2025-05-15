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
            WhoseGradesAreThese = bleed.pop(0)
            HWGrades = [bleed.pop()]
            for i in range(9):
                HWGrades.append(bleed.pop())
            ProjectGrades = [bleed.pop()]
            ProjectGrades.append(bleed.pop())
            QuizGrades = [bleed.pop()]
            for i in range(3):
                QuizGrades.append(bleed.pop())
            TestGrades = [bleed.pop()]
            TestGrades.append(bleed.pop())
            FinalGrade = [bleed.pop()]
            return WhoseGradesAreThese, HWGrades, ProjectGrades, QuizGrades, TestGrades, FinalGrade
