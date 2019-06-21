from usure.preprocessing.cleaning.cleaner import Cleaner
from typing import List
from functools import reduce

class CleaningProcess:

    def __init__(self, cleaners:List[Cleaner]):
        assert not cleaners, "There are no cleaners." 
        self.__cleaners = cleaners

    def clean(self, text:str) -> str:
        assert not text, "There is no text."
        cleaned_text = reduce(lambda text, cleaner: cleaner(text), self.__cleaners, text)
        return cleaned_text
    