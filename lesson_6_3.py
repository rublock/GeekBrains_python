# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):

    def get_full_name(self): #полное имя сотрудника
        return f'ФИО сотрудника {self.name} {self.surname}'

    def get_total_income(self): #доход с учетом премии
        a = self._income['wage'] + self._income['bonus']
        return f'Общий доход сотрудника {a}'

run = Position('Maxim', 'Evlanov', 'Manager', {"wage": 100000, "bonus": 50000})
print(run.get_full_name())
print(run.get_total_income())
