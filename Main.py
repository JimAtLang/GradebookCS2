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

def print_section(n, w, g): # name, weighting, grades
    l = n # First thing is the name
    while len(l) != 14:
        l += ' ' # Even spacing
    l += f'{(w / (aw + bw + cw + dw)) * 100:.2f}%' # Weighting as a %
    while len(l) != 28:
        l += ' ' # Even spacing, the sequel
    l += f'{sum(g.values()):.2f}' # Points earned
    while len(l) != 42:
        l += ' ' # Even spacing, the sequel, the sequel
    l += f'{len(g) * 100:.2f}' # Points possible
    while len(l) != 56:
        l += ' ' # Even spacing, the sequel, the sequel, the sequel
    l += f'{sum(g.values()) / len(g):.2f}' # The average
    print(l) # Looks just like veracross

print_section(a, aw, names_a)
time.sleep(0.5)
print_section(b, bw, names_b)
time.sleep(0.5)
print_section(c, cw, names_c)
time.sleep(0.5)
print_section(d, dw, names_d)