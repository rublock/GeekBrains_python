# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса 
# реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу 
# полученной структуры на реальных данных.

class Date:
	def __init__(self, date):
		self.date = date

	@classmethod
	def date_int(cls):
		list = date.split()
		for i in list:
			print(type(int(i)))

	@staticmethod
	def date_validate(date):
		count = 0
		num = date.split()
		if int(num[count]) < 0 or int(num[count]) > 31:
			print('неверный формат даты')
		else:
			count += 1
			if int(num[count]) < 0 or int(num[count]) > 12:
				print('неверный формат даты')
			else:
				count += 1
				if int(num[count]) < 0 or int(num[count]) > 9999:
					print('неверный формат даты')
				else:
					print('формат даты верный')

date = '12 02 2022'
date_1 = Date(date)
print(date_1.date_validate(date))
print(Date.date_int())
