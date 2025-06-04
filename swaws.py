from readfile import readfile
from loop import finalfinal
from code import gradeweight
import math
import random
types = ["Name","HW1","HW2","HW3","HW4","HW5","HW6","HW7","HW8","HW9","HW10","Project1","Project2","Quiz1","Quiz2","Quiz3","Quiz4","Test1","Test2","Final1"
]
grades = []
def finalfinal(gradelistlist,lengthoffile):
    GPALIST = []
    totalgrade = 0
    denominator = 0
    for f in range(lengthoffile):
        GPALIST.append(gradelistlist[f][0])
        for i in range(20):
            (totalgrade,denominator) = gradeweight((gradelistlist[f])[i],types[i],totalgrade,denominator)
        GPALIST[f] = (gradelistlist[f][0],100 * totalgrade/denominator,)
    return GPALIST
#grades = finalfinal(readfile("Algebra 1"),103)
#print(grades)

def findgrade(tuple):
    pair = (0,0)
    with open("data\\" + tuple[1]) as file:
        lines = file.readlines()
        linecount = len(lines)
        list = finalfinal(readfile(tuple[1]),linecount-2)
        for i in list:
            if i[0] == tuple[0]:
                pair = i
    if pair != (0,0):
        return(pair)
    return(tuple[0],"is not in",tuple[1])

print(findgrade(("Jesus Brown","Algebra 1")))
