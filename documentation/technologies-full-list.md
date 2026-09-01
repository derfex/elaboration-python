# Technologies

## Full list

### Python

#### Input and output

- `input()`
- `print()`
  - `print(42, end = 'str')`

#### Numeric Types — `int`, `float`, `complex`

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

- `max(42, 4.2)`
- `min(42, 4.2)`

- `round(42)`

##### Number comparison

- `42 == 42`
- `42 != 42`
- `42 > 42`, `42 < 42`
- `42 >= 42`, `42 <= 42`
- `42 == 42 == 42`
- `42 >= 42 >= 42`, `42 >= 42 > 42`, etc.
- `42 <= 42 <= 42`, `42 <= 42 < 42`, etc.

#### Boolean Type — `bool`

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
  - `f'{var:>{length}}'`
  - `f'{var:^{length}}'`
  - `f'{var:<{length}}'`
  - ```python
    f"""\
    """
    ```

- `str[42]`, `str[-1]`
- `str[42:42]`

- `chr(42)`
- `ord('ё')`
- `len('str')`

##### String comparison

- `'str' == 'str'`, `'str' != 'str'`
- `'str' > 'str'`, `'str' < 'str'`
- `'str' in 'str'`

- `max('str', 'str')`
- `min('str', 'str')`

#### Binary Sequence Types — `bytes`, `bytearray`, `memoryview`

#### Set Types — `set`, `frozenset`

#### Mapping Types — `dict`

#### Type conversion

- `int()`
  - `int('42')`
  - `int('101', 2)`
- `float('4.2')`
- `str(42)`

#### Conditions

- `if condition:`, `elif condition:`, `else:`
- `match subject_expression:`, `case value:`
- `condition_1 and condition_2`
- `condition_1 or condition_2`
- `not condition`

#### Cycles

- `for variable in iterable_variable:`
- `while condition:`
- `while variable := expression:`
- `break`

#### Other

- `[a, b, c] = 'str'`
- `number_1, number_2 = expression_1, expression_2`

#### Comments

- `# …`
- ```python
  """
  …
  """
  ```
