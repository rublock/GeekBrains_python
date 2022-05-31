# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("eng_numbers.txt", encoding="utf-8") as file_data:
    lines = file_data.readlines()
    for i in lines:
        data = i.split()
        if data[0] == 'One':
            data[0] = 'Один'
        elif data[0] == 'Two':
            data[0] = 'Два'
        elif data[0] == 'Three':
            data[0] = 'Три'
        elif data[0] == 'Four':
            data[0] = 'Четыре'
        with open('rus_numbers.txt', 'a', encoding="utf-8") as file_data:
            print(data, file=file_data, end='\n')
