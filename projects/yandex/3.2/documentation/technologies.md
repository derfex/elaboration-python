# Yandex. 3.2. Technologies

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

###### Numbers comparison

- `42 > 42`, `42 < 42`

##### `int`

- `int()`
  - `int('42')`

#### Boolean Type — `bool`

#### Sequence Types — `list`, `tuple`, `range`

##### `list`

Doc: `class list(iterable=(), /)`.

- `list()`

- `[42]`, `[42, 4.2]`

- `list_value[index]`, `list_value[-index]`

- `*list_value`

###### Lists functions

- `len(list_value)`
- `sorted(list_value)`

###### Lists methods

- `list_variable.append(list_item_value)`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

#### Text Sequence Type — `str`

##### Strings methods

- `string_value_1.split(string_value_2)`
- `string_value_1.upper()`

#### Binary Sequence Types — `bytes`, `bytearray`, `memoryview`

#### Set Types — `set`, `frozenset`

##### Common sets operations

- `*set_variable`

- `set_value_1 & set_value_2`
- `set_value_1 ^ set_value_2`
- `set_variable |= set_value`

- `value in set_value`, `value not in set_value`

##### Common sets functions

- `len(set_value)`

##### `frozenset`

- `frozenset(iterable_value)`

##### `set`

- `set(iterable_value)`

##### Sets methods

- `set_variable.add(value)`

#### Mapping Types — `dict`

- `dict()`

- `{'immutable_key_1': value_1, 'immutable_key_2': value_2}`

- `dict_value[immutable_key]`

##### Dicts operations

- `immutable_key in dict_value`, `immutable_key not in dict_value`

#### Conditions

- `if condition:`, `elif condition:`, `else:`

#### Loops

- `for variable in iterable_value:`
- `continue`

#### Other
