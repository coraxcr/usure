from abc import ABC, abstractclassmethod
from typing import Iterable, Dict, Any
from .models import WordVectors


class WordVectorsRepository(ABC):

    def get(self, name: str) -> WordVectors:
        pass

    def get_all(self) -> Iterable[WordVectors]:
        pass
