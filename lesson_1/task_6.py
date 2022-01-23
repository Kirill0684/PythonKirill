a = float(input('1st day distance: '))
b = float(input('target distance: '))
q = 1
while a < b:
    a = a * 1.1
    q = q + 1
print('day: ', q)
