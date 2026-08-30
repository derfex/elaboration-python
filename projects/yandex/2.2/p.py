"""
# P. Легенды велогонок возвращаются: кто быстрее?

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Ура! Зерон повержен, и это всё благодаря вам! Герои заслужили отдых.
Сделайте короткую паузу, чтобы восстановить силы, и возвращайтесь, когда будете готовы.

Осталось ещё 4 задачи!
Давайте освежим в памяти,
как работать с вложенными условными операторами `if-else` или `if-elif-else` и применять наивную сортировку данных.

В новом сезоне за первенство в велогонках снова сражаются сильнейшие.
Протяжённость финальной трассы — 43872м, и все хотят узнать, кто первым пересечёт финишную черту.

Нам известны средние скорости трёх претендентов — Пети, Васи и Толи. Кто станет победителем?

## Формат ввода

В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

## Формат вывода

Красивый пьедестал (ширина ступеней 8 символов).
"""


step_length = 8
step_empty_placeholder = ' ' * step_length

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

print(f"""\
{step_empty_placeholder}{place_1_name:^{step_length}}{step_empty_placeholder}
{place_2_name:^{step_length}}{step_empty_placeholder}{step_empty_placeholder}
{step_empty_placeholder}{step_empty_placeholder}{place_3_name:^{step_length}}
{'II':^{step_length}}{'I':^{step_length}}{'III':^{step_length}}\
""")
