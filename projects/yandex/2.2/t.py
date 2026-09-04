"""
# T. Зайка — 2

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

И это последняя задачка! Ура!

По пути домой родители снова решили сыграть с детьми в поиск зверушек.
Но на этот раз задача сложнее — нужно не просто найти зайку, а выбрать правильную строку по определённым условиям.

Вам предстоит проверить три строки, найти среди них ту, где встречается слово «зайка», и вывести её вместе с её длиной.
Если таких строк несколько, выберите наименьшую в алфавитном порядке.

Для этого используйте составные условные операции, чтобы одновременно учесть несколько условий.

## Формат ввода

Три строки описывающих придорожную местность.

## Формат вывода

Строка в которой есть зайка, а затем её длина.
Если таких строк несколько, выбрать ту, что меньше всех лексикографически.
"""


sought_after = 'зайка'

terrain_description_1 = input()
terrain_description_2 = input()
terrain_description_3 = input()

result_terrain_description = ''
if sought_after in terrain_description_1:
    result_terrain_description = terrain_description_1
if sought_after in terrain_description_2:
    if result_terrain_description == '':
        result_terrain_description = terrain_description_2
    else:
        result_terrain_description = min(result_terrain_description, terrain_description_2)
if sought_after in terrain_description_3:
    if result_terrain_description == '':
        result_terrain_description = terrain_description_3
    else:
        result_terrain_description = min(result_terrain_description, terrain_description_3)

print(result_terrain_description, len(result_terrain_description))
