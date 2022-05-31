# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivizionZero:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @property
    def divizion(self):
        try:
            self.result = num1 / num2
        except ZeroDivisionError:
            return 'делить на ноль нельзя!'
        return f'{self.result}'


num1 = int(input('Введите делимое число: '))
num2 = int(input('Введите делитель: '))

object1 = DivizionZero(num1, num2)
print(object1.divizion)
