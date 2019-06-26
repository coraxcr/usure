import os
from abc import ABC, abstractmethod
from typing import List, Callable
from pandas import DataFrame
import pandas as pd
#from typing import Callable
#is_even: Callable[[int], bool] = lambda x: (x % 2 == 0)
#sep=os.linesep

class CorpusDAO():

    def __init__(self):
        self._basepath = "assets/corpora/"

    _location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._location__, filename)        

    def _get_corpus(self, filename:str) -> DataFrame:
        path = self._get_absolute_path(f"{self._basepath}{filename}")
        result = pd.read_csv(path, sep=os.linesep, encoding="latin_1", header=None)
        return result

    def _store_corpus(self, filename:str, corpus):
        path = self._get_absolute_path(f"{self._basepath}{filename}.usu")
        corpus.to_csv(path, encoding="ascii", index=False, header=False)

    @abstractmethod
    def get_corpus(self):
        raise NotImplementedError
    
    @abstractmethod
    def store_corpus(self, corpus):
        raise NotImplementedError