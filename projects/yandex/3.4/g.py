"""
# G. Игровая сетка

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Ребята в классе решили устроить чемпионат по шашкам по принципу «каждый с каждым».
Напишите программу, которая составляет список всех возможных игр между учениками.

## Формат ввода

В первой строке записано число учеников (`N`).
В каждой из последующих `N` строк записано одно имя.

## Формат вывода

Список игр в формате:
`<Игрок 1> - <Игрок 2>`
Порядок игр не имеет значения.
"""


from itertools import combinations

players_separator = ' - '

combinations_pull = frozenset(input() for _ in range(int(input())))  # player_name, players_quantity

for player_1_name, player_2_name in combinations(combinations_pull, 2):
    print(player_1_name, player_2_name, sep=players_separator)
