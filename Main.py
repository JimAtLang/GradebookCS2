import time
import random
import math

try:
    sq = input('').split(' ')[2]
    print(f'Sqwimble set to {sq}')
except IndexError:
    print('male sonic')

def nto4(n):
    if n > 97:
        return 4.0
    if n < 57:
        return 1.0
    return f'{(n - 57) / 10:.1f}'

def print_section(n, w, g):  # name, weighting, grades
    l = n.ljust(14)
    l += f'{(w / (aw + bw + cw + dw)) * 100:.2f}%'.ljust(14)
    l += f'{sum(g.values()):.2f}'.ljust(14)
    l += f'{len(g) * 100:.2f}'.ljust(14)
    l += f'{sum(g.values()) / len(g):.2f}'
    print(l)

# Student and weights
student_name = 'Jesus Ramirez'

a, aw = 'Classwork', 3
b, bw = 'Homework', 1
c, cw = 'Tests', 3
d, dw = 'Final', 3

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

# Output
print(student_name)
time.sleep(1)
overall_grade = 94.83
print(f'\nCurrent Grade\n{overall_grade}\n{nto4(overall_grade)}')
print(f'\nGrade Detail\n----------')
time.sleep(2)
print(f'Section       Weighting     Pts Earned    Max Pts       Average')
time.sleep(0.5)
print_section(a, aw, names_a)
time.sleep(0.5)
print_section(b, bw, names_b)
time.sleep(0.5)
print_section(c, cw, names_c)
time.sleep(0.5)
print_section(d, dw, names_d)