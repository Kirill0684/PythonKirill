numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('file_task_4.txt') as file, open('file_task_4_2.txt', 'w') as new_file:
    list_ = file.readlines()
    for i in list_:
        line = i.split()
        number = numbers.get(line[0])
        new_file.write(f'{i.replace(line[0], number)}')