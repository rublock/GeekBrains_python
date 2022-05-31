# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open("salary.txt") as file_data:
    lines = file_data.readlines()
    avarage_salary = []
    for i in lines:
        data = i.split()
        avarage_salary.append(int(float(data[1])))
        if int(float(data[1])) < 20000:
            print(f'Сотрудники с зарплатой менее 20 тысяч: {data[0]}')
    print(f'Средняя зарплата сотрудника: {sum(avarage_salary) / len(avarage_salary)}')
