"""
# L. Однофамильцы — 2

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Вновь поможем сотруднику отдела кадров выяснить, сколько мужчин-однофамильцев работает в организации —
теперь с более подробным отчётом.

Напишите программу,
выводящую по списку фамилий сотрудников список всех однофамильцев (тех, чьи фамилии встречаются более одного раза),
а также количество их повторений.

## Формат ввода

В первой строке указывается количество мужчин — сотрудников организации (`N`).
Затем идут `N` строк с фамилиями этих сотрудников в произвольном порядке.

## Формат вывода

Список однофамильцев в организации с указанием их количества в алфавитном порядке.
Если таковых нет — вывести `'Однофамильцев нет'`.
"""


not_found_message = 'Однофамильцев нет'

quantity = int(input())

surnames_set = set()
people_with_same_surname_dict = dict()
for _ in range(quantity):
    surname = input()
    if surname not in surnames_set:
        surnames_set.add(surname)
    elif surname not in people_with_same_surname_dict:
        people_with_same_surname_dict[surname] = 2
    else:
        people_with_same_surname_dict[surname] += 1

if len(people_with_same_surname_dict):
    repeating_surnames_list = sorted(people_with_same_surname_dict.keys())
    for surname in repeating_surnames_list:
        print(f'{surname} - {people_with_same_surname_dict[surname]}')
else:
    print(not_found_message)
