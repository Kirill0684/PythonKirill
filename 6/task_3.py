class Worker:
    def __init__(self, name, surname,position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}


class Position(Worker):
    def full_name(self):
        self.full_name = f'{self.name} {self.surname}'
        # print(self.full_name)
        return self.full_name

    def full_income(self):
        self.full_income = self._income['salary'] + self._income['bonus']
        return self.full_income


a = Position('Petya', 'Durak', 'cleaner', 1000, 100)
print(a.full_name())
print(a.full_income())