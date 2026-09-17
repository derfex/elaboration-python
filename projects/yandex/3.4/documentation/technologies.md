# Yandex. 3.4. Technologies

## Used

### Python

#### Input and output

- `input()`
- `print()`
  - `print(value_1, value_2, end=string_value)`
  - `print(value_1, value_2, sep=string_value)`

#### Numeric Types — `int`, `float`, `complex`

##### Numbers operations

- `42 + 42`
- `42 - 42`
- `42 * 42`
- `num += 42`
- `num //= 42`

###### Numbers comparison

- `42 > 42`, `42 < 42`
- `42 >= 42`, `42 <= 42`

##### `float`

- `float('4.2')`

##### `int`

- `int()`
  - `int('42')`

#### Boolean Type — `bool`

- `False`, `True`

#### Iterator Types

##### Iterators operations

- `*iterable_value`

##### Iterators functions

- `iter(iterable_value, /)`

- `enumerate(iterable_value, start=0)`
- `zip(*iterable_values, strict=False)`

#### Sequence Types — `list`, `tuple`, `range`

##### `list`

Doc: `class list(iterable=(), /)`.

- `[42]`, `[42, 4.2]`

###### Lists operations

- `list_value_1 + list_value_2`
- `list_value * 42`

###### Lists functions

- `enumerate(list_value)`

- `sorted(iterable_value)`

###### Lists methods

- `list_variable.append(list_item_value)`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `tuple()`

- `(value, )`, `(value_1, value_2)`

###### Tuples operations

- `variable_1, variable_2 = iterable_value`

#### Text Sequence Type — `str`

##### Strings operations

- `string_variable += string_value`

- `f''`
  - `f'{string_value}'`
  - `f'{string_value:.2f}'`
  - `f'{string_value:>{length}}'`

###### Strings comparison

- `string_value_1 == string_value_2`, `string_value_1 != string_value_2`

##### `str`

- `str(value)`

##### Strings methods

- `string_value_1.join(iterable_value)`
- `string_value_1.split(string_value_2)`

#### Binary Sequence Types — `bytes`, `bytearray`, `memoryview`

#### Set Types — `set`, `frozenset`

##### `frozenset`

- `frozenset(iterable_value)`

#### Mapping Types — `dict`

- `{'immutable_key_1': value_1, 'immutable_key_2': value_2}`

- `dict_value[immutable_key]`

##### Dicts methods

- `dict_value.values()`

#### Conditions

- `if condition:`, `elif condition:`, `else:`

#### Loops

- `for variable in iterable_value:`
- `break`
- `continue`

#### List comprehensions

- `[expression for variable in iterable_value]`
- `[expression for variable in iterable_value if condition]`

#### Generator comprehensions

- `(expression for variable in iterable_value)`

#### Other

- `map()`

### Standard libraries

#### `itertools`

- `count(start=0, step=1)`
- `cycle(iterable_value)`

- `accumulate(iterable_value)`
- `chain(*iterable_values)`
    - `chain.from_iterable(iterable_value)`
- `product(*iterable_values, repeat=1)`

- `combinations(iterable_value)`
- `permutations(iterable_value)`

- `islice(iterable_value, stop_integer_value)`
