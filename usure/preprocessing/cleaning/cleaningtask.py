from typing import List
from functools import reduce
from usure.preprocessing.cleaning.cleaner import Cleaner

class CleaningTask:

    def __init__(self, cleaners:List[Cleaner]):
        assert cleaners, "There are no cleaners." 
        self.__cleaners = cleaners

    def clean(self, text:str) -> str:
        assert text, "There is no text."
        #try:
        cleaned_text = reduce(lambda text, cleaner: cleaner.clean(text), self.__cleaners, text)
        #except:
        #   print("Este es el texto invalido  ===> "+text) 
        #   raise
        return cleaned_text
    