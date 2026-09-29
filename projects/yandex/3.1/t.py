"""
# T. Польский калькулятор — 2

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Поздравляем! Это финальная, 20-я задача.
Вы уже уверенно работаете со строками, коллекциями и логикой обработки данных.

-
Операции, которые выполняются с одним значением, называются унарными, с двумя — бинарными, с тремя — тернарными.

Давайте улучшим наш калькулятор, добавив поддержку следующих операций:

- бинарные:
    - `'+'` (сложение),
    - `'-'` (вычитание),
    - `'*'` (умножение),
    - `'/'` (деление нацело; для отрицательных чисел работает по тем же правилам, что и в Python);
- унарные:
    - `'~'` (унарный минус — меняет знак),
    - `'!'` (факториал),
    - `'#'` (клонирование — вернуть в стек значение дважды);
- тернарные:
    - `'@'` (возвращает в стек те же три значения, но в ином порядке: второе, третье, первое).

## Формат ввода

Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций.
Вместе они составляют корректное выражение в обратной польской нотации,
не содержащее деления на ноль и взятия факториала от отрицательного числа.

## Формат вывода

Выводится одно целое число — результат вычисления выражения.
"""


addition_operator_symbol = '+'
change_order_operator_symbol = '@'
cloning_operator_symbol = '#'
exact_division_operator_symbol = '/'
factorial_operator_symbol = '!'
multiplication_operator_symbol = '*'
subtraction_operator_symbol = '-'
unary_minus_operator_symbol = '~'
binary_operator_symbols = (
    addition_operator_symbol,
    exact_division_operator_symbol,
    multiplication_operator_symbol,
    subtraction_operator_symbol,
)
unary_operator_symbols = (cloning_operator_symbol, factorial_operator_symbol, unary_minus_operator_symbol)
ternary_operator_symbols = (change_order_operator_symbol,)

parts = input().split()

numbers_stack = []
for part in parts:
    if part in unary_operator_symbols:
        a = numbers_stack.pop()
        match part:
            case _operator_1 if _operator_1 == cloning_operator_symbol:
                numbers_stack.append(a)
                numbers_stack.append(a)
            case _operator_2 if _operator_2 == factorial_operator_symbol:
                if a <= 1:
                    numbers_stack.append(1)
                    continue
                result = 2
                for i in range(3, a + 1):
                    result *= i
                numbers_stack.append(result)
            case _operator_3 if _operator_3 == unary_minus_operator_symbol:
                numbers_stack.append(-a)
        continue

    if part in binary_operator_symbols:
        b = numbers_stack.pop()
        a = numbers_stack.pop()
        match part:
            case _operator_1 if _operator_1 == addition_operator_symbol:
                numbers_stack.append(a + b)
            case _operator_2 if _operator_2 == exact_division_operator_symbol:
                numbers_stack.append(a // b)
            case _operator_3 if _operator_3 == multiplication_operator_symbol:
                numbers_stack.append(a * b)
            case _operator_4 if _operator_4 == subtraction_operator_symbol:
                numbers_stack.append(a - b)
        continue

    if part in ternary_operator_symbols:
        c = numbers_stack.pop()
        b = numbers_stack.pop()
        a = numbers_stack.pop()
        numbers_stack.append(b)
        numbers_stack.append(c)
        numbers_stack.append(a)
        continue

    numbers_stack.append(int(part))

print(numbers_stack[0])
