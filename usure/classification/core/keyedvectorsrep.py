from abc import ABC, abstractclassmethod
from gensim.models import KeyedVectors
from  typing import Iterable

class KeyedVectorsRep(ABC):

    def get(self,name:str) -> KeyedVectors:
        pass

    def get_all(self) -> Iterable[KeyedVectors]:
        pass