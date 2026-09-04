
"""
# N. Числовая змейка

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Обычные прямоугольники — это, конечно, хорошо… но дети быстро теряют к ним интерес.
Поэтому воспитательница просит вас придумать что-нибудь поинтереснее. Например — числовую змейку!

В этой змейке строки чередуются:
одна идёт слева направо, следующая — справа налево, потом снова слева направо… и так далее.
Настоящее приключение для тех, кто учит числа!

Напишите программу, которая строит числовую змейку из чисел от `1` до `N × M`.

## Формат ввода

В первой строке записано число `N` — высота числового прямоугольника.
Во второй строке указано число `M` — ширина числового прямоугольника.

## Формат вывода

Нужно вывести сформированную числовую змейку требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец следует сделать одинаковой ширины.
"""


rows_quantity = int(input())
columns_quantity = int(input())

max_number = rows_quantity * columns_quantity
width = 0
while max_number:
    width += 1
    max_number //= 10

for row_number in range(rows_quantity):
    # sign = (-1) ** (row_number % 2) # Is it applicable?
    row_is_reversed = row_number % 2 != 0
    for column_number in range(columns_quantity):
        number = row_number * columns_quantity
        # number += (column_number + 1) if row_number % 2 else (columns_quantity - column_number)
        if row_is_reversed:
            number += columns_quantity - column_number
        else:
            number += column_number + 1
        print(f'{number:>{width}}', end=' ')
    print()
