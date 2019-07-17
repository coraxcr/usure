from abc import ABC, abstractmethod
from typing import Iterable
from usure.wordvectors.core import Corpus

class CorpusRepository(ABC):

    @abstractmethod
    def get(self, name:str) -> Corpus:
        pass
    
    @abstractmethod
    def get_all(self) -> Iterable[Corpus]:
        pass