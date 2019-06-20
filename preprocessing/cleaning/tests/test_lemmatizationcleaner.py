from usure.preprocessing.cleaning.lemmatizationcleaner import LemmatizationCleaner
import pytest


@pytest.mark.parametrize("text,expected", [
    ("casas", " casar"),
    ("corazones estaban cayendo", " corazón estar caer")
])
def can_lemmatize_basic_spanish_words_test(text,expected):
     cleaner = LemmatizationCleaner()
     result = cleaner.clean(text)
     assert result == expected