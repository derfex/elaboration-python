# Technologies

## Used

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

##### `range`

Doc: `class range(stop, /)`, `class range(start, stop, step=1, /)`.

- `range()`

##### `tuple`

Doc: `class tuple(iterable=(), /)`.

- `variable_1, variable_2 = expression_1, expression_2`
- `variable_1, variable_2, variable_3 = 'str'`

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
  - `f'{string_value:^{length}}'`
  - `f'{string_value:>{length}}'`
  - ```python
    f"""\
    """
    ```

###### Strings comparison

- `'str' == 'str'`, `'str' != 'str'`
- `'str' > 'str'`, `'str' < 'str'`

##### Strings functions

- `chr(42)`
- `ord('ё')`

- `len('str')`
- `min('str', 'str')`

##### `str`

- `str(42)`

##### Strings methods

- `string_value_1.split(string_value_2)`

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
