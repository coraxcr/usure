import os
from abc import ABC, abstractmethod
from gensim.utils import tokenize


class TrainingCorpusDAO(ABC):

    def __init__(self):
        self._basepath = "/assets/corpora/"
        self._location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._location__+self._basepath, filename) 

    def _get_trainingcorpus(self, filename):
        path = self._get_absolute_path(filename) 
        with open(path, encoding="ascii") as file:
            line = file.readline()
            while line:
                yield tokenize(line, lower=True, errors='ignore')
                line = file.readline()

    @abstractmethod
    def get_trainingcorpus(self):
        raise NotImplementedError()