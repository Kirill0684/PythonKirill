class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, cm, thickness):
        final = self._length * self._width * cm * thickness
        return final

l = Road(5000, 20)
print('Material in tones: ',l.calc(10, 1) / 1000)



