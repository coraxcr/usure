from typing import Set
import os
from os.path import join


class EmoticonRepository:

    def __init__(self, folderpath):
        self._folderpath = folderpath

    def __get_emoticons(self, filename:str) -> Set[str]:
        file_absolutepath = join(self._folderpath, filename)
        with open(file_absolutepath) as f:
            emoticons = f.readlines()
        emoticons = map(lambda emoticon: emoticon.strip(os.linesep), emoticons)
        return set(emoticons)
    
    def get_negative_emoticons(self) -> Set[str]:
        return self.__get_emoticons('negative.txt')

    def get_positive_emoticons(self) -> Set[str]:
        return self.__get_emoticons('positive.txt')

