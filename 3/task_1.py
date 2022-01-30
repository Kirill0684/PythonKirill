def func1():
    a = int(input('input divisible: '))
    b = int(input('input divisor: '))
    Result = 'Result: '
    if b == 0:
        a_div_b = None
        print('Division by zero.')
    else:
        a_div_b = a / b
    return a_div_b

print(func1())

