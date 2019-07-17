from abc import ABC, abstractmethod
from typing import Iterable
from usure.preprocessing.core import Corpus


class CorpusRepository(ABC):

    @abstractmethod
    def get(self, name: str) -> Corpus:
        pass

    @abstractmethod
    def get_all(self) -> Iterable[Corpus]:
        pass

    @abstractmethod
    def save(self, corpora: Corpus):
        pass
