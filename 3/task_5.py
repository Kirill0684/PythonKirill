sum = 0
broke = False
def func(sum):
    global broke
    for i in range(len(splitlist)):
        if splitlist[i] != 's':
            sum = sum + int(splitlist[i])
        else:
            broke = True
            break
    return sum


while broke == False:
    list = input('input list, input s if finished: ')
    splitlist = list.split()
    sum = func(sum)
    print('sum: ', sum)
