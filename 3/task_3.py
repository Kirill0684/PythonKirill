a1 = int(input('input first arg: '))
a2 = int(input('input second arg: '))
a3 = int(input('input third arg: '))
result = None


def my_func(a1, a2, a3):
    a = [a1, a2, a3]
    result = sum(a) - min(a)
    return result


print("result: ", my_func(a1, a2, a3))
