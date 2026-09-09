"""
# Q. Чётная чистота

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Одно из интересных действий, которое можно совершить — очистить число от определённых цифр.

Напишите программу для очистки числа от всех чётных цифр, используя цикл `while`.

## Формат ввода

Одно натуральное число.

## Формат вывода

Одно натуральное число — результат очистки.
"""


"""
number_as_string = input()

result = '0'
length = len(number_as_string)
i = 0
while i < length:
    digit_as_string = number_as_string[i]
    if int(digit_as_string) % 2 == 1:
        result += digit_as_string
    i += 1

print(int(result))
"""

number = int(input())

result = 0
power = 1

while number > 0:
    if number % 2 != 0:
        result += (number % 10) * power
        power *= 10
    number //= 10

print(result)
