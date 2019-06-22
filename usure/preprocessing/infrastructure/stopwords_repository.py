from typing import Set
import os.path
import os

class StopwordsRepository:

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def __get_absolute_path(self, filename:str) -> str:
        return os.path.join(self.__location__, filename)

    def __get_emoticons(self, filename:str) -> Set[str]:
        file_absolutepath = self.__get_absolute_path(filename)
        with open(file_absolutepath) as f:
            tokens = f.readlines()
        tokens = map(lambda token: token.strip(os.linesep), tokens)
        return set(tokens)
    
    def get_spanish_stopwords(self) -> Set[str]:
        return self.__get_emoticons('assets/stopwords-es.txt')
        #https://github.com/stopwords-iso/stopwords-es/blob/master/stopwords-es.txt

