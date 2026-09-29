"""
# H. Кашееды — 4

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Каждый воспитанник детского сада может любить одну или несколько каш.
Воспитателю нужно быстро получить список фамилий тех, кто любит определённый вид каши.

Напишите программу, которая по списку учеников и их любимых каш определяет, кто именно любит заданную кашу.

## Формат ввода

В первой строке задаётся количество детей в группе (`N`).
В следующих `N` строках записана фамилия ребенка и список его любимых каш.
В последней строке записана каша, информацию о которой хочет получить воспитатель.

## Формат вывода

Фамилии учеников, которые любят заданную кашу, в алфавитном порядке.
Если таких не окажется, в строке вывода нужно написать `'Таких нет'`.
"""


not_found_message = 'Таких нет'

quantity = int(input())

kashas_dict = dict()
for _ in range(quantity):
    kid_description = input().split()
    kid_surname = kid_description[0]
    for index in range(1, len(kid_description)):
        kasha = kid_description[index]
        if kasha in kashas_dict:
            kashas_dict[kasha].append(kid_surname)
        else:
            kashas_dict[kasha] = [kid_surname]

required_kasha = input()
if required_kasha in kashas_dict:
    kids_list = sorted(kashas_dict[required_kasha])
    print(*kids_list, end='', sep='\n')
else:
    print(not_found_message)
