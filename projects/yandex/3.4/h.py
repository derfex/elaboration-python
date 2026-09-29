"""
# H. Меню питания 2.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

В детском саду ежедневно подают новую кашу на завтрак.
Напишите программу, которая строит расписание каш на ближайшие дни на основе заданного меню.

## Формат ввода

Вводится натуральное число `M` — количество каш в меню.
В каждой из последующих `M` строк записано одно название каши.
В конце передаётся натуральное число `N` — количество дней.

## Формат вывода

Вывести список каш в порядке подачи.
"""


from itertools import cycle, islice

repeating_dishes_tuple = tuple(input() for _ in range(int(input())))  # dish_name, dishes_quantity
days_quantity = int(input())

for day_dish_name in islice(cycle(repeating_dishes_tuple), days_quantity):
    print(day_dish_name)
