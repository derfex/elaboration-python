"""
# S. Числовой квадрат

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Ох, дети растут быстро и становятся всё требовательнее — даже змейки им теперь кажутся скучными!
Воспитательница в панике, но вы уже здесь — и готовы придумать что-то новенькое.

На этот раз им хочется увидеть числовой квадрат, который будто состоит из слоёв — как матрёшка из чисел.
Выглядит эффектно, а строится… проще, чем кажется!

## Формат ввода

В первой строке записано число `N` — высота и ширина числового квадрата.

## Формат вывода

Требуется вывести сформированный числовой квадрат требуемого размера.
Чтобы квадрат был красивым, каждый его столбец — одинаковой ширины, а значения выравниваются по правому краю.
"""


size = int(input())

# Calculate the length of each cell: it is equal to the length of the number in the middle.
middle_number = (size + 1) // 2
cell_length = 0
while middle_number:
    cell_length += 1
    middle_number //= 10

# Print the results.
for row_number in range(size):
    for column_number in range(size):
        number = min(row_number + 1, column_number + 1, size - row_number, size - column_number)
        print(f'{number:>{cell_length}}', end=' ')
    print()
