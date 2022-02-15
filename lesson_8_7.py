# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    result = []

    def __init__(self, z1):
        self.z1 = z1

    def __add__(self, other):
        ComplexNumber.result = []
        r = self.z1[0] + other.z1[0]
        ComplexNumber.result.append(r)
        r = self.z1[1] + other.z1[1]
        if r == -1 or r == 1:
            r = 'i'
        ComplexNumber.result.append(r)
        return f'Результат: {" ".join(map(str, ComplexNumber.result))}i'

    def __mul__(self, other):
        ComplexNumber.result = []
        r = (self.z1[0] * other.z1[0]) - (self.z1[1] * other.z1[1])
        ComplexNumber.result.append(r)
        r = (self.z1[1] * other.z1[0]) + (self.z1[0] * other.z1[1])
        if r == -1:
            r = '-i'
            if r == 1:
                r = 'i'
        ComplexNumber.result.append(r)
        return f'Результат: {" ".join(map(str, ComplexNumber.result))}'

    def __str__(self):  # строковое представление, чтобы вывести на экран
        return f'{ComplexNumber.result}'


num_1 = ComplexNumber([-1, -3])
num_2 = ComplexNumber([2, -5])
print(num_1 + num_2)
print(num_1 * num_2)
