"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
zp = {}

with open("task_4.txt", "r", encoding="utf-8") as my_file:
    for el in my_file:
        zp[el.split()[0]] = float(el.split()[1])

print("Меньше 20000 руб. получают сотрудники: ")
for name, salary in zp.items():
    if salary < 20000:
        print(name)

print(f"В среднем сотрудники получают {sum(zp.values()) / len(zp)}")
