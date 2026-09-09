"""
# J. Частотный анализ на минималках

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Частотный анализ — это метод подсчёта, какие символы (или слова) чаще всего встречаются в тексте.
Это важнейший инструмент взлома многих классических шифров — от шифра Цезаря и до шифровальной машины «Энигма».

В этой задаче вы реализуете простейшую версию частотного анализа:
выясните, какая буква встречается чаще других в тексте.

Напишите программу, которая читает строки до тех пор, пока не встретится строка `'ФИНИШ'`,
и выводит наиболее часто встречающуюся букву (в нижнем регистре).

## Формат ввода

Вводятся строки, пока не будет введена строка `'ФИНИШ'`.

## Формат вывода

Выводится один символ в нижнем регистре — наиболее часто встречающийся во введённой строке.

## Примечания

Пробелы в анализе не участвуют.
Если в результате анализа получено несколько ответов, следует вывести первый по алфавиту.

У данной задачи множество «быстрых» способов решения,
но в этом параграфе мы просим вас сосредоточиться на использовании строк и списков.
"""


letters = []
letters_count = 0
letters_counts = []
stop_command = 'ФИНИШ'

# Calculate counts of the letters.
while (string := input()) != stop_command:
    for letter in string:
        if letter == ' ':
            continue
        letter = letter.lower()
        if letter in letters:
            letters_count += 1
            index = letters.index(letter)
            letters_counts[index] += 1
        else:
            letters.append(letter)
            letters_counts.append(1)

# Among the most frequent letters, find the lexicographically smallest one.
letters_count_max = max(letters_counts)
result_letter = chr(ord('ё') + 1)
for i in range(letters_count):
    letters_count_max_index = letters_counts[i:].index(letters_count_max)
    letter_with_max_count = letters[letters_count_max_index]
    result_letter = min(result_letter, letter_with_max_count)

print(result_letter)
