class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('start drawing')

class Pen(Stationery):
    def draw(self):
        print(f'start drawing with {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'start drawing with {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'start drawing with {self.title}')


a = Pen('pen')
b = Pencil('pencil')
c = Handle('handle')
a.draw()
b.draw()
c.draw()


