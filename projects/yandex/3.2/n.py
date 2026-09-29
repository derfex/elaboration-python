"""
# N. Это будет шедевр!

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Главный повар детского сада хочет быстрее определять, какие блюда можно приготовить на обед.
У него есть список доступных продуктов и список рецептов.

Напишите программу, которая по списку имеющихся продуктов и рецептам определяет, какие блюда можно приготовить.

## Формат ввода

Число продуктов (`N`), которые имеются в наличии.
`N` строк с названиями продуктов.
Число рецептов (`M`), о которых имеется информация.
`M` блоков строк для каждого из рецептов.
В первой строке каждого блока записано название блюда.
Во второй — число ингредиентов.
Затем перечисляются сами ингредиенты, требуемые для приготовления блюда.

## Формат вывода

Список блюд, которые можно приготовить в алфавитном порядке.
Если ни одно из блюд нельзя приготовить, следует вывести `'Готовить нечего'`.
"""


not_found_message = 'Готовить нечего'

available_products_quantity = int(input())
available_products_set = set()
for _ in range(available_products_quantity):
    available_products_set.add(input())

available_recipes_set = set()
recipes_quantity = int(input())
for _ in range(recipes_quantity):
    recipe_name = input()
    recipe_is_available = True
    for _ in range(int(input())):  # ingredients_quantity
        ingredient_name = input()
        if not recipe_is_available:
            continue
        if ingredient_name not in available_products_set:
            recipe_is_available = False
    if recipe_is_available:
        available_recipes_set.add(recipe_name)

if len(available_recipes_set):
    available_recipes_list = sorted(available_recipes_set)
    print(*available_recipes_list, sep='\n')
else:
    print(not_found_message)
