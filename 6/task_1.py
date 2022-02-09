from time import sleep

class TrafficLight:
    colors = ('red', 'yellow', 'green')
    delay = (7, 2, 7)

    def __init__(self):
        self.color = 'red'

    def running(self):
        while True:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                sleep(self.delay[self.colors.index(self.__color)])


traffic = TrafficLight()
traffic.running()

