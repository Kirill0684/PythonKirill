from functools import reduce


def ab(a, b):
    num = a*b
    return num


_list = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce((ab), _list))