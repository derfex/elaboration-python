"""
# M. Дайте чего-нибудь новенького!

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Главный повар детского сада готовит меню на праздник и хочет выбрать блюда,
которые ни разу не подавались на этой неделе.

В его распоряжении есть список блюд:

- тех, что можно приготовить в столовой сегодня;
- тех, что были приготовлены в каждый из дней недели.

Напишите программу,
которая по списку доступных сегодня блюд и истории приготовления на неделе определяет,
что из этого можно приготовить нового.

## Формат ввода

Число блюд (`N`), которые можно приготовить в столовой.
`N` строк с названиями блюд.
Число дней (`M`), о которых имеется информация.
`M` блоков строк для каждого из списков.
В первой строке каждого блока записано число блюд в заданный день, затем перечисляются эти блюда.

## Формат вывода

Список блюд, которые ещё не готовились на этой неделе в алфавитном порядке.
Если все возможные блюда уже были приготовлены, следует вывести `'Готовить нечего'`.
"""


not_found_message = 'Готовить нечего'

available_dishes_quantity = int(input())
available_dishes_set = set()
for _ in range(available_dishes_quantity):
    available_dishes_set.add(input())  # available_dish_name

days_quantity = int(input())
dishes_that_were_already_being_cooked_set = set()
for _ in range(days_quantity):
    for _ in range(int(input())):  # dishes_for_day_quantity
        dishes_that_were_already_being_cooked_set.add(input())  # dish_that_was_already_being_cooked_name

new_dishes_set = frozenset(available_dishes_set - dishes_that_were_already_being_cooked_set)

if len(new_dishes_set):
    new_dishes_list = sorted(new_dishes_set)
    print(*new_dishes_list, sep='\n')
else:
    print(not_found_message)
