import pytest
import main

@pytest.mark.parametrize("input_str, expected", [
    ('()', True),
    ('[]', True),
    ('{}', True),
    ('[()]', True),
    ('(())', True),
    ('(])', False),
    (']()', False),
    ('(}', False),
])
def test_isValid(input_str, expected):
    assert main.isValid(input_str) == expected
