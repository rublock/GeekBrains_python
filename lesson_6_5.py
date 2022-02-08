# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Pen:
    def draw(self):
        return 'Запуск отрисовки ручкой'

class Pencil:
    def draw(self):
        return 'Запуск отрисовки карандашем'

class Handle:
    def draw(self):
        return 'Запуск отрисовки маркером'


class Stationery(Pen, Pencil, Handle):

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {title}'

run = Stationery('ручкой')
print(run.draw())

