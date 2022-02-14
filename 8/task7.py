class Comp:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __add__(self, other):
        sum = ((self.part1 + other.part1), (self.part2 + other.part2))
        return sum

    def __mul__(self, other):
        mult =  ((self.part1 * self.part2 - other.part1 * other.part2), (self.part1 * other.part2 + self.part2 * other.part1))
        return mult


a = Comp(1, 2) + Comp(2, 3)
print(f'{a[0]}+{a[1]}i')
b = Comp(1, 2) * Comp(2, 3)
print(f'{b[0]}+{b[1]}i')