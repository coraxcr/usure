import pytest
from usure.preprocessing.cleaning import EscapeCleaner


@pytest.mark.parametrize("text,expected", [
    ("casas \\n ", "casas   "),
    ("casas \\\" ", "casas   ")
])
def can_clean_escapes_test(text, expected):
    cleaner = EscapeCleaner()
    result = cleaner.clean(text)
    assert result == expected
