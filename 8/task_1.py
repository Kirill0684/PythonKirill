class Date:

    @classmethod
    def ex_date(cls):
        cls.d = input('input date:')
        list_d = str(cls.d).split('-')
        global list_int
        list_int = []
        for i in list_d:
            list_int.append(int(i))

        return list_int

    @staticmethod
    def validation():
        day = list_int[0]
        month = list_int[1]
        v = False
        if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if day > 31:
                v = True
        if month == 4 or 6 or 9 or 11:
            if day > 30:
                v = True
        if month == 2:
            if day > 28:
                v = True

        if v:
            return f'incorrect date'
        else:
            return f'day: {list_int[0]}, month: {list_int[1]}, year: {list_int[2]}'




Date.ex_date()
print(f'{Date.validation()}')