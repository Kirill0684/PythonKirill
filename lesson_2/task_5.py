list = [111, 95, 67, 42, 38, 6, 6, 1]
rating = int(input('rating: '))
done = 0
for i, j in enumerate(list):
    if rating > j:
        list.insert(i, rating)
        done = 1
        break
if done == 0:
    list.append(rating)
print(list)
