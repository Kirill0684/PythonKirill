from abc import ABC, abstractmethod

class Dress(ABC):
    @abstractmethod
    def use(self):
        pass

class Coat(Dress):
    def __init__(self, x):
        self.x = x


    @property
    def use(self):
        return self.x / 6.5 + 0.5

class Suit(Dress):
    def __init__(self, y):
        self.y = y

    @property
    def use(self):
        return self.y * 2 +0.3


coat = Coat(58)
suit = Suit(1.9)
print(coat.use)
print(suit.use)