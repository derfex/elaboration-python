"""
# T. Таблица истинности 3

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Поздравляем, это последняя задача в параграфе!

На этот раз придётся справиться с выражением, в котором встречаются нестандартные логические операции:
импликация, строгая дизъюнкция и эквивалентность.
Они не поддерживаются в Python напрямую, но вы сможете реализовать их самостоятельно.

Напишите программу, которая для заданного логического выражения строит таблицу истинности, включая поддержку следующих операций:

- `->` — импликация
- `^` — строгая дизъюнкция
- `~` — эквивалентность

## Формат ввода

Вводится логическое выражение от нескольких переменных.

Возможное содержание выражения:

- Заглавная латинская буква — переменная;
- `not` — отрицание;
- `and` — конъюнкция;
- `or` — дизъюнкция;
- `^` — строгая дизъюнкция;
- `->` — импликация;
- `~` — эквивалентность;
- `()` — логические скобки.

-## Формат вывода

Выведите таблицу истинности данного выражения.
"""


# // TODO

from itertools import product

# region Operations
space_operation_symbol = ' '
group_begin_operation_symbol = '('
group_end_operation_symbol = ')'
# endregion Operations
operations_dict = {
    '->': '<=',
    '^': '!=',
    '~': '==',
}
operations_priorities_list = ['not', 'and', 'or', '!=', '<=', '==', group_begin_operation_symbol]
operations_priorities_dict = {
    operation: priority
    for priority, operation in enumerate(operations_priorities_list)
}
table_header_result_title = 'F'

expression = input()

# Let me parse `expression` in one pass, symbol by symbol.
expression_index = 0
expression_length = len(expression)
expression_list = []
variables_set = set()
while expression_index < expression_length:
    symbol = expression[expression_index]
    if symbol.isupper():
        expression_list.append(symbol)
        variables_set.add(symbol)
        expression_index += 1
        continue
    if symbol == group_begin_operation_symbol:
        expression_list.append(symbol)
        expression_index += 1
        continue
    if symbol == group_end_operation_symbol:
        expression_list.append(symbol)
        expression_index += 2
        continue
    if symbol == space_operation_symbol:
        expression_index += 1
        continue
    operation = symbol
    while expression[expression_index + 1] != space_operation_symbol:
        expression_index += 1
        operation += expression[expression_index]
    expression_list.append(operations_dict.get(operation, operation))
    expression_index += 2

# // TODO
