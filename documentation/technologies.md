# Technologies

## Used

### Python

#### Input and output

- `input()`
- `print()`

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

##### `int`

- `int()`
  - `int('42')`
  - `int('101', 2)`

##### `float`

- `float('4.2')`

##### Number comparison

- `42 == 42`
- `42 != 42`
- `42 > 42`, `42 < 42`
- `42 >= 42`, `42 <= 42`
- `42 == 42 == 42`
- `42 >= 42 >= 42`, `42 >= 42 > 42`, etc.
- `42 <= 42 <= 42`, `42 <= 42 < 42`, etc.

#### Sequence Types — `list`, `tuple`, `range`

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

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

##### String comparison

- `'str' == 'str'`, `'str' != 'str'`
- `'str' > 'str'`, `'str' < 'str'`
- `'str' in 'str'`

- `min('str', 'str')`

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

- ```python
  """
  …
  """
  ```
