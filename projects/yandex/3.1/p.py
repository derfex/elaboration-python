"""
# P. Анонс новости 2.0

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Поздравляем! Вы уже прошли три четверти всех задач этого параграфа — 15 из 20.
Финиш совсем близко. Можно сделать короткий перерыв — или двинуться дальше с новыми силами. Решать вам!

Вы снова работаете над лентой новостей для сайта.
Теперь заголовки могут занимать несколько строк, но при этом всё равно нужно соблюдать лимит:
если заголовок слишком длинный — он должен быть сокращён и завершён многоточием `'...'`.

Эта задача поможет вам научиться учитывать длину строк, переносы и условия обрезки текста.

Напишите программу, которая по заданному количеству строк и максимально допустимой длине:

- выводит заголовок, при необходимости обрезая его;
- если заголовок слишком длинный — заменяет последние символы на `'...'`;
- если строки заканчиваются слишком коротко, `'...'` может перейти в предыдущую строку.

## Формат ввода

Вводится натуральное число `L` — необходимая длина заголовка.
Вводится натуральное число `N` — количество строк в заголовке новости.
В каждой из последующих `N` строк записано по одной строке заголовка.

## Формат вывода

Сокращённый заголовок.

## Примечание

Многоточие учитывается при подсчёте длины заголовка.
Символ перевода строки при подсчёте длины не учитывается.
"""


ellipsis_suffix = '...'
ellipsis_suffix_length = len(ellipsis_suffix)

title_max_length = int(input())
title_strings_quantity = int(input())

total_length = 0
title_strings = []

for title_string_index in range(title_strings_quantity):
    title_string = input()
    title_string_length = len(title_string)
    forecast_length = total_length + title_string_length
    if forecast_length <= title_max_length:
        title_strings.append(title_string)
        total_length += title_string_length
    else:
        allowed_length = title_max_length - total_length - ellipsis_suffix_length
        if allowed_length < 0:
            # We make the assumption that `title_strings_quantity > 1`.
            previous_index = title_string_index - 1
            title_strings[previous_index] = title_strings[previous_index][:allowed_length] + ellipsis_suffix
            break
        title_strings.append(title_string[:allowed_length] + ellipsis_suffix)
        break

print('\n'.join(title_strings))
