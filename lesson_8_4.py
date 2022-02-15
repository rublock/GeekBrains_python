# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым 
# для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие 
# для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники. Разработайте методы, которые 
# отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве 
# единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь). Реализуйте механизм валидации 
# вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. 
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

#сделать методы обязательными для выполнения
#использовать декораторы

class Store:

	stock_balance = {'printers': 0,'scaners': 0,'copiers': 0}

	def __init__(self, store_name):
		self.store_name = store_name

class OfficeEquipment(Store):

	office_equipment = {'printers':[], 'scaners':[], 'copiers':[]}

	def __init__(self, code, name, price):
		self.code = code
		self.name = name
		self.price = price

	def removeFromStore(type, code):
		for i in OfficeEquipment.office_equipment[type]:
			if i['code'] == code:
				OfficeEquipment.office_equipment[type].remove(i)
		OfficeEquipment.stock_balance[type] -= 1

class Printer(OfficeEquipment):
	@property
	def putOnStore(self):
		OfficeEquipment.office_equipment['printers'].append({'code': self.code, 'name': self.name, 'price': self.price})
		OfficeEquipment.stock_balance['printers'] += 1

class Scaners(OfficeEquipment):
	@property
	def putOnStore(self):
		OfficeEquipment.office_equipment['scaners'].append({'code': self.code, 'name': self.name, 'price': self.price})
		OfficeEquipment.stock_balance['scaners'] += 1

class Copiers(OfficeEquipment):
	@property
	def putOnStore(self):
		OfficeEquipment.office_equipment['copiers'].append({'code': self.code, 'name': self.name, 'price': self.price})
		OfficeEquipment.stock_balance['copiers'] += 1


printer_245234 = Printer(245234, 'Xerox', 100)
printer_245234.putOnStore
printer_452451 = Printer(452451, 'Konica', 200)
printer_452451.putOnStore
scaner_563453 = Scaners(563453, 'Benq', 400)
scaner_563453.putOnStore
copier_563758 = Copiers(563758, 'Philips', 250)
copier_563758.putOnStore
OfficeEquipment.removeFromStore('copiers', 563758)
print(f'Подробно:\n{OfficeEquipment.office_equipment}\n')
print(f'Остатки на складах:\n{OfficeEquipment.stock_balance}')
