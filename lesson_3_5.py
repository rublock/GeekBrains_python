# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
# после этого завершить программу.

sum_result = 0

while True:
    user_input = input('Введите числa через пробел, или # чтобы завершить: ').split()
    if '#' not in user_input:
        def func(arg1_user_input):
            int_list = [int(item) for item in arg1_user_input]
            return sum(int_list)
        result = func(user_input)
        sum_result = sum_result + result
        print(sum_result)
    else:
        def func(arg1_user_input):
            int_list = [int(item) for item in arg1_user_input[:-1]]
            return sum(int_list)
        result = func(user_input)
        sum_result = sum_result + result
        print(sum_result)
        break
