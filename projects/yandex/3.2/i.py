"""
# I. Зайка — 9

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Поможем детям подсчитать, сколько животных и деревьев каждого вида встречается за окном поезда.

Напишите программу, которая по текстовому описанию местности подсчитывает,
сколько раз каждое слово встречается во входных данных.

## Формат ввода

В каждой строке записано описание придорожной местности.
Конец ввода обозначается пустой строкой.

## Формат вывода

Список увиденного и их количество.
Порядок вывода не имеет значения.
"""


terrain_description_objects_dict = dict()
while terrain_description_string := input():
    for terrain_description_object in terrain_description_string.split():
        if terrain_description_object in terrain_description_objects_dict:
            terrain_description_objects_dict[terrain_description_object] += 1
        else:
            terrain_description_objects_dict[terrain_description_object] = 1

for terrain_description_object, terrain_description_object_quantity in terrain_description_objects_dict.items():
    print(terrain_description_object, terrain_description_object_quantity)
