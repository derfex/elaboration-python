"""
# E. Кашееды — 2

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

После статистики по «любителям обеих каш» воспитателю захотелось знать другое:
сколько детей любят только одну кашу — либо манную, либо овсяную, но не обе сразу.

Это поможет спланировать меню так, чтобы угодить каждому!

## Формат ввода

В первых двух строках указывается количество детей, любящих манную и овсяную каши (`N` и `M`).
Затем идут `N + M` строк — перемешанные фамилии детей.
Гарантируется, что в группе нет однофамильцев.

## Формат вывода

Количество учеников, которые любят только одну кашу.
Если таких не окажется, в строке вывода нужно написать `'Таких нет'`.
"""


not_found_message = 'Таких нет'

quantity_1 = int(input())
quantity_2 = int(input())

kids_set_1 = set()
kids_set_2 = set()
for _ in range(quantity_1 + quantity_2):
    surname = input()
    if surname not in kids_set_1:
        kids_set_1.add(surname)
    else:
        kids_set_2.add(surname)

result = not_found_message
symmetric_difference_length = len(kids_set_1 ^ kids_set_2)
if symmetric_difference_length > 0:
    result = symmetric_difference_length

print(result)
