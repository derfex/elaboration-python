"""
# P. Зайка — 10

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Ого, уже 15 задач позади! Вы приближаетесь к финишу — осталось всего 5. Можно немного выдохнуть и продолжить.

Дети в поезде снова играют в любимую игру — считать зверей за окном.
На этот раз их заинтересовало, что находится рядом с зайками. Поможем им разобраться!

Напишите программу, которая по описанию придорожной местности находит все объекты,
стоящие рядом с зайками — слева или справа от слова зайка.

## Формат ввода

В каждой строке записано описание придорожной местности.
Конец ввода обозначается пустой строкой.

## Формат вывода

Определите список увиденного рядом с зайками без повторений.
Порядок вывода не имеет значения.

## Примечание

Считается, что объект находится рядом, если он записан справа или слева от требуемого.
"""


# I am making the assumption that `'зайка'` does not appear more than once in a row inside `terrain_description_string`.

sought_after = 'зайка'

terrain_description_objects_set = set()
while terrain_description_string := input():
    terrain_description_objects_tuple = tuple(terrain_description_string.split())
    for terrain_object_index, terrain_object in enumerate(terrain_description_objects_tuple):
        if terrain_object != sought_after:
            continue
        if terrain_object_index > 0:
            terrain_description_objects_set.add(terrain_description_objects_tuple[terrain_object_index - 1])
        if terrain_object_index < len(terrain_description_objects_tuple) - 1:
            terrain_description_objects_set.add(terrain_description_objects_tuple[terrain_object_index + 1])

print(*terrain_description_objects_set, sep='\n')
