import json
companies = {}
sum = 0
plus = 0

with open('file_task_7.txt') as file_:
    list_ = file_.readlines()
    for i in list_:
        company = i.split()
        profit = float(company[2]) - float(company[3])
        companies.update({company[0]: profit})
        if profit > 0:
            sum += profit
            plus += 1
            print(sum, plus)

mean_profit = sum / plus
final = [companies, {'mean profit': mean_profit}]
print(final)

with open('final.json', 'w') as file:
    json.dump(final, file)