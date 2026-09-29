"""
# P. Расклад таков…

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Осталось всего 5 задач — вы уже почти на финишной прямой!

Можно налить себе чай перед следующей задачей — и снова в бой!
Виталий любит играть в карты.
Он решил выяснить, какие есть вариации вытащить из колоды определённые тройки карт.
Напишите программу, которая выводит список подходящих троек в лексикографическом порядке с учётом заданных условий.

## Формат ввода

В первой строке записана масть, которая должна присутствовать в тройке.
Во второй строке записано достоинство, которого не должно быть в тройке.

## Формат вывода

Выведите на экран первые 10 получившихся троек.
Карты в каждой комбинации должны быть отсортированы лексикографически (по строке названия карты).
Карты комбинации выводятся через запятую с пробелом после неё.
Комбинации между собой также должны быть отсортированы в лексикографическом порядке по строке,
представляющей комбинацию целиком.

## Примечание

Обратите внимание: валет-дама-король-туз лексикографически упорядочены.
Но «10 …» лексикографически младше, чем «2 …», а бубны младше, чем пики.

Масти в именительном и родительном падежах:
(Именительный — Родительный)
- буби — бубен
- пики — пик
- трефы — треф
- черви — червей
"""


from itertools import combinations, islice, product

print_separator = ', '
suits_dict = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
triplets_quantity = 10
weights_tuple = tuple(['10'] + [str(weight) for weight in range(2, 10)] + ['валет', 'дама', 'король', 'туз'])

included_suit = input()
excluded_weight = input()

allowed_weights_tuple = tuple(weight for weight in weights_tuple if weight != excluded_weight)
allowed_deck_tuple = tuple(
    ' '.join(weight_and_suit_tuple)
    for weight_and_suit_tuple in product(allowed_weights_tuple, suits_dict.values())
)
triplets_iterator = combinations(allowed_deck_tuple, 3)
prepared_included_suit = suits_dict[included_suit]
result_triplets_iterator = islice(tuple(
    triplet_tuple
    for triplet_tuple in triplets_iterator
    if prepared_included_suit in str(triplet_tuple)
), triplets_quantity)

for result_triplet_tuple in result_triplets_iterator:
    print(*result_triplet_tuple, sep=print_separator)
