"""
# Q. Друзья друзей

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Теория шести рукопожатий гласит,
что любые два человека на планете могут быть связаны друг с другом через максимум шесть знакомых.
Но мы не будем идти так далеко — давайте ограничимся двумя уровнями знакомства.

Напишите программу,
которая по списку пар друзей для каждого человека определяет список его друзей второго уровня
— то есть друзей его друзей, исключая его самого и его непосредственных друзей.

## Формат ввода

В каждой строке записывается два имени.
Окончанием ввода служит пустая строка.

## Формат вывода

Выведите список всех людей и их «друзей 2-го уровня» в формате «Человек: Друг1, Друг2, …».
Список людей и друзей в каждой строке требуется вывести в алфавитном порядке без повторений.
"""


people_dict = dict()
while string := input():
    surname_1, surname_2 = string.split()
    if surname_1 in people_dict:
        people_dict[surname_1].add(surname_2)
    else:
        people_dict[surname_1] = {surname_2}
    if surname_2 in people_dict:
        people_dict[surname_2].add(surname_1)
    else:
        people_dict[surname_2] = {surname_1}

people_list = sorted(people_dict.keys())
for surname_level_0 in people_list:
    surnames_level_1_set = people_dict[surname_level_0]
    surnames_level_2_set = set()
    for surname_level_1 in surnames_level_1_set:
        surnames_level_2_set = surnames_level_2_set.union(people_dict[surname_level_1])
    surnames_levels_0_and_1_set = frozenset(surnames_level_1_set.union({surname_level_0}))
    friends_level_2_set = frozenset(surnames_level_2_set.difference(surnames_levels_0_and_1_set))
    friends_level_2_list = sorted(friends_level_2_set)
    print(f'{surname_level_0}: ', end='')
    print(*friends_level_2_list, sep=', ')
