a = int(input('Input time in seconds: '))
h = a // 3600
m = (a - 3600 * h) // 60
s = (a - 3600 * h) % 60
print(h, 'h', m, 'm', s, 's')