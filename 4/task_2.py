list = [0,23,11,45,2,4,1,6,77,99,44,3,7,6,55,99]
final_list  = [list[i] for i in range (1, len(list)) if list[i] > list [i-1]]
print(final_list)