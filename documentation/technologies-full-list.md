# Technologies

## Full list

### Python

#### Input and output

- `input()`
- `print()`
  - `print(42, 'str', end='str')`
  - `print(42, 'str', sep='str')`

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

- `list_variable[index]`, `list_variable[-index]`
- `list_variable[i:j]`, `list_variable[i:j:k]`

###### Lists operations

- `list_variable_1 + list_variable_2`
- `list_variable * 42`
- `list_variable_1 += list_variable_2`

- `variable in list_variable`, `variable not in list_variable`

- `del list_variable[index]`
- `del list_variable[i:j:k]`

###### Lists methods

- `list_variable.append(variable)`
- `list_variable.clear()`
- `list_variable.count(variable)`
- `list_variable.extend(variable)`
- `list_variable.index(variable)`
- `list_variable.insert(index, variable)`
- `list_variable.pop()`
- `list_variable.remove(variable)`
- `list_variable.reverse()`
- `list_variable.sort()`

###### Lists functions

- `len(list_variable)`
- `max(list_variable)`
- `min(list_variable)`
- `sorted(list_variable)`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `tuple()`

- `(42, )`, `(42, 4.2)`

- `tuple_variable[index]`, `tuple_variable[-index]`
- `tuple_variable[i:j]`, `tuple_variable[i:j:k]`

###### Tuples operations

- `variable_1, variable_2 = expression_1, expression_2`
- `variable_1, variable_2, variable_3 = 'str'`

- `tuple_variable_1 + tuple_variable_2`
- `tuple_variable * 42`

- `variable in tuple_variable`, `variable not in tuple_variable`

###### Tuples functions

- `len(tuple_variable)`
- `max(tuple_variable)`
- `min(tuple_variable)`

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
- `string_value_1.join([string_value_2, string_value_3])` // TODO: list or iterable?
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

##### `set`

- `set(iterable_value)`

#### Mapping Types — `dict`

#### Conditions

- `if condition:`, `elif condition:`, `else:`
- `match subject_expression:`, `case value:`
- `match … case variable if expression:`
- `condition_1 and condition_2`
- `condition_1 or condition_2`
- `not condition`

#### Loops

- `for variable in iterable_value:`
- `while condition:`
- `break`
- `continue`
- `else:`

#### Other

- `variable := expression`
- `map()`
- `a, b = <map object>`

#### Comments

- `# …`
- ```python
  """
  …
  """
  ```
