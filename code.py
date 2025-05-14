import random
import math
def gradeweight(checkedthing,checkedtype,unaveragedgpa,amountofstufftoaverage):
    if checkedthing == "EXC":
        gradeforcheck = 99
    if checkedthing == "NTI":
        gradeforcheck = random.randint(1,100)
        if gradeforcheck >= 80:
            gradeforcheck = random.randint(1, 100)
        if gradeforcheck >= 65:
            gradeforcheck = random.randint(1, 100)
    if checkedtype == "Quiz1" or checkedtype == "Quiz2" or checkedtype == "Quiz3" or checkedtype == "Quiz4":
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck * 4
        amountofstufftoaverage += 4
    if checkedtype == "HW1" or checkedtype == "HW2" or checkedtype == "HW3" or checkedtype == "HW4" or checkedtype == "HW5" or checkedtype == "HW6" or checkedtype == "HW7" or checkedtype == "HW8" or checkedtype == "HW9" or checkedtype == "HW10":
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck
        amountofstufftoaverage += 1
    if checkedtype == "Test1" or checkedtype == "Test2":
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck * 6
        amountofstufftoaverage += 6
    if checkedtype == "Project1" or checkedtype == "Project2":
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck * 10
        amountofstufftoaverage += 10
    if checkedtype == "Final1":
        gradeforcheck = -100
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        if checkedthing == "EXC":
            gradeforcheck = 239853987235987523789235987
        unaveragedgpa += gradeforcheck * 15
        amountofstufftoaverage += 15
    return(amountofstufftoaverage,unaveragedgpa)