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

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `tuple()`

#### Text Sequence Type — `str`

- `'str' + 'ing'`
- `'str' * 42`
- `variable += 'str'`
- `f''`
  - `f'{var}'`
  - `f'{var:02d}'`
  - `f'{var:.2f}'`
  - `f'{var:<{length}}'`
  - `f'{var:^{length}}'`
  - `f'{var:>{length}}'`
  - ```python
    f"""\
    """
    ```

- `str[42]`, `str[-1]`
- `str[42:42]`

- `chr(42)`
- `ord('ё')`
- `len('str')`

##### `str`

- `str(42)`

- `'str str'.split('str')`

##### String comparison

- `'str' == 'str'`, `'str' != 'str'`
- `'str' > 'str'`, `'str' < 'str'`
- `'str' in 'str'`

- `max('str', 'str')`
- `min('str', 'str')`

#### Binary Sequence Types — `bytes`, `bytearray`, `memoryview`

#### Set Types — `set`, `frozenset`

##### `set`

- `set(iterable_variable)`

- `variable_1, variable_2 = expression_1, expression_2`
- `variable_1, variable_2, variable_3 = 'str'`

#### Mapping Types — `dict`

#### Conditions

- `if condition:`, `elif condition:`, `else:`
- `match subject_expression:`, `case value:`
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
