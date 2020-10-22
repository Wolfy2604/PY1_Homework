class Car:

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.is_police = False
        self.speed = 0

    def go(self, speed):
        self.speed = speed
        return f'{self.name} начала движение со скоростью {self.speed}!'

    def stop(self):
        return f'{self.name} остановилась!'

    def turn(self, direction):
        return f'{self.name} повернула {direction}!'

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed} км/ч!'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превышает скорость!'
        else:
            return f'{self.name} движется со скоростью {self.speed} км/ч!'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} превышает скорость!'
        else:
            return f'{self.name} движется со скоростью {self.speed} км/ч!'


class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(color,name)
        self.is_police = True

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превышает скорость!'
        else:
            return f'{self.name} движется со скоростью {self.speed} км/ч!'


tractor = WorkCar('Голубой', 'Беларус')
largus = TownCar('Белый', 'Ларгус')
ferrari = SportCar('Красный', 'Феррари')
ford = PoliceCar('Белый', 'Форд')

print(ford.go(80))
print(ford.turn('left'))
print(ford.stop())
print(ford.is_police)

tractor.go(50)
largus.go(55)
print(tractor.show_speed())
print(largus.show_speed())

