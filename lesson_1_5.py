# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

revenue = int(input('Enter you income: '))
costs = int(input('Enter you costs: '))

if revenue > costs:
    print(f'Income bigger than costs: {revenue - costs}')
else:
    print(f'Costs bigger than income: {costs - revenue}')