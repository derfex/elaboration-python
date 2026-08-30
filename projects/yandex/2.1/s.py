"""
# S. Украшение чека

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

На этот раз предлагаем решить задачу, которая научит вас форматировать строки с заданной длиной и выравниванием.

Давайте приведём в порядок чек, который печатали ранее.
Все строки должны быть длиной в 35 символов.

Напишите программу, которая выводит красиво оформленный чек.
Все строки в чеке должны быть длиной ровно 35 символов, текст выровнен в соответствии с примером.

## Формат ввода

- Название товара (строка);
- цена товара (натуральное число);
- вес товара (натуральное число);
- количество денег у пользователя (натуральное число).

## Формат вывода

Красивый чек в формате:

```
================Чек================
Товар:                    <продукт>
Цена:     <число>кг * <число>руб/кг
Итого:                   <число>руб
Внесено:                 <число>руб
Сдача:                   <число>руб
===================================
```
"""


string_total_length = 35
title_length = 9
formated_value_length = string_total_length - title_length

product_name = input()
product_price = int(input())
product_weight = int(input())
deposited = int(input())

price_formated = f'{product_weight}кг * {product_price}руб/кг'
total = product_weight * product_price
total_formated = f'{total}руб'
change_formated = f'{deposited - total}руб'

print(f"""\
================Чек================
Товар:   {product_name:>{formated_value_length}}
Цена:    {price_formated:>{formated_value_length}}
Итого:   {total_formated:>{formated_value_length}}
Внесено: {(str(deposited) + 'руб'):>{formated_value_length}}
Сдача:   {change_formated:>{formated_value_length}}
===================================\
""")
