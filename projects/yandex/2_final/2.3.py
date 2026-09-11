"""
# 2.3. Анализ качества образовательной программы

## Ограничение времени

1 с

## Ограничение памяти

64.0 Мб

## Ввод

стандартный ввод или `input.txt`

## Вывод

стандартный вывод или `output.txt`

---

Поздравляем! Вот и последняя задача. Чтобы её решить, вам понадобятся наработки из предыдущих задач. Успехов!

Немного контекста: недавно начался образовательный курс по Python.
Прошло несколько недель — и настало время подвести первые итоги:
насколько курс усваивается учениками, и нужно ли в нём что-то менять.

Вас попросили собрать статистику по успеваемости учеников на курсе.

## Что нужно сделать

- Вывести общие показатели учеников программы:
  максимальное, среднее и минимальное значение рейтинга в процентах от максимально возможного.
- Округлить результаты до целого значения с помощью функции `round()`.
- Вывести лучших учеников:
  топ-3 лидера по рейтингу,
  их фамилии в порядке убывания рейтинга и заработанный процент от максимального количества баллов.
  Если у студентов равный рейтинг (в абсолютном значении), то они идут в порядке их ввода —
  кто первый указан, тот выше по рейтингу и находится.
  Фамилии учеников уникальны.
- На основе данных сделать предварительный вывод, насколько усваивается курс:
    - Если среднее значение рейтинга <= 50 — курс усваивается плохо.
    - Если среднее значение рейтинга > 50 — курс усваивается хорошо.

Также нужно проверить правильность введённых данных и расчётов.
Если есть ошибки, выводим строку `'Во введённых данных ошибка'`.

## Формат ввода

Одна строчка, в которой через пробел подаются следующие данные:
```
N M Q cw sw hw tw
```
`N` (`num_students`) — число учеников на курсе
`M` (`num_lessons`) — количество занятий в курсе
`Q` (`max_rating`) — максимальный рейтинг
`cw` (`classwork_coefficient`) — коэффициент для активности на занятии
`sw` (`selfwork_coefficient`) — коэффициент для практики
`hw` (`homework_coefficient`) — коэффициент для домашней работы
`tw` (`testwork_coefficient`) — коэффициент для контрольной работы

Далее идут фамилии учеников (`N`) и несколько строчек (`M`) с оценками ученика на занятиях в формате:

```
Иванов
a₁,b₁,c₁,d₁
a₂,b₂,c₂,d₂
a₃,b₃,c₃,d₃
⋮
aₘ,bₘ,cₘ,dₘ
Сидоров
…
```

Где `aᵢ,bᵢ,cᵢ,dᵢ` — это оценки за `i`-ое занятие:

`aᵢ` (`classwork_grade`) — оценка за активность на занятии
`bᵢ` (`selfwork_grade`) — оценка за практику на занятии
`cᵢ` (`homework_grade`) — оценка за домашнюю работу на занятии
`dᵢ` (`testwork_grade`) — оценка за контрольную работу на занятии

Если не было активности, ученик отсутствовал либо не проявил себя на занятии — значение за активность будет `0`.

## Формат вывода

Построчно в следующей последовательности:

- Максимальный, средний и минимальный рейтинг учеников программы.
  Через пробел, округлённый до целого числа с помощью `round()`.
- Построчно фамилию и процент от максимального рейтинга,
  округлённый до целого числа с помощью функции `round()` (через пробел), трёх лидеров рейтинга.
- Предварительный вывод «как усваивается курс» (хорошо или плохо).

```
Max Average Min (максимальный, средний и минимальный рейтинг учеников программы)
Фамилия_1 Rating_1% (top-1)
Фамилия_2 Rating_2% (top-2)
Фамилия_3 Rating_3% (top-3)
Курс усваивается хорошо/плохо
```

Также сделайте проверку на верность вводных данных.
Если условие не выполняется, то необходимо вывести строку `'Во введённых данных ошибка'`.

- `N >= 3` (количество учеников больше или равно `3`)
- `M > 0` (количество проведённых занятий `1` и больше)
- `cw, sw, hw, tw > 0` (все активности учитываются в рейтинге)
- Рассчитанный максимальный рейтинг ученика на программе не должен превышать `Q`.
"""


course_is_not_well_understood_message = 'Курс усваивается плохо'
course_is_well_understood_message = 'Курс усваивается хорошо'
students_quantity_min = 3
wrong_input_message = 'Во введённых данных ошибка'

students_quantity, lessons_quantity, max_rating, cw, sw, hw, tw = map(int, input().split())

if students_quantity < students_quantity_min or lessons_quantity <= 0 or cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0:
    print(wrong_input_message)
else:
    result_student_rating_min = max_rating
    result_student_1_rating = -1
    result_student_1_surname = ''
    result_student_2_rating = -1
    result_student_2_surname = ''
    result_student_3_rating = -1
    result_student_3_surname = ''
    student_rating_sum = 0
    for _ in range(students_quantity):
        student_rating = 0
        student_surname = input()
        for _ in range(lessons_quantity):
            a, b, c, d = map(int, input().split(','))
            student_rating += a * cw + b * sw + c * hw + d * tw
        if student_rating > max_rating:
            print(wrong_input_message)
            break
        result_student_rating_min = min(result_student_rating_min, student_rating)
        student_rating_sum += student_rating

        # Calculate top 3 places.
        if student_rating > result_student_1_rating:
            result_student_3_rating = result_student_2_rating
            result_student_3_surname = result_student_2_surname
            result_student_2_rating = result_student_1_rating
            result_student_2_surname = result_student_1_surname
            result_student_1_rating = student_rating
            result_student_1_surname = student_surname
        elif student_rating > result_student_2_rating:
            result_student_3_rating = result_student_2_rating
            result_student_3_surname = result_student_2_surname
            result_student_2_rating = student_rating
            result_student_2_surname = student_surname
        elif student_rating > result_student_3_rating:
            result_student_3_rating = student_rating
            result_student_3_surname = student_surname
    result_student_1_rating = round(result_student_1_rating * 100 / max_rating)
    result_student_2_rating = round(result_student_2_rating * 100 / max_rating)
    result_student_3_rating = round(result_student_3_rating * 100 / max_rating)

    result_student_rating_average = round(student_rating_sum / students_quantity * 100 / max_rating)
    result_student_rating_max = result_student_1_rating
    result_student_rating_min = round(result_student_rating_min * 100 / max_rating)

    if result_student_rating_average > 50:
        course_understanding_message = course_is_well_understood_message
    else:
        course_understanding_message = course_is_not_well_understood_message

    print(result_student_rating_max, result_student_rating_average, result_student_rating_min)
    print(f'{result_student_1_surname} {result_student_1_rating}%')
    print(f'{result_student_2_surname} {result_student_2_rating}%')
    print(f'{result_student_3_surname} {result_student_3_rating}%')
    print(course_understanding_message)
