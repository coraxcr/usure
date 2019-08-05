from abc import ABC, abstractmethod
from typing import Iterable
from .labeled_comments import LabeledComments


class LabeledCommentsDao(ABC):

    @abstractmethod
    def get(self, name:str) -> LabeledComments:
        """Return training, dev and test comments consolidated"""
        pass

    #def save(self, name:str) -> 
        
    @abstractmethod
    def get_chunks(self, name, *percentages) -> Iterable[LabeledComments]:
        pass
