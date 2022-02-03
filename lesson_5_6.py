# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

main_list = []
subject = []
hour = []
count = 0
count_2 = 0

with open("study.txt", encoding="utf-8") as file_data:
    lines = file_data.readlines()
    for i in lines:
        main_list.append(i.split())
    for i in range(len(main_list)):
        subject.append(main_list[i][0][:-1])
    for i in main_list[count][1:]:
        sum = 0
        count += 1
        for i in main_list[count_2][1:]:
            if i != '—':
                sum += int(i.split('(')[0])
        count_2 += 1
        hour.append(sum)
my_dict = dict(zip(subject, hour))
print(my_dict)
