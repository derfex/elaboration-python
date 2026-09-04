"""
# T. Математическая выгода

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Поздравляем! Вы дошли до финала — перед вами последняя, двадцатая задача!
Ваша настойчивость, внимание к деталям и логика — просто на высоте.

На этот раз — настоящая задача для мыслителя.

Виталий Евгеньевич задумался:
«А какая система счисления — самая выгодная?»

По его логике, выгодной считается та система счисления, в которой сумма цифр числа — наибольшая.
А если таких систем несколько — он выбирает наименьшее основание из них.

Ваша задача — помочь ему это выяснить!

## Формат ввода

Одно натурально число в десятичной СС.

## Формат вывода

Одно натуральное число из диапазона `[2;10]` — основание системы счисления с максимальной выгодой.
Если таких оснований несколько, выбирается наименьшее.
"""


number_system_base_max = 10
number_system_base_min = 2
number_system_bases = range(number_system_base_min, number_system_base_max + 1)

number_initial = int(input(), 10)

digits_sum_max = 0
result_base = number_system_base_min
for base in number_system_bases:
    digits_sum = 0
    number = number_initial
    while number:
        digits_sum += number % base
        number //= base
    if digits_sum > digits_sum_max:
        digits_sum_max = digits_sum
        result_base = base

print(result_base)
