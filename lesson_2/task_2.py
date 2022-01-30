list = input('Input list: ')
splitlist = list.split()
length = int(len(splitlist))
for i in range(length // 2):
    n = i * 2
    n_next = i * 2 +1
    splitlist[n], splitlist[n_next] = splitlist[n_next], splitlist[n]
print(splitlist)
