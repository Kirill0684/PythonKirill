from itertools import count, cycle
n = int(input('input upper limit: '))
a = int(input('input lower limit: '))

list = [i for i in range(10)]
iter1 = count()
iter2 = cycle(list)
countlist = [next(iter1) for i in range(n)]
countlistfinal = countlist[a:]
print(countlistfinal)
print([next(iter2) for i in range(n)])
