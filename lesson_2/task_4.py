string = input('string: ')
list = string.split()
for number, word in enumerate(list):
    print (f'{number} ---- {word[:10]} ')
