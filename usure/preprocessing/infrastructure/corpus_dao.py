import os
from abc import ABC, abstractmethod
from typing import List, Callable
from pandas import DataFrame
import pandas as pd
#from typing import Callable
#is_even: Callable[[int], bool] = lambda x: (x % 2 == 0)

class CorpusDAO():

    def __init__(self):
        self._basepath = "assets/corpora/"

    _location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._location__, filename)        

    def get_facebookcorpus(self) -> DataFrame:
        path = self._get_absolute_path(f"{self._basepath}CorpusFBCR2013.txt")
        result = pd.read_csv(path, sep=os.linesep, encoding="latin_1")
        return result

    def store_facebookcorpus(self, data):
        data.to_csv(self._get_absolute_path(f"{self._basepath}CorpusFBCR2013.usu"))
    
    def get_twittercorpus(self) -> DataFrame:
        raise NotImplementedError()

