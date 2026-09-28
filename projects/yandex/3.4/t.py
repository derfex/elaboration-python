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

# region Calculate `expression_list`, `polish_calculator_expression_stack`, `variables_set`.
# Let me parse `expression` in one pass, symbol by symbol.
expression_index = 0
expression_length = len(expression)
expression_list = []
polish_calculator_expression_stack = []
polish_calculator_operations_stack = []
variables_set = set()
while expression_index < expression_length:
    symbol = expression[expression_index]
    if symbol.isupper():
        polish_calculator_expression_stack.append(symbol)
        expression_list.append(symbol)
        variables_set.add(symbol)
        expression_index += 1
        continue
    if symbol == group_begin_operation_symbol:
        polish_calculator_operations_stack.append(symbol)
        expression_list.append(symbol)
        expression_index += 1
        continue
    if symbol == group_end_operation_symbol:
        while polish_calculator_operations_stack[-1] != group_begin_operation_symbol:
            polish_calculator_expression_stack.append(polish_calculator_operations_stack.pop())
        polish_calculator_operations_stack.pop()
        expression_list.append(symbol)
        expression_index += 2
        continue
    if symbol == space_operation_symbol:
        expression_index += 1
        continue
    expression_operation = symbol
    while expression[expression_index + 1] != space_operation_symbol:
        expression_index += 1
        expression_operation += expression[expression_index]
    operation = operations_dict.get(expression_operation, expression_operation)
    while polish_calculator_operations_stack and (
        operations_priorities_dict[operation] >= operations_priorities_dict[polish_calculator_operations_stack[-1]]
    ):
        polish_calculator_expression_stack.append(polish_calculator_operations_stack.pop())
    polish_calculator_operations_stack.append(operation)
    expression_list.append(operation)
    expression_index += 2
while polish_calculator_operations_stack:
    polish_calculator_expression_stack.append(polish_calculator_operations_stack.pop())
# endregion Calculate `expression_list`, `polish_calculator_expression_stack`, `variables_set`.

values_tuples_iterator = product((False, True), repeat=len(variables_set))
variables_list = sorted(variables_set)

print(*variables_list, table_header_result_title)



exit()

# // TODO
