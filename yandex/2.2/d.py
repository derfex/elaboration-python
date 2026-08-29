"""
# D. Список победителей

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или input.txt

## Вывод

стандартный вывод или output.txt

---

В этой задаче вы продолжите работать с операторами, но добавим к этому наивную сортировку данных.

Время подвести итоги гонки и объявить победителя!
Длина трассы — 43872 метра, и нам известны средние скорости трёх фаворитов: Пети, Васи и Толи.
Ваша задача — сравнить результаты гонщиков и вывести имя победителя.

## Формат ввода

В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Все скорости различны.

## Формат вывода

Имена победителей в порядке занятых мест.
"""


rider_1_name = 'Петя'
rider_2_name = 'Вася'
rider_3_name = 'Толя'

rider_1_speed = float(input())
rider_2_speed = float(input())
rider_3_speed = float(input())

if rider_1_speed > rider_2_speed and rider_1_speed > rider_3_speed:
    place_1_name = rider_1_name
    if rider_2_speed > rider_3_speed:
        place_2_name = rider_2_name
        place_3_name = rider_3_name
    else:
        place_2_name = rider_3_name
        place_3_name = rider_2_name
elif rider_2_speed > rider_3_speed:
    place_1_name = rider_2_name
    if rider_1_speed > rider_3_speed:
        place_2_name = rider_1_name
        place_3_name = rider_3_name
    else:
        place_2_name = rider_3_name
        place_3_name = rider_1_name
else:
    place_1_name = rider_3_name
    if rider_1_speed > rider_2_speed:
        place_2_name = rider_1_name
        place_3_name = rider_2_name
    else:
        place_2_name = rider_2_name
        place_3_name = rider_1_name

print(f'''\
1. {place_1_name}
2. {place_2_name}
3. {place_3_name}\
''')
