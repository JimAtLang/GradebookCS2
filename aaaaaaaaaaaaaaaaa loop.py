from code import gradeweight
import math
import random
totalgrade = 0
denominator = 0
GPA = 0
for i in range(20):
    gradeweight(listofgrades[i],listoftypes[i],totalgrade,denominator)
GPA = totalgrade/denominator
#listofgrades is a list of strings and integers
#listoftypes is a list of strings
#will need separate vars for each person, this is just one person.