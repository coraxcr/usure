import os
from abc import ABC, abstractmethod
from typing import List, Callable
from pandas import DataFrame
import pandas as pd

class CorpusDAO():

    def __init__(self):
        self._basepath = "assets/corpora/"

    _location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._location__, filename)        

    def _get_corpus(self, filename:str) -> DataFrame:
        path = self._get_absolute_path(f"{self._basepath}{filename}")
        result = pd.read_csv(path, sep=os.linesep, encoding="utf_8", header=None)
        return result
    
    def _get_corpus_by_chunks(self, filename:str) -> DataFrame:
        path = self._get_absolute_path(f"{self._basepath}{filename}")
        input_fd = open(path, encoding="utf_8", errors = 'backslashreplace')
        reader = pd.read_csv(input_fd, sep=os.linesep, header=None, chunksize=400000)
        return reader

    def _store_corpus(self, filename:str, corpus):
        path = self._get_absolute_path(f"preprocessed/{self._basepath}{filename}.usu")
        corpus.to_csv(path, encoding="ascii", index=False, header=False)

    @abstractmethod
    def get_corpus(self):
        raise NotImplementedError

    @abstractmethod
    def get_corpus_by_chunks(self):
        raise NotImplementedError
    
    @abstractmethod
    def store_corpus(self, corpus):
        raise NotImplementedError