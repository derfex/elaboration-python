# Yandex. 3.4. Technologies. Used

Used technologies.

## Python

### Input and output

- `input()`
- `print()`
  - `print(value_1, value_2, end=string_value)`
  - `print(value_1, value_2, sep=string_value)`

### Numeric Types — `int`, `float`, `complex`

#### Numbers operations

- `42 + 42`
- `42 - 42`
- `42 * 42`
- `num += 42`
- `num //= 42`

##### Numbers comparison

- `42 > 42`, `42 < 42`
- `42 >= 42`, `42 <= 42`

#### `float`

- `float('4.2')`

#### `int`

- `int()`
  - `int('42')`

### Boolean Type — `bool`

- `False`, `True`

### Iterator Types

#### Iterators operations

- `*iterable_value`

#### Iterators functions

- `iter(iterable_value, /)`

- `len(iterable_value)`

- `enumerate(iterable_value, start=0)`
- `zip(*iterable_values, strict=False)`

### Sequence Types — `list`, `tuple`, `range`

#### `list`

Doc: `class list(iterable=(), /)`.

- `[42]`, `[42, 4.2]`

##### Lists operations

- `list_value_1 + list_value_2`
- `list_value * 42`

##### Lists functions

- `enumerate(list_value)`

- `sorted(iterable_value)`

##### Lists methods

- `list_variable.append(list_item_value)`
- `list_variable.pop()`

#### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

#### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `tuple()`

- `(value, )`, `(value_1, value_2)`

##### Tuples operations

- `variable_1, variable_2 = iterable_value`
- `variable_1, variable_2 = expression_1, expression_2`

### Text Sequence Type — `str`

- `string_value[index]`, `string_value[-index]`

#### Strings operations

- `string_variable += string_value`

- `f''`
  - `f'{string_value}'`
  - `f'{string_value:.2f}'`
  - `f'{string_value:>{length}}'`

##### Strings comparison

- `string_value_1 == string_value_2`, `string_value_1 != string_value_2`

#### Strings functions

- `len(string_value)`

#### `str`

- `str(value)`

#### Strings methods

- `string_value_1.isupper()`
- `string_value_1.join(iterable_value)`
- `string_value_1.split(string_value_2)`

### Set Types — `set`, `frozenset`

#### Common sets operations

- `value in set_value`, `value not in set_value`

#### Common sets functions

- `len(set_value)`

#### `frozenset`

- `frozenset(iterable_value)`

#### `set`

- `set(iterable_value)`

#### Sets methods

- `set_variable.add(value)`

### Mapping Types — `dict`

- `{'immutable_key_1': value_1, 'immutable_key_2': value_2}`

- `dict_value[immutable_key]`

#### Dicts operations

- `immutable_key in dict_value`, `immutable_key not in dict_value`

#### Dicts methods

- `dict_value.get(immutable_key, default_value)`

- `dict_value.values()`

### Conditions

- `if condition:`, `elif condition:`, `else:`
- `condition_1 and condition_2`
- `not condition`

### Loops

- `for variable in iterable_value:`
- `while condition:`
- `break`
- `continue`

### List comprehensions

- `[expression for variable in iterable_value]`
- `[expression for variable in iterable_value if condition]`

### Dict comprehensions

- `{key_expression: value_expression for variable in iterable_value}`

### Generator comprehensions

- `(expression for variable in iterable_value)`

### Other

- `map()`

- `eval(…)`

## Standard libraries

### `itertools`

- `count(start=0, step=1)`
- `cycle(iterable_value)`

- `accumulate(iterable_value)`
- `chain(*iterable_values)`
    - `chain.from_iterable(iterable_value)`
- `product(*iterable_values, repeat=1)`

- `combinations(iterable_value)`
- `permutations(iterable_value)`

- `islice(iterable_value, stop_integer_value)`
