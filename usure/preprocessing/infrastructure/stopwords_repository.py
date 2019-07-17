from typing import Set
from os.path import join
import os 

class StopwordsRepository:

    def __init__(self, folderpath):
        self._folderpath = folderpath
        
    def __get_emoticons(self, filename:str) -> Set[str]:
        file_absolutepath = join(self._folderpath, filename)
        with open(file_absolutepath) as f:
            tokens = f.readlines()
        tokens = map(lambda token: token.strip(os.linesep), tokens)
        return set(tokens)
    
    def get_spanish_stopwords(self) -> Set[str]:
        return self.__get_emoticons('stopwords-es.txt')
        #https://github.com/stopwords-iso/stopwords-es/blob/master/stopwords-es.txt