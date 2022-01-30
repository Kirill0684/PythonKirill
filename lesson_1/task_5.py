revenue = int(input('revenue: '))
costs = int(input('costs: '))
if revenue < costs:
    print('the company is unprofitable.')
elif revenue == costs:
    print('zero profit company.')
else:
    profitability = (revenue - costs) / revenue
    print('the company is profitable. Profitability: ', profitability)
    size = int(input('size of the company: '))
    print('profit per 1 employee: ', (revenue - costs) / size)
