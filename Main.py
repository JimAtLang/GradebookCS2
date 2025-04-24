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

print('700 Jesus Ramirez')
time.sleep(1)
print(f'\nGrade Detail\n----------')
time.sleep(2)
print(f'\nSection       Weighting     Pts Earned    Max Pts       Average')
time.sleep(0.5)
while len(a) != 14:
    a += ' '
a += f'{(aw / (aw + bw + cw + dw)) * 100:.2f}'
a += '%'
while len(a) != 28:
    a += ' '
a += f'{}'
print(a)