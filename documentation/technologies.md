# Technologies

## Used

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

- `[42].append(42)`
- `[42].index(42)`
- `[42].pop()`

- `42 in [42, 4.2]`, `42 not in [42, 4.2]`
- `len([42])`
- `max([42, 4.2])`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `42 in (42, 4.2)`, `42 not in (42, 4.2)`

#### Text Sequence Type — `str`

- `'str' + 'ing'`
- `'str' * 42`
- `variable += 'str'`
- `f''`
  - `f'{var}'`
  - `f'{var:02d}'`
  - `f'{var:.2f}'`
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

- `'str str'.count('str')`
- `'str str'.endswith('str')`
- `'str str'.find('str')`
- `'str str'.join(['str', 'str'])`
- `'str str'.lower()`
- `'str str'.rstrip('str')`
- `'str str'.split('str')`
- `'str str'.startswith('str')`
- `'str str'.upper()`

##### String comparison

- `'str' == 'str'`, `'str' != 'str'`
- `'str' > 'str'`, `'str' < 'str'`
- `'str' in 'str'`

- `min('str', 'str')`

#### Set Types — `set`, `frozenset`

##### `set`

- `variable_1, variable_2 = expression_1, expression_2`
- `variable_1, variable_2, variable_3 = 'str'`

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
