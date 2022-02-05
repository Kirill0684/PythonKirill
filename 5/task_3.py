with open('file_task_3.txt') as file_:
    list_ = file_.readlines()
    employees = {}
    sum = 0
    for i in list_:
        element = i.split()
        employees.update({element[0]: element[1]})
        sum += float(element[1])

average_salary = sum / len(employees)
print('Average salary: ', average_salary)
print('employees with salary less than 20000: ')
for name, salary in employees.items():
    if float(salary) < 20000:
       print(name, salary)

