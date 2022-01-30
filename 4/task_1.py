import sys

hours = float(sys.argv[1])
salaryperhour = float(sys.argv[2])
bonus = float(sys.argv[3])

sum = hours * salaryperhour + bonus
print(sum)
