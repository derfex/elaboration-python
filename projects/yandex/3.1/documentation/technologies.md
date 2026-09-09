# Yandex. 3.1. Technologies

## Used

### Python

#### Input and output

- `input()`
- `print()`

#### Numeric Types — `int`, `float`, `complex`

##### Numbers operations

- `42 + 42`
- `42 - 42`
- `42 * 42`
- `42 // 42`
- `42 % 42`
- `42 ** 42`
- `num += 42`
- `num *= 42`

###### Numbers comparison

- `42 != 42`
- `42 >= 42`, `42 <= 42`

##### `int`

- `int()`

#### Sequence Types — `list`, `tuple`, `range`

##### `list`

Doc: `class list(iterable=(), /)`.

- `list()`

- `list_value[index]`, `list_value[-index]`

###### Lists operations

- `value in list_value`, `value not in list_value`

###### Lists functions

- `len(list_value)`
- `max(list_value)`

###### Lists methods

- `list_variable.append(list_item_value)`
- `list_variable.index(list_item_value)`
- `list_variable.pop()`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `(42, )`, `(42, 4.2)`

###### Tuples operations

- `value in tuple_value`, `value not in tuple_value`

#### Text Sequence Type — `str`

- `string_value[index]`, `string_value[-index]`
- `string_value[i:j]`, `string_value[i:j:k]`

##### Strings operations

- `string_value_1 + string_value_2`

###### Strings comparison

- `'str' == 'str'`, `'str' != 'str'`
- `'str' in 'str'`

- `chr(42)`
- `ord('ё')`
- `len('str')`

##### `str`

- `str(42)`

- `'str str'.count('str')`
- `'str str'.endswith('str')`
- `'str str'.find('str')`
- `'str str'.join(['str', 'str'])`
- `'str str'.lower()`
- `'str str'.rstrip('str')`
- `'str str'.split('str')`
- `'str str'.startswith('str')`
- `'str str'.upper()`

- `min('str', 'str')`

#### Set Types — `set`, `frozenset`

##### `set`

- `variable_1, variable_2 = expression_1, expression_2`

#### Conditions

- `if condition:`, `elif condition:`, `else:`
- `match subject_expression:`, `case value:`
- `match … case variable if expression:`
- `condition_1 or condition_2`
- `not condition`

#### Loops

- `for variable in iterable_value:`
- `while condition:`
- `break`
- `continue`

#### Other

- `variable := expression`
- `map()`
- `a, b = <map object>`
