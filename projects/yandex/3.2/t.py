"""
# T. Простая задача 4.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Поздравляем с финальной задачей!
Вы проделали отличную работу и дошли до конца — впереди последняя, двадцатая задача.
Она не простая, но вы уже вооружены знаниями о множествах, словарях и алгоритмах.

Напомним, что взаимно простыми называются числа, которые не имеют общих делителей, кроме 1.

Напишите программу, которая:

- получает список чисел, разделённых точкой с запятой и пробелом;
- для каждого числа определяет, с какими другими числами оно взаимно просто;
- выводит результат в порядке возрастания чисел без повторений;
- если для числа не найдено ни одного взаимно простого числа — его не нужно выводить вовсе.

## Формат ввода

Задана последовательность чисел, записанных через точку с запятой (`';'`) и пробел.

## Формат вывода

Список чисел с указанием взаимно простых ему среди переданных.
Все числа должны быть выведены в порядке возрастания без повторений.
Строки следует отформатировать по правилу:
`число - взаимно простое 1, взаимно простое 2, …`
Если для числа не было найдено ни одного взаимно простого, то и выводить его не требуется.
"""


numbers_list = sorted(map(int, frozenset(input().split('; '))))

numbers_list_length = len(numbers_list)
# `mutually_prime_numbers_dict` — for the numbers in the future (`numbers_list[j]`).
mutually_prime_numbers_dict = dict()
for i in range(numbers_list_length):
    number_1_initial = numbers_list[i]
    # `mutually_prime_numbers_list` — for the “current” number (`numbers_list[i]`).
    mutually_prime_numbers_list = mutually_prime_numbers_dict.pop(number_1_initial, [])
    for j in range(i + 1, numbers_list_length):
        number_1 = number_1_initial
        number_2 = number_2_initial = numbers_list[j]
        while number_2:
            number_1, number_2 = number_2, number_1 % number_2
        if number_1 != 1:
            continue
        mutually_prime_numbers_list.append(str(number_2_initial))
        if number_2_initial in mutually_prime_numbers_dict:
            mutually_prime_numbers_dict[number_2_initial].append(str(number_1_initial))
        else:
            mutually_prime_numbers_dict[number_2_initial] = [str(number_1_initial)]
    if mutually_prime_numbers_list:
        print(number_1_initial, '-', ', '.join(mutually_prime_numbers_list))
