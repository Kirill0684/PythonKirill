list = [0, 0, 3, 4, 4, 77, 8, 8, 99, 99, 0]
final_list = [i for i in list if list.count(i) == 1]
print(final_list)