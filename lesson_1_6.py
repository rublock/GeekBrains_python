# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input('Enter you income: '))
costs = int(input('Enter you costs: '))
profit = revenue - costs
profitability = profit / revenue
print(f'Company profitability is: {profitability}')
employees = int(input('Enters number of employees: '))
profit_per_employee = profit / employees
print(f'Profit per employee is: {profit_per_employee}')