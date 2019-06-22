from usure.preprocessing.cleaning.cleaner import Cleaner
from typing import List
from functools import reduce

class CleaningTask:

    def __init__(self, cleaners:List[Cleaner]):
        assert cleaners, "There are no cleaners." 
        self.__cleaners = cleaners

    def clean(self, text:str) -> str:
        assert text, "There is no text."
        cleaned_text = reduce(lambda text, cleaner: cleaner.clean(text), self.__cleaners, text)
        return cleaned_text
    