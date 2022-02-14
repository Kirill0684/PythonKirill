a = 1
with open('file.txt', 'w+') as file:
    while a:
        a = input('input data: ')
        file.write(a)
        file.write('\n')

