"""
# S. Таблица истинности 2

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Продолжим работу с таблицами истинности.
Теперь выражения могут содержать переменное количество переменных, обозначенных заглавными латинскими буквами.

Напишите программу, которая строит таблицу истинности для заданного логического выражения.

## Формат ввода

Вводится логическое выражение от нескольких переменных валидное для языка Python.
Все переменные заданы заглавными латинскими буквами.

## Формат вывода

Выведите таблицу истинности данного выражения.
"""


from itertools import product

table_header_result_title = 'F'

expression = input()

# region Calculate `variables_list` and `variables_quantity`
variables_set = set()
for symbol in expression:
    if symbol.isupper() and symbol not in variables_set:
        variables_set.add(symbol)
variables_list = sorted(variables_set)
variables_quantity = len(variables_set)
# endregion Calculate `variables_list` and `variables_quantity`

values_tuples_iterator = product((False, True), repeat=variables_quantity)

print(*variables_list, table_header_result_title)
for values in values_tuples_iterator:
    variables_and_values_iterator = zip(variables_list, values)
    eval_locals = {variable_as_key: value for variable_as_key, value in variables_and_values_iterator}
    print(*[int(v) for v in values], int(eval(expression, {}, eval_locals)))
