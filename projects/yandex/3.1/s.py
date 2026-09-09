"""
# S. Польский калькулятор

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Осталась всего одна задача до финиша — вы почти дошли до конца третьего параграфа!
Сейчас — вызов на логику: реализуем калькулятор на основе обратной польской нотации (ОПН).

В ОПН нет скобок и приоритета операций — всё вычисляется строго слева направо, с помощью стека.
Вы добавляете числа в стек, а когда встречаете оператор (`'+'`, `'-'`, `'*'`) —
извлекаете два последних числа, применяете операцию и возвращаете результат обратно в стек.

Напишите программу, которая по введённому выражению в ОПН вычисляет результат.

## Формат ввода

Вводится одна строка, содержащая разделённые пробелами целые числа и знаки операций `'+'`, `'-'`, `'*'`,
которые вместе составляют корректное выражение в обратной польской нотации.

## Формат вывода

Выводится одно целое число — результат вычисления выражения.
"""


addition_operator_symbol = '+'
multiplication_operator_symbol = '*'
subtraction_operator_symbol = '-'
operator_symbols = (addition_operator_symbol, subtraction_operator_symbol, multiplication_operator_symbol)

parts = input().split()

numbers_stack = []
for part in parts:
    if part in operator_symbols:
        b = numbers_stack.pop()
        a = numbers_stack.pop()
        match part:
            case _operator_1 if _operator_1 == addition_operator_symbol:
                numbers_stack.append(a + b)
            case _operator_2 if _operator_2 == multiplication_operator_symbol:
                numbers_stack.append(a * b)
            case _operator_3 if _operator_3 == subtraction_operator_symbol:
                numbers_stack.append(a - b)
        continue

    numbers_stack.append(int(part))

print(numbers_stack[0])
