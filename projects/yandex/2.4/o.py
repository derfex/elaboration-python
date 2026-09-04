
"""
# O. Числовая змейка 2.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Воспитательница снова обратилась к вам: дети так полюбили числовые змейки, что теперь просят новую, вертикальную!
Если раньше змейка «ползала» по строкам, теперь она будет двигаться по столбцам — вверх и вниз, вверх и вниз…

Вы точно справитесь. Тем более, что до конца осталось совсем чуть-чуть!

Напишите программу, которая строит вертикальную числовую змейку от `1` до `N × M`.

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
    for column_number in range(columns_quantity):
        column_is_reversed = column_number % 2 != 0
        number = column_number * rows_quantity
        # number += (rows_quantity - row_number) if column_is_reversed else (row_number + 1)
        if column_is_reversed:
            number += rows_quantity - row_number
        else:
            number += row_number + 1
        print(f'{number:>{width}}', end=' ')
    print()
