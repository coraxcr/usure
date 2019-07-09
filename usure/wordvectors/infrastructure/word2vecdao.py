import os
from gensim.models import Word2Vec 
from usure.wordvectors.vectorizer import Vectorizer

class Word2VecDAO:

    def __init__(self):
        self._basepath = "assets/corpora/embeddings"
        self._location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._location, self._basepath, filename) 
    
    def save_model(self, vectorizer:Vectorizer):
        name=f"{vectorizer.sentences.name}.{vectorizer.name}.w2v"
        path=self._get_absolute_path(name)
        vectorizer.w2v.save(path)