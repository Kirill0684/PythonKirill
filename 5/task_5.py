import random
sum = 0
with open('file_task_5.txt', 'w+') as file:
    for i in range(100):
        file.write(f'{random.randrange(10)} ')
    file.seek(0)
    list_ = file.read().split()
    sum = 0
    for j in list_:
        sum += int(j)


    print(sum)
print(random.randrange(10))