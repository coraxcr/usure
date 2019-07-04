import os
from io import TextIOWrapper
from abc import ABC, abstractmethod
#from gensim.utils import tokenize


class TrainingCorpusDAO(ABC):

    def __init__(self):
        self._basepath = "/assets/corpora/preprocessed"
        self._location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._location__+self._basepath, filename) 

    def _get_trainingcorpus(self, filename):
        path = self._get_absolute_path(filename) 
        return TrainingCorpus(path)

    @abstractmethod
    def get_trainingcorpus(self):
        raise NotImplementedError()

class TrainingCorpus:

    def __init__(self, path:str):
        self._path = path

    def __iter__(self):
        with open(self._path, encoding="ascii") as file:
            line = file.readline()
            while line:
                yield line.split()
                line = file.readline()