"""
# Q. А есть ещё варианты?

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Давайте вновь поможем Виталию — теперь его интересует, какой вариант расклада идёт сразу после уже полученного.
Напишите программу, которая находит следующий подходящий вариант тройки карт, соответствующий условиям.

## Формат ввода

В первой строке записана масть, которая должна присутствовать в тройке.
Во второй строке записано достоинство, которого не должно быть в тройке.
В третьей строке записан предыдущий вариант, полученный Виталием.

## Формат вывода

Выведите следующий вариант расклада.

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


from itertools import combinations, product

print_separator = ', '
suits_dict = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
weights_tuple = tuple(['10'] + [str(weight) for weight in range(2, 10)] + ['валет', 'дама', 'король', 'туз'])

included_suit = input()
excluded_weight = input()
previous_triplet = input()

allowed_weights_tuple = tuple(weight for weight in weights_tuple if weight != excluded_weight)
allowed_deck_tuple = tuple(
    ' '.join(weight_and_suit_tuple)
    for weight_and_suit_tuple in product(allowed_weights_tuple, suits_dict.values())
)
triplets_iterator = combinations(allowed_deck_tuple, 3)
prepared_included_suit = suits_dict[included_suit]
result_triplets_iterator = (
    triplet_tuple
    for triplet_tuple in triplets_iterator
    if prepared_included_suit in str(triplet_tuple)
)

need_to_print = False
for result_triplet_tuple in result_triplets_iterator:
    triplet_string = print_separator.join(result_triplet_tuple)
    if need_to_print:
        print(triplet_string)
        break
    if triplet_string == previous_triplet:
        need_to_print = True
