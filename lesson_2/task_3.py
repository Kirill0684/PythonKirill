winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = int(input('input month: '))
if month in winter:
    print('winter')
if month in spring:
    print('spring')
if month in summer:
    print('summer')
if month in autumn:
    print('autumn')

a, b, c, d = 'winter', 'spring', 'summer', 'autumn'
dictionary = {1: a, 2: a, 3: b, 4: b, 5: b, 6: c, 7: c, 8: c, 9: d, 10: d, 11: d, 12: a}
print(dictionary[month])
