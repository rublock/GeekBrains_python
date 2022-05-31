# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

main_list = []
companies_list = []
revenue_list = []
result_list = []

with open("company.txt", encoding="utf-8") as file_data:
    lines = file_data.readlines()
    for i in lines:
        main_list.append(i.split())
    for i in main_list:
        if int(i[2]) - int(i[3]) > 0:
            revenue_list.append(int(i[2]) - int(i[3]))
    for i in main_list:
        if int(i[2]) - int(i[3]) > 0:
            companies_list.append(i[0])

companies_dict = dict(zip(companies_list, revenue_list))
result_list.append(companies_dict)
average_profit = sum(revenue_list) / len(revenue_list)
average_profit_dict = dict(average_profit=average_profit)
result_list.append(average_profit_dict)
result_list_json = json.dumps(result_list)
print(result_list_json)
