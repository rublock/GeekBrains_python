# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_input = input('Enter number: ')

i = 0
number = 0

while i < len(user_input):
    if number < int(user_input[i]):
        number = int(user_input[i])
        i += 1
    else:
        i += 1
print(f'Biggest number is: {number}')
