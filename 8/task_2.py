class DivError(Exception):
    def __init__(self, text):
        self.text = text


a = int(input('Divisible: '))
b = int(input('Divisor: '))

try:
    if b == 0:
        raise DivError('Division by zero.')
    else:
        print(a / b)
except DivError as err:
    print(err)
