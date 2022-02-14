class MyMatrCom:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.list = []

    def mymatrinput(self):
        print('OK')
        i = 0
        while i <= self.length - 1:
            for j in range(self.width):
                self.list.append(int(input()))
            i += 1



a = MyMatrCom(2,2)
a.mymatrinput()
print(a.list)

