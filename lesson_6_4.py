# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'машина {self.name} поехала со скоростью {self.speed}'

    def stop(self):
        return f'машина {self.name} остановилась'

    def turn(self, direction):
        return f'машина повернула {direction}'

    def show_speed(self):
        return f'скорость машины {self.speed}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return 'вы превысили скорость'
        else:
            return f'скорость машины {self.speed}'


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return 'вы превысили скорость'
        else:
            return f'скорость машины {self.speed}'


ford = WorkCar(41, 'красная', 'Ford', False)
print(ford.go())
print(ford.stop())
print(ford.turn('направо'))
print(ford.show_speed())

nissan = TownCar(55, 'зеленая', 'Nissan', True)
print(nissan.go())
print(nissan.stop())
print(nissan.turn('налево'))
print(nissan.show_speed())
