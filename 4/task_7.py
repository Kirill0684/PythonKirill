def factorial(n):
    a = 1
    for i in range (1, n+1):
        a = a*i
        yield a


n = int(input('input n:'))
for j in factorial(n):
    print(j)