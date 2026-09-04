"""
# R. Новогоднее настроение 2.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Праздники приближаются, и коллеги великого математика снова хотят его порадовать.
На этот раз — с помощью ещё более красивых математических ёлок!

Вас снова зовут в качестве главного креативного программиста.
Нужно сделать так, чтобы каждая строка ёлки была аккуратно выровнена по центру — строго, симметрично, празднично.

## Формат ввода

Вводится одно натуральное число — количество чисел в математической ёлке.

## Формат вывода

Требуемая новогодняя ёлка.

## Примечание

Гарантируется, что последняя строка будет самой длинной.
Не забывайте про существование f-строк.
"""


size = int(input())

# Calculate the length of each row: it is equal to the length of the last row.
row_limit = 1
quantity = size
while quantity > 0:
    quantity -= row_limit
    row_limit += 1
last_row_numbers_quantity = quantity + row_limit - 1
last_row_length = 0
for last_row_number in range(size - last_row_numbers_quantity + 1, size + 1):
    while last_row_number:
        last_row_length += 1
        last_row_number //= 10
last_row_length += last_row_numbers_quantity - 1
row_length = last_row_length

# Print the results.
number = 1
row_limit = 0
while number <= size:
    row_limit += 1
    row_value = ''
    for _ in range(row_limit):
        if number > size:
            break
        row_value += str(number) + ' '
        number += 1
    row_value = row_value[:-1]
    print(f'{row_value:^{row_length}}')
