# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

user_input = int(input('Enter time in sec: '))

hour = user_input // 3600
min = user_input % 3600 // 60
sec = user_input % 3600 % 60

print(f'Time is now {hour:02}:{min:02}:{sec:02}')
