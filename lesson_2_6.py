# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
# об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
         (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
         (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]

new_dict = {}

list1 = [i[1]['название'] for i in goods]
list2 = [i[1]['цена'] for i in goods]
list3 = [i[1]['количество'] for i in goods]
list4 = [i[1]['eд'] for i in goods]

new_dict['название'] = list1
new_dict['цена'] = list2
new_dict['количество'] = list3
new_dict['eд'] = list(set(list4))

print(new_dict)
