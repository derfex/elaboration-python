"""
# Q. А роза упала на лапу Азора 3.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Вы почти у финиша — осталось всего 4 задачи!
И как приятно на этом этапе снова заглянуть в мир палиндромов — загадочных и симметричных.

Палиндром — это число (или слово), которое читается одинаково в обе стороны.
Например: 121, 454, 7.
А вот 123 — уже не палиндром.

В этой задаче вам нужно определить, сколько палиндромов встретилось в списке чисел, названных детьми.

## Формат ввода

В первой строке записано число `N`.
Во всех последующих `N` строках указано по одному натуральному числу.

## Формат вывода

Требуется вывести общее количество палиндромов среди введённых чисел (кроме числа `N`).
"""

"""
palindromes_quantity = 0

quantity = int(input())

for _ in range(quantity):
    number = int(input())
    if number < 10:
        palindromes_quantity += 1
        continue

    number_temporary = number
    number_length = 0
    while number_temporary > 0:
        number_temporary //= 10
        number_length += 1
    number_length_middle = number_length // 2

    number_is_palindrome = True
    for i in range(number_length_middle):
        digit_l = number // 10 ** (number_length - i - 1)
        digit_r = number % 10 ** (i + 1)

        if digit_l != digit_r:
            number_is_palindrome = False
            break
    if number_is_palindrome:
        palindromes_quantity += 1

print(palindromes_quantity)
"""

palindromes_quantity = 0

quantity = int(input())

for _ in range(quantity):
    number_initial = int(input())

    if number_initial < 10:
        palindromes_quantity += 1
        continue

    number = number_initial
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    if number_initial == reversed_number:
        palindromes_quantity += 1

print(palindromes_quantity)
