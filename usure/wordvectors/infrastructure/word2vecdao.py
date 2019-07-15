import os
from pathlib import Path
from gensim.models import Word2Vec  
from typing import Generator, Iterator
from usure.wordvectors.vectorizer import Vectorizer
from usure.common.fileutils import get_absolutefilepaths_ordered_by_size


def load_w2v(absolutefilepath) -> Word2Vec:
        w2v = Word2Vec.load(absolutefilepath)
        w2v.name = Path(absolutefilepath).name
        return w2v

class FileWord2Vecs:

    def __init__(self, absolutefilepaths):
        self._absolutefilepaths=absolutefilepaths

    def __iter__(self) -> Iterator[Word2Vec]:
        for absolutefilepath in self._absolutefilepaths:
            w2v = load_w2v(absolutefilepath)
            yield w2v
            
class Word2VecDAO:

    def __init__(self):
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        basepath = "assets/corpora/embeddings"
        self._embeddingsfolderpath = os.path.join(location, basepath)

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._embeddingsfolderpath, filename) 
    
    def save_model(self, vectorizer:Vectorizer):
        name = f"{vectorizer.sentences.name}.{vectorizer.name}.w2v"
        path = self._get_absolute_path(name)
        vectorizer.w2v.save(path)

    def get_models(self) -> FileWord2Vecs:
        absolutefilepaths=get_absolutefilepaths_ordered_by_size(self._embeddingsfolderpath, ".w2v")
        return FileWord2Vecs(absolutefilepaths)

    def get_model(self, name_id) -> Word2Vec:
        absolutefilepath = os.path.join(self._embeddingsfolderpath, f"{name_id}")
        return load_w2v(absolutefilepath)
