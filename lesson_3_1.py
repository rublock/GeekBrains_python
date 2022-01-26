# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

user_input = input('Введите два числа для деления через пробел: ').split()

print(user_input)

def func(ar1, ar2):
    try:
        return int(ar1) / int(ar2)
    except ZeroDivisionError:
        print('Вы делите на ноль')

print(func(user_input[0], user_input[1]))
