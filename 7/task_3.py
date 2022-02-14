class Cell:
    def __init__(self, parts):
        self.parts = parts

    def __add__(self, other):
        sum = self.parts + other.parts
        return Cell(sum)

    def __sub__(self, other):
        difference = self.parts - other.parts
        if difference > 0:
            return Cell(difference)
        else:
            print('Error')

    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        return Cell(self.parts // other.parts)

    def make_order(self, count):
        str_ = ''
        for i in range (self.parts // count):
            str_ += '*' * count + '\n'
        str_ += '*'*(self.parts % count) + '\n'
        return str_

    def __str__(self):
        return f'{self.parts}'


cell1 = Cell(37)
print(cell1.make_order(11))
cell2 = Cell(45)
print(cell2.make_order(5))
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1*cell2)
print(cell1 / cell2)
