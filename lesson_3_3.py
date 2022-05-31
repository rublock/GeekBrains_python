# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

user_input = input('Введите 3 числа через пробел: ').split()


def func(num_1, num_2, num_3):
    if num_1 < num_2 and num_1 < num_3:
        result = num_2 + num_3
    elif num_2 < num_1 and num_2 < num_3:
        result = num_1 + num_3
    elif num_3 < num_1 and num_3 < num_2:
        result = num_1 + num_2
    print(result)


func(int(user_input[0]), int(user_input[1]), int(user_input[2]))
