from usure.preprocessing.cleaning.punctuationcleaner import PuntuationCleaner
import pytest

@pytest.mark.parametrize("text,expected", [
    ("¡Hola a todos! casa grande casa roj@, *& # %", " Hola a todos  casa grande casa roj         ")
])
def can_remove_punctuation_simbols_test(text, expected):
    cleaner = PuntuationCleaner()
    result = cleaner.clean(text)
    assert result == expected
