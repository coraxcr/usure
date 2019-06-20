from typing import Set
import pandas as pd
import os.path
import os

class EmoticonRepository:

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def __get_absolute_path(self, filename:str) -> str:
        return os.path.join(self.__location__, filename)

    def __get_emoticons(self, filename:str) -> Set[str]:
        file_absolutepath = self.__get_absolute_path(filename)
        with open(file_absolutepath) as f:
            emoticons = f.readlines()
        emoticons = map(lambda emoticon: emoticon.strip(os.linesep), emoticons)
        return set(emoticons)
    
    def get_negative_emoticons(self) -> Set[str]:
        return self.__get_emoticons('assets/negative.txt')

    def get_positive_emoticons(self) -> Set[str]:
        return self.__get_emoticons('assets/positive.txt')

