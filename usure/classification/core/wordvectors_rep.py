from abc import ABC, abstractclassmethod
from typing import Iterable, Dict, Any
from .wordvectors import WordVectors


class WordVectorsRep(ABC):

    def get(self, name: str) -> WordVectors:
        pass

    def get_all(self) -> Iterable[WordVectors]:
        pass
