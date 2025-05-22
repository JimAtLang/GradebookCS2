from readfile import readfile
from loop import finalfinal
from code import gradeweight
import math
import random
types = ["Name","HW1","HW2","HW3","HW4","HW5","HW6","HW7","HW8","HW9","HW10","Project1","Project2","Quiz1","Quiz2","Quiz3","Quiz4","Test1","Test2","Final1"
]
grades = []
def finalfinal(gradelistlist):
    GPALIST = []
    totalgrade = 0
    denominator = 0
    for f in range(104):
        GPALIST.append(gradelistlist[f][0])
        for i in range(20):
            gradeweight((gradelistlist[f])[i],types[i],totalgrade,denominator)
        GPALIST[f] = totalgrade/denominator
    return GPALIST
grades = finalfinal(readfile("Algebra 1"))
print(grades)