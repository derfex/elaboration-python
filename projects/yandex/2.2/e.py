"""
# E. Яблоки

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Как насчёт небольшой головоломки с применением условного оператора?

У Пети было 7 яблок, а у Васи 6.
Затем Петя отдал 3 яблока Васе, а у Толи взял 2 яблока.
Вася попросил у Толи 5 яблок, но отдал Гене 2.
Затем Дима дал Пете `N` яблок, а Васе `M`.

Так у кого в итоге яблок больше — у Пети или Васи?

## Формат ввода

В первой строке записано натуральное число `N`.
Во второй — `M`.

## Формат вывода

Имя ребёнка, у которого больше яблок.

## Примечание

Гарантируется, что у всех детей оказалось разное количество яблок.
"""


petya_apples = 7
petya_name = 'Петя'
vasya_apples = 6
vasya_name = 'Вася'

petya_apples -= 3
vasya_apples += 3
petya_apples += 2
vasya_apples += 5 - 2

dima_to_petya_apples = int(input())
dima_to_vasya_apples = int(input())

petya_apples += dima_to_petya_apples
vasya_apples += dima_to_vasya_apples

if petya_apples > vasya_apples:
    print(petya_name)
else:
    print(vasya_name)
