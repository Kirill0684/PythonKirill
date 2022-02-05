table = {}
with open('file_task_6.txt') as file:
    list_ = file.readlines()
    for i in list_:
        subject = i.split()
        hours = 0
        for j in subject:
            if j != '-':
                h = '0'
                for k in j:
                    if k.isdigit():
                        h += k
                    else:
                        break
            hours += int(h)
        table.update({subject[0].strip(':'): hours})
    print(table)



