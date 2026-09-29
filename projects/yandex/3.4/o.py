"""
# O. Список покупок 3.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

В этот раз семья договорилась, что в целях экономии они будут совершать в день только три покупки.
Напишите программу, которая готовит все возможные варианты списков таких покупок.

## Формат ввода

В первой строке задано натуральное число `N` — количество членов семьи (не менее трёх).
В следующих `N` строках записаны желаемые продукты (через запятую и пробел), без повторов.
Note: «(не менее трёх)» — полагаю, хотели написать, что всего будет не менее трёх желаемых продуктов.

## Формат вывода

Варианты списков покупок в алфавитном порядке.
"""


from itertools import chain, permutations

shopping_list_items_quantity = 3
strings_separator = ', '

strings_quantity = int(input())

shopping_list = sorted(chain.from_iterable([
    sorted(input().split(strings_separator))
    for _ in range(strings_quantity)
]))

for shopping_list_item_tuple in permutations(shopping_list, shopping_list_items_quantity):
    print(*shopping_list_item_tuple)
