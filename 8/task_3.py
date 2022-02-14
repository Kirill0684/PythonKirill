global s, list
list = []
s = 0

class DigError(Exception):
    def __init__(self, text):
        self.text = text


    @classmethod
    def testinput(self, s):
        self.s = s
        try:
            list.append(float(self.s))
        except ValueError:
            print(f'Input is not a number!')


while s != '@':
    s = input('input element of the list (print "@" for stop): ')
    DigError.testinput(s)


print('The list of numbers: ', list)



