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
- `42 - 42`
- `42 % 42`
- `num += 42`
- `num //= 42`

###### Numbers comparison

- `42 > 42`, `42 < 42`

##### `int`

- `int()`
  - `int('42')`

#### Boolean Type — `bool`

- `False`, `True`

#### Sequence Types — `list`, `tuple`, `range`

##### `list`

Doc: `class list(iterable=(), /)`.

- `list()`

- `[42]`, `[42, 4.2]`

- `list_value[index]`, `list_value[-index]`

###### Lists operations

- `*list_value`

###### Lists functions

- `len(list_value)`
- `sorted(iterable_value)`

###### Lists methods

- `list_variable.append(list_item_value)`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `tuple()`

- `tuple_variable[index]`, `tuple_variable[-index]`

###### Tuples operations

- `variable_1, variable_2 = tuple_value`

###### Tuples functions

- `enumerate(tuple_value)`

- `len(tuple_value)`

#### Text Sequence Type — `str`

##### Strings operations

- `string_variable += string_value`

- `f''`
  - `f'{string_value}'`

###### Strings comparison

- `string_value_1 == string_value_2`, `string_value_1 != string_value_2`

##### Strings methods

- `string_value_1.islower()`
- `string_value_1.lower()`
- `string_value_1.split(string_value_2)`
- `string_value_1.upper()`

#### Binary Sequence Types — `bytes`, `bytearray`, `memoryview`

#### Set Types — `set`, `frozenset`

##### Common sets operations

- `set_value_1 & set_value_2`
- `set_value_1 - set_value_2`
- `set_value_1 ^ set_value_2`
- `set_variable |= set_value`

- `value in set_value`, `value not in set_value`

- `*set_value`

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

##### Dicts functions

- `len(dict_value)`

##### Dicts methods

- `dict_value.items()`
- `dict_value.keys()`
- `dict_value.values()`

#### Conditions

- `if condition:`, `elif condition:`, `else:`
- `not condition`

#### Loops

- `for variable in iterable_value:`
- `while condition:`
- `continue`

#### Other

- `variable := expression`
- `map()`
- `a, b = <map object>`
- `sum(iterable_value)`
