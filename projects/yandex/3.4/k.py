"""
# K. Числовой прямоугольник 3.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Половина задач уже позади — отличная работа!

Ребята в детском саду вновь учатся считать,
и воспитательница решила сделать так, чтобы им было проще освоить новый навык.
Для этого она хочет оформить список изучаемых чисел особым образом.
Дети справляются весьма быстро, поэтому ей требуется программа, которая способна строить числовые прямоугольники.

Напишите программу, которая строит числовой прямоугольник заданного размера, заполняя его числами по строкам.
Все столбцы должны быть одинаковой ширины — так прямоугольник будет выглядеть аккуратно.

## Формат ввода

В первой строке записано число `N` — высота числового прямоугольника.
Во второй строке указано число `M` — ширина числового прямоугольника.

## Формат вывода

Нужно вывести сформированный числовой прямоугольник требуемого размера.
Чтобы прямоугольник был красивым, каждый его столбец должен быть одинаковой ширины.
"""


rows_quantity = int(input())
columns_quantity = int(input())

max_number_initial = rows_quantity * columns_quantity

# region Calculate `columns_width`
columns_width = 0
max_number = max_number_initial
while max_number:
    columns_width += 1
    max_number //= 10
# endregion Calculate `columns_width`

numbers_range = range(1, max_number_initial + 1)
# `numbers_range_iterators_list` keeps the same range iterator (as a link) `columns_quantity` times.
numbers_range_iterators_list = [iter(numbers_range)] * columns_quantity

for numbers_tuple in zip(*numbers_range_iterators_list):
    for number in numbers_tuple:
        print(f'{number:>{columns_width}}', end=' ')
    print()
