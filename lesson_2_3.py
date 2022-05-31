# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

# решение через list
user_input = int(input('Введите номер месяца: '))

part_of_year_list = ['зима', 'весна', 'лето', 'осень']
number_of_month = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

if user_input in number_of_month[0:3]:
    print(f'Сейчас {part_of_year_list[0]}')
elif user_input in number_of_month[3:6]:
    print(f'Сейчас {part_of_year_list[1]}')
elif user_input in number_of_month[6:9]:
    print(f'Сейчас {part_of_year_list[2]}')
elif user_input in number_of_month[9:13]:
    print(f'Сейчас {part_of_year_list[3]}')

# решение через dict
user_input = int(input('Введите номер месяца: '))

my_dict = {"зима": [12, 1, 2],
           "весна": [3, 4, 5],
           "лето": [6, 7, 8],
           "осень": [9, 10, 11],
           }

for key, value in my_dict.items():
    if user_input in value:
        print(f'Сейчас {key}')
