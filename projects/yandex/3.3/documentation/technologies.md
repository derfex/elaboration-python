# Yandex. 3.3. Technologies

## Used

### Python

#### Input and output

#### Numeric Types — `int`, `float`, `complex`

##### Numbers operations

- `42 + 42`
- `42 - 42`
- `42 * 42`
- `42 % 42`
- `42 ** 42`

###### Numbers comparison

- `42 == 42`
- `42 != 42`
- `42 > 42`, `42 < 42`
- `42 >= 42`, `42 <= 42`

##### Numbers functions

- `max(42, 4.2)`
- `min(42, 4.2)`

#### Sequence Types — `list`, `tuple`, `range`

##### `list`

Doc: `class list(iterable=(), /)`.

###### Lists functions

- `len(list_value)`

- `sorted(iterable_value)`

###### Lists methods

- `list_variable.count(list_item_value)`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `(value, )`, `(value_1, value_2)`

- `tuple_variable[index]`, `tuple_variable[-index]`

###### Tuples operations

- `variable_1, variable_2 = iterable_value`

#### Text Sequence Type — `str`

- `string_value[index]`, `string_value[-index]`

##### Strings operations

- `string_value * 42`

###### Strings comparison

- `string_value_1 > string_value_2`, `string_value_1 < string_value_2`

##### Strings functions

- `len(string_value)`

##### `str`

- `str(42)`

##### Strings methods

- `string_value_1.count(string_value_2)`
- `string_value_1.isalpha()`
- `string_value_1.isdigit()`
- `string_value_1.join([string_value_2, string_value_3])` // TODO: list or iterable?
- `string_value_1.lower()`
- `string_value_1.split(string_value_2)`
- `string_value_1.upper()`

#### Set Types — `set`, `frozenset`

##### Common sets operations

- `set_value_1 & set_value_2`

- `value in set_value`, `value not in set_value`

##### Common sets functions

- `len(set_value)`

##### `frozenset`

- `frozenset(iterable_value)`

#### Mapping Types — `dict`

##### Dicts methods

- `dict_value.items()`

#### Conditions

- `condition_1 and condition_2`

- `value_1 if condition else value_2`

#### List comprehensions

- `[expression for variable in iterable_value]`
- `[expression for variable in iterable_value if condition]`

#### Set comprehensions

- `{expression for variable in iterable_value}`
- `{expression for variable in iterable_value if condition}`

#### Dict comprehensions

- `{key_expression: value_expression for variable in iterable_value}`
- `{key_expression: value_expression for variable in iterable_value if condition}`

#### Other

- `all(iterable_value)`
- `sum(iterable_value)`
