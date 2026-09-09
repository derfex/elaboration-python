# Technologies

## Full list

### Python

#### Input and output

- `input()`
- `print()`
  - `print(42, 'str', end='str')`
  - `print(42, 'str', sep='str')`

#### Numeric Types — `int`, `float`, `complex`

##### Number operations

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

###### Number comparison

- `42 == 42`
- `42 != 42`
- `42 > 42`, `42 < 42`
- `42 >= 42`, `42 <= 42`
- `42 == 42 == 42`
- `42 >= 42 >= 42`, `42 >= 42 > 42`, etc.
- `42 <= 42 <= 42`, `42 <= 42 < 42`, etc.

##### Number functions

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

- `[42][0]`

###### Lists operations

- `[42] + [42]`
- `[42] * 42`
- `list_variable += [42]`

- `42 in [42, 4.2]`, `42 not in [42, 4.2]`

- `del list_variable[42]`
- `del list_variable[::42]`

###### Lists methods

- `[42].append(42)`
- `[42].clear()`
- `[42].count(42)`
- `[42].extend(42)`
- `[42].index(42)`
- `[42].insert(42, 42)`
- `[42].pop()`
- `[42].remove(42)`
- `[42].reverse()`
- `[42].sort()`

###### Lists functions

- `len([42])`
- `max([42, 4.2])`
- `min([42, 4.2])`
- `sorted([42, 4.2])`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `tuple()`

- `42 in (42, 4.2)`, `42 not in (42, 4.2)`

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

- `'str str'.capitalize()`
- `'str str'.count('str')`
- `'str str'.endswith('str')`
- `'str str'.find('str')`
- `'str str'.index('str')`
- `'str str'.isalnum()`
- `'str str'.isalpha()`
- `'str str'.isdigit()`
- `'str str'.islower()`
- `'str str'.isupper()`
- `'str str'.join(['str', 'str'])`
- `'str str'.ljust(width, fillchar)`
- `'str str'.lower()`
- `'str str'.lstrip('str')`
- `'str str'.rjust(width, fillchar)`
- `'str str'.rstrip('str')`
- `'str str'.split('str')`
- `'str str'.startswith('str')`
- `'str str'.strip('str')`
- `'str str'.title()`
- `'str str'.upper()`
- `'str str'.zfill(42)`

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
- `match … case variable if expression:`
- `condition_1 and condition_2`
- `condition_1 or condition_2`
- `not condition`

#### Loops

- `for variable in iterable_variable:`
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
