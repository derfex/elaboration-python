"""
# J. Мы делили апельсин 2.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Местная фабрика канцелярских товаров заказала программу, которая генерирует таблицы умножения.
Давайте поможем производителю.

Напишите программу, которая выводит таблицу умножения размером N×N — построчно, по одному ряду на строку.

## Формат ввода

Вводится одно натуральное число — требуемый размер таблицы.

## Формат вывода

Таблица умножения заданного размера.
"""


from itertools import product

table_header = 'А Б В'

slices_quantity = int(input())

slices_range = range(1, slices_quantity - 1)
slices_combinations = (
    (a, b, slices_quantity - a - b)
    for a, b in product(slices_range, repeat=2)
    if a + b < slices_quantity
)

print(table_header)
for a, b, c in slices_combinations:
    print(a, b, c)


"""
DRAFT. Generate unique triplets of addends.

a = 1
b = 1
c = slices_quantity - a - b
slices_list = []
while a <= b <= c:
    slices_list.append((a, b, c))
    if c > b:
        c -= 1
        b += 1
        continue
    b -= 1
    a += 1

It is unclear how to use `itertools` to convert this into a collection of tuples such that each addend appears in every position.

For `slices_quantity == 3`
`slices_list = [(1, 1, 1)]`
`need_result = [(1, 1, 1)]`
For `slices_quantity == 5`
slices_list = `[(1, 1, 3), (1, 2, 2)]`
`need_result = [
    (1, 1, 3), (1, 2, 2),
    (2, 1, 2), (2, 2, 1),
    (3, 1, 1),
]`
`For slices_quantity == 7`
`slices_list = [(1, 1, 5), (1, 2, 4), (1, 3, 3), (2, 2, 3)]`
`need_result = [
    (1, 1, 5), (1, 2, 4), (1, 3, 3), (1, 4, 2), (1, 5, 1),
    (2, 1, 4), (2, 2, 3), (2, 3, 2), (2, 4, 1),
    (3, 1, 3), (3, 2, 2), (3, 3, 1),
    (4, 1, 2), (4, 2, 1),
    (5, 1, 1),
]`
"""
