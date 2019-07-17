from abc import ABC, abstractmethod
from gensim.models import KeyedVectors
from typing import Iterable


class KeyedVectorsRepository(ABC):

    @abstractmethod
    def get(self, name:str) -> KeyedVectors:
        pass
    
    @abstractmethod
    def get_all(self) -> Iterable[KeyedVectors]:
        pass

    @abstractmethod
    def save(self, kvs:KeyedVectors):
        pass