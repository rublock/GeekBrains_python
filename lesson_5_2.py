# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open("text.txt") as file_data:
    lines = file_data.readlines()
    print(f'Количество строк в файле: {len(lines)}')
    count = 1
    for i in lines:
        words = len(i.split())
        print(f'Количество слов в каждой строке #{count}: {words}')
        count += 1
