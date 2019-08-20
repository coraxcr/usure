from abc import ABC, abstractmethod
from typing import Iterable
from .labeled_comments import LabeledComments


class LabeledCommentsDao(ABC):

    @abstractmethod
    def get(self, name:str) -> LabeledComments:
        """Return training, dev and test comments consolidated"""
        pass

    @abstractmethod
    def save(self, labeled_comments:LabeledComments):
        pass

    @abstractmethod
    def save_from_origin(self, labeled_comments : LabeledComments, origin_name):
        pass