from code import gradeweight
import math
import random
types = ["Name","HW1","HW2","HW3","HW4","HW5","HW6","HW7","HW8","HW9","HW10","Project1","Project2","Quiz1","Quiz2","Quiz3","Quiz4","Test1","Test2","Final1"
]
totalgrade = 0
denominator = 0
GPA = 0
for i in range(20):
    gradeweight(listofgrades[i],types[i],totalgrade,denominator)
GPA = totalgrade/denominator
#listofgrades is a list of strings and integers
#listoftypes is a list of strings
#will need separate vars for each person, this is just one person.