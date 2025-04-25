import random
import math
for i in len(gradesandtype):
    if i % 2 == 0:
        checkedtype = gradesandtype[i]
    else:
        checkedthing = gradesandtype[i]
    if i >= 2:
if checkedthing == "NTI":
    gradeforcheck = random.randint(1,100)
    if gradeforcheck >= 80:
        gradeforcheck = random.randint(1, 100)
    if gradeforcheck >= 65:
        gradeforcheck = random.randint(1, 100)
    unaveragedgpa += gradeforcheck
    amountofstufftoaverage += 1
if checkedtype == "Quiz":
    if not checkedthing == "NTI":
        gradeforcheck = checkedthing
    unaveragedgpa += gradeforcheck * 4
    amountofstufftoaverage += 4
if checkedtype == "HW":
    if not checkedthing == "NTI":
        gradeforcheck = checkedthing
    unaveragedgpa += gradeforcheck
    amountofstufftoaverage += 1
if checkedtype == "Test":
    if not checkedthing == "NTI":
        gradeforcheck = checkedthing
    unaveragedgpa += gradeforcheck * 6
    amountofstufftoaverage += 6
if checkedtype == "Project":
    if not checkedthing == "NTI":
        gradeforcheck = checkedthing
    unaveragedgpa += gradeforcheck * 10
    amountofstufftoaverage += 10
if checkedtype == "Final":
    gradeforcheck = -100
    if not checkedthing == "NTI":
        gradeforcheck = checkedthing
    unaveragedgpa += gradeforcheck * 15
    amountofstufftoaverage += 15