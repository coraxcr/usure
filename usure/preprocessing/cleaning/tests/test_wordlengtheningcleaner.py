from usure.preprocessing.cleaning.wordlengtheningcleaner import WordLengtheningCleaner
import pytest


@pytest.mark.parametrize("token,expected", [
    ("casaaaaaaaaa", "casaa"),
    ("grandeeeee", "grandee"),
    ("pequenoooo", "pequenoo"),
    ("fuuuuuuuuerte", "fuuerte"),
    ("fuuuerteee", "fuuertee"),
    ("fuuuerteee el baaarsa", "fuuertee el baarsa")
])
def can_shorten_letter_wordlengthening_test(token, expected):
    cleaner = WordLengtheningCleaner()
    result = cleaner.clean(token)
    assert result == expected
    
'''    
@pytest.mark.parametrize("token,expected", [
    ("grandotototote", "grandototote"),
    ("pequenininito", "pequeninito")
])
def can_shorten_syllable_wordlengthening_test(token, expected):
    cleaner = WordLengtheningCleaner()
    result = cleaner.clean(token)
    assert result == expected
'''