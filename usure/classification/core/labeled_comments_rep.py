from abc import ABC, abstractmethod
from typing import Iterable
from .labeled_comments import LabeledComments


class LabeledCommentsRep(ABC):

    @abstractmethod
    def get(self, name:str) -> LabeledComments:
        """Return training, dev and test comments consolidated"""
        pass

    @abstractmethod
    def get_training(self, name:str) -> LabeledComments:
        pass

    @abstractmethod
    def get_dev(self, name:str) -> LabeledComments:
        pass

    @abstractmethod
    def get_test(self, name:str) -> LabeledComments:
        pass
