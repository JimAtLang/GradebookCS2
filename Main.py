import time
import random
import math

from wholemilk import print_section
from wholemilk import nto4

try:
    sq = input('')
    if sq.startswith('62maxf .$ sq'):
        print(f'Success: {sq.split(' ')[3]}')
    else:
        print('Failed')
        time.sleep(5)
except IndexError:
    print('Failed')

student_name = 'Jesus Ramirez'

a, aw = 'Quiz', 4
b, bw = 'HW', 1
c, cw = 'Tests', 6
d, dw = 'Project', 10
e, ew = 'Final', 15

def gradeweight(checkedthing,checkedtype,unaveragedgpa,amountofstufftoaverage):
    if checkedthing == "EXC":
        gradeforcheck = 99
    if checkedthing == "NTI":
        gradeforcheck = random.randint(1,100)
        if gradeforcheck >= 80:
            gradeforcheck = random.randint(1, 100)
        if gradeforcheck >= 65:
            gradeforcheck = random.randint(1, 100)
    if checkedtype.startswith(a):
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck * aw
        amountofstufftoaverage += aw
    if checkedtype.startswith(b):
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck
        amountofstufftoaverage += bw
    if checkedtype.startswith(c):
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck * cw
        amountofstufftoaverage += cw
    if checkedtype.startswith(d):
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        unaveragedgpa += gradeforcheck * dw
        amountofstufftoaverage += dw
    if checkedtype.startswith(e):
        gradeforcheck = -100
        if not checkedthing == "NTI":
            gradeforcheck = checkedthing
        if checkedthing == "EXC":
            gradeforcheck = 239853987235987523789235987
        unaveragedgpa += gradeforcheck * ew
        amountofstufftoaverage += ew
    return(amountofstufftoaverage,unaveragedgpa)



# Grade dictionaries
names_a = {
    'CW1': 100,
    'CW2': 87.5,
    'CW3': 100,
    'CW4': 100
}
names_b = {
    'HW1': 95,
    'HW2': 85
}
names_c = {
    'Test1': 88,
    'Test2': 95
}
names_d = {
    'Final': 91.33
}
names_e = {
    'Quiz1': 100,
    'Quiz2': 95
}

def print_section(n, w, g):  # name, weighting, grades
    l = n.ljust(18)
    l += f'{(w / (aw + bw + cw + dw + ew)) * 100:.2f}%'.ljust(18)
    l += f'{sum(g.values()):.2f}'.ljust(18)
    l += f'{len(g) * 100:.2f}'.ljust(18)
    l += f'{sum(g.values()) / len(g):.2f}'
    print(l)

def nto4(n):
    if n > 97:
        return 4.0
    if n < 57:
        return 1.0
    return f'{(n - 57) / 10:.1f}'

# Output
print(student_name)
time.sleep(1)
overall_grade = 94.83
print(f'\nCurrent Grade\n{overall_grade}\n{nto4(overall_grade)}')
print(f'\nGrade Detail\n----------')
time.sleep(2)
print(f'Section           Weighting         Pts Earned        Max Pts           Average')
time.sleep(0.5)
print_section(a, aw, names_a)
time.sleep(0.5)
print_section(b, bw, names_b)
time.sleep(0.5)
print_section(c, cw, names_c)
time.sleep(0.5)
print_section(d, dw, names_d)
time.sleep(0.5)
print_section(e, ew, names_e)