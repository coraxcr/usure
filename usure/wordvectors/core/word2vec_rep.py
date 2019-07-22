from abc import ABC, abstractmethod
from gensim.models import Word2Vec
from typing import Iterable


class Word2VecRep(ABC):

    @abstractmethod
    def get(self, name: str) -> Word2Vec:
        pass

    @abstractmethod
    def get_all(self) -> Iterable[Word2Vec]:
        pass

    @abstractmethod
    def save(self, w2v: Word2Vec):
        pass
