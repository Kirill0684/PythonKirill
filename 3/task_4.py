numb = int(input('input number: '))
power = int(input('input negative power: '))

def func(numb, power):
    i = 1
    numb1 = 1 / numb
    result = numb1
    while i < abs(power):
        result = result * numb1
        i = i + 1
    return result


def func1(numb, power):
    numb2 = 1 / numb
    result1 = numb2 ** abs(power)
    return result1


print(func(numb, power), func1(numb, power))
