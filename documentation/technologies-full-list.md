# Technologies

## Full list

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
- `42 / 42`
- `42 // 42`
- `42 % 42`
- `42 ** 42`
- `num += 42`
- `num -= 42`
- `num *= 42`
- `num //= 42`

###### Numbers comparison

- `42 == 42`
- `42 != 42`
- `42 > 42`, `42 < 42`
- `42 >= 42`, `42 <= 42`
- `42 == 42 == 42`
- `42 >= 42 >= 42`, `42 >= 42 > 42`, etc.
- `42 <= 42 <= 42`, `42 <= 42 < 42`, etc.

##### Numbers functions

- `max(42, 4.2)`
- `min(42, 4.2)`

- `round(4.2)`

##### `float`

- `float('4.2')`

##### `int`

- `int()`
  - `int('42')`
  - `int('101', 2)`

#### Boolean Type — `bool`

- `False`, `True`

#### Sequence Types — `list`, `tuple`, `range`

##### `list`

Doc: `class list(iterable=(), /)`.

- `list()`

- `[42]`, `[42, 4.2]`

- `list_value[index]`, `list_value[-index]`
- `list_value[i:j]`, `list_value[i:j:k]`

###### Lists operations

- `list_value_1 + list_value_2`
- `list_value * 42`
- `list_variable += list_value`

- `value in list_value`, `value not in list_value`

- `del list_variable[index]`
- `del list_variable[i:j:k]`

- `*list_value`

###### Lists functions

- `enumerate(list_value)`

- `len(list_value)`
- `max(list_value)`
- `min(list_value)`
- `sorted(iterable_value)`

###### Lists methods

- `list_variable.append(list_item_value)`
- `list_variable.clear()`
- `list_variable.count(list_item_value)`
- `list_variable.extend(iterable_value)`
- `list_variable.index(list_item_value)`
- `list_variable.insert(index, list_item_value)`
- `list_variable.pop()`
- `list_variable.remove(list_item_value)`
- `list_variable.reverse()`
- `list_variable.sort()`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `tuple()`

- `(value, )`, `(value_1, value_2)`

- `tuple_variable[index]`, `tuple_variable[-index]`
- `tuple_variable[i:j]`, `tuple_variable[i:j:k]`

###### Tuples operations

- `variable_1, variable_2 = iterable_value`
- `variable_1, variable_2 = expression_1, expression_2`

- `tuple_value_1 + tuple_value_2`
- `tuple_value * 42`

- `value in tuple_value`, `value not in tuple_value`

###### Tuples functions

- `enumerate(tuple_value)`

- `len(tuple_value)`
- `max(tuple_value)`
- `min(tuple_value)`

#### Text Sequence Type — `str`

- `string_value[index]`, `string_value[-index]`
- `string_value[i:j]`, `string_value[i:j:k]`

##### Strings operations

- `string_value_1 + string_value_2`
- `string_value * 42`
- `string_variable += string_value`

- `string_value_1 in string_value_2`

- `f''`
  - `f'{string_value}'`
  - `f'{string_value:02d}'`
  - `f'{string_value:.2f}'`
  - `f'{string_value:<{length}}'`
  - `f'{string_value:^{length}}'`
  - `f'{string_value:>{length}}'`
  - ```python
    f"""\
    """
    ```

###### Strings comparison

- `string_value_1 == string_value_2`, `string_value_1 != string_value_2`
- `string_value_1 > string_value_2`, `string_value_1 < string_value_2`

##### Strings functions

- `chr(42)`
- `ord('ё')`

- `enumerate(string_value)`

- `len(string_value)`
- `max(string_value_1, string_value_2)`
- `min(string_value_1, string_value_2)`

##### `str`

- `str(42)`

##### Strings methods

- `string_value_1.capitalize()`
- `string_value_1.count(string_value_2)`
- `string_value_1.endswith(string_value_2)`
- `string_value_1.find(string_value_2)`
- `string_value_1.index(string_value_2)`
- `string_value_1.isalnum()`
- `string_value_1.isalpha()`
- `string_value_1.isdigit()`
- `string_value_1.islower()`
- `string_value_1.isupper()`
- `string_value_1.join(iterable_value)`
- `string_value_1.ljust(width, fillchar)`
- `string_value_1.lower()`
- `string_value_1.lstrip('str')`
- `string_value_1.rjust(width, fillchar)`
- `string_value_1.rstrip(string_value_2)`
- `string_value_1.split(string_value_2)`
- `string_value_1.startswith(string_value_2)`
- `string_value_1.strip(string_value_2)`
- `string_value_1.title()`
- `string_value_1.upper()`
- `string_value_1.zfill(42)`

#### Binary Sequence Types — `bytes`, `bytearray`, `memoryview`

#### Set Types — `set`, `frozenset`

##### Common sets operations

- `set_value_1 | set_value_2`
- `set_value_1 & set_value_2`
- `set_value_1 - set_value_2`
- `set_value_1 ^ set_value_2`
- `set_variable |= set_value`

- `value in set_value`, `value not in set_value`

- `*set_value`

###### Common sets comparison

- `set_value_1 == set_value_2`, `set_value_1 != set_value_2`
- `set_value_1 >= set_value_2`, `set_value_1 <= set_value_2`

##### Common sets functions

- `len(set_value)`

##### Common sets methods

- `set_variable.difference(set_value)`
- `set_variable.intersection(set_value)`
- `set_variable.symmetric_difference(set_value)`
- `set_variable.union(set_value)`

##### `frozenset`

- `frozenset(iterable_value)`

##### `set`

- `set(iterable_value)`

- `{value_1, value_2}`

##### Sets methods

- `set_variable.add(value)`
- `set_variable.clear()`
- `set_variable.discard(value)`
- `set_variable.pop()`
- `set_variable.remove(value)`

#### Mapping Types — `dict`

- `dict()`

- `{'immutable_key_1': value_1, 'immutable_key_2': value_2}`

- `dict_value[immutable_key]`

##### Dicts operations

- `immutable_key in dict_value`, `immutable_key not in dict_value`

- `del dict_value[immutable_key]`

##### Dicts functions

- `len(dict_value)`

##### Dicts methods

- `dict_value.clear()`
- `dict_value.get(immutable_key, default_value)`
- `dict_value.pop(immutable_key, default_value)`

- `dict_value.items()`
- `dict_value.keys()`
- `dict_value.values()`

#### Conditions

- `if condition:`, `elif condition:`, `else:`
- `match subject_expression:`, `case value:`
- `match … case variable if expression:`
- `condition_1 and condition_2`
- `condition_1 or condition_2`
- `not condition`

- `value_1 if condition else value_2`

#### Loops

- `for variable in iterable_value:`
- `while condition:`
- `break`
- `continue`
- `else:`

#### List comprehensions

- `[expression for variable in iterable_value]`
- `[expression for variable in iterable_value if condition]`

#### Set comprehensions

- `{expression for variable in iterable_value}`
- `{expression for variable in iterable_value if condition}`

#### Dict comprehensions

- `{key_expression: value_expression for variable in iterable_value}`
- `{key_expression: value_expression for variable in iterable_value if condition}`

#### Generator comprehensions

- `(expression for variable in iterable_value)`
- `(expression for variable in iterable_value if condition)`

#### Other

- `variable := expression`

- `all(iterable_value)`
- `len(iterable_value)`
- `sum(iterable_value)`

- `map()`
- `max(<map object>)`

#### Comments

- `# …`
- ```python
  """
  …
  """
  ```
