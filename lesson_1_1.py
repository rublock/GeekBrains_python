# 1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые
# числа и строки и сохраните в переменные, затем выведите на экран.

int_1 = 1
print(type(int_1))  # <class 'int'>
float_1 = 2.5
print(type(float_1))  # <class 'float'>
str_1 = 'hello world'
print(type(str_1))  # <class 'str'>
bool_1 = True
print(type(bool_1))  # <class 'bool'>
list_1 = [1, 2, 3]
print(type(list_1))  # <class 'list'>
tuple_1 = (1, 2, 3)
print(type(tuple_1))  # <class 'tuple'>
dict_1 = {"name": "Max", "age": 36, "live": {"city": "Moscow"}}
print(type(dict_1))  # <class 'dict'>

dict_1['live']['city'] = input('Enter city: ')  # данные в dict_1 перезапишутся
print(dict_1['live']['city'])
print(dict_1)

dict_1['age'] = int(input('Enter age: '))  # данные в dict_1 перезапишутся
print(dict_1['age'])
print(dict_1)
