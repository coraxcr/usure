import pytest
from ..numericcleaner import NumericCleaner


@pytest.mark.parametrize("text,expected", [
    ("Hola 658575 mundo", "Hola mundo"),
    ("658575 Hola mundo", "Hola mundo"),
    ("Hola mundo 658575", "Hola mundo")
])
def delete_all_numericwords_test(text, expected):
    cleaner = NumericCleaner()
    result = cleaner.clean(text)
    assert result == expected
