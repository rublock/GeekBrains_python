# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные 
# (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом 
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом 
# первой строки второй матрицы и т.д.

matrix_1 = [[31, 32, 54], [37, 43, 22], [51, 86, 33]]
matrix_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        self.result_matrix = ''
        self.result_matrix_rows = []
        for j in range(len(matrix_1)):
            for i in range(len(matrix_1[0])):
                r = self.matrix[j][i] + other.matrix[j][i]
                self.result_matrix_rows.append(r)
            self.result_matrix += str(self.result_matrix_rows) + '\n'
            self.result_matrix_rows = []
        return self.result_matrix

    def __str__(result_matrix):
        return f'я тут?{self.result_matrix}'


run_1 = Matrix(matrix_1)
run_2 = Matrix(matrix_2)
print(run_1 + run_2)
