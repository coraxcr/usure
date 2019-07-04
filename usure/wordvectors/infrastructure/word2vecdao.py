import os
from abc import ABC, abstractmethod
from gensim.models import Word2Vec 
  

class Word2VecDAO(ABC):

    def __init__(self):
        self._basepath = "/assets/corpora/embeddings"
        self._location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self._fullfilepath = None

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._location+self._basepath, filename) 
    
    def save_model(self, w2v: Word2Vec):
        w2v.save(self._fullfilepath)

    def get_model(self, w2v: Word2Vec):
        return Word2Vec.load(self._fullfilepath)