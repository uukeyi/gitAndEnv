# LeetCode Problem Valid Parentheses

### Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

### An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type

### Example 1

```python
# is_valid_brackets("()[]{}")
True
```


### Example 2

```python
# is_valid_brackets("(]")
False
```


### Example 3
```python
# is_valid_brackets("()")
True
```

### Example 4

```python
# is_valid_brackets("[]")
True
```

## Constraints:

- 1 <= s.length <= 10<sup>4</sup>
- s consists of parentheses only '()[]{}'.

# How to test

### Install dependecies

```
pip install -r requirements_test.txt
```

### Init tests
```
pytest
```
or
```
pytest -v
```
for detail log
