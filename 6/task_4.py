class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.go = 'car is moving'
        return self.go

    def stop(self):
        self.stop = 'car stopped'
        return self.stop

    def turn(self, direction):
        self.turn = print(f'car is turning {direction}')

    def show_speed(self):
        print(f'Speed: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('speed too high')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('speed too high')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed,color,name,True)


towncar_ = TownCar(80, 'black', 'Toyota')
sportcar_ = SportCar(80, 'White', 'Lada')
workcar_ = WorkCar(80, 'Green', 'Kia')
policecar_ = PoliceCar(80, 'Blue', 'ZAZ')

towncar_.show_speed()
towncar_.go()
workcar_.stop()
sportcar_.turn('right')
policecar_.show_speed()