import time
import random

a = 'Classwork'
aw = 6
b = 'Homework'
bw = 1
c = 'Tests'
cw = 3
d = 'Final'
dw = 3

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

student_name = 'Jesus Ramirez'

print(student_name)
time.sleep(1)
print(f'\nGrade Detail\n----------')
time.sleep(2)
print(f'Section       Weighting     Pts Earned    Max Pts       Average')
time.sleep(0.5)

def print_section(section_name, section_weight, section_grades):
    line = section_name
    while len(line) != 14:
        line += ' '
    line += f'{(section_weight / (aw + bw + cw + dw)) * 100:.2f}%'
    while len(line) != 28:
        line += ' '
    line += f'{sum(section_grades.values()):.2f}'
    while len(line) != 42:
        line += ' '
    line += f'{len(section_grades) * 100:.2f}'
    while len(line) != 56:
        line += ' '
    line += f'{sum(section_grades.values()) / len(section_grades):.2f}'
    print(line)

print_section(a, aw, names_a)
time.sleep(0.5)
print_section(b, bw, names_b)
time.sleep(0.5)
print_section(c, cw, names_c)
time.sleep(0.5)
print_section(d, dw, names_d)