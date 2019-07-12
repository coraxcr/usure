import os
from pathlib import Path
from gensim.models import KeyedVectors  
from typing import Generator, Iterator
from usure.common.fileadministrator import get_absolutefilepaths_ordered_by_size


def load_kvs(absolutefilepath) -> KeyedVectors:
        kvs = KeyedVectors.load_word2vec_format(absolutefilepath, binary=True)
        kvs.name = Path(absolutefilepath).name
        return kvs

class FileKeyedVectors:

    def __init__(self, absolutefilepaths):
        self._absolutefilepaths=absolutefilepaths

    def __iter__(self) -> Iterator[KeyedVectors]:
        for absolutefilepath in self._absolutefilepaths:
            kvs = load_kvs(absolutefilepath)
            yield kvs
            
class KeyedVectorsDAO:

    def __init__(self):
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        basepath = "assets/corpora/embeddings"
        self._embeddingsfolderpath = os.path.join(location, basepath)

    def _get_absolute_path(self, filename:str) -> str:
        return os.path.join(self._embeddingsfolderpath, filename) 

    def get_models(self) -> FileKeyedVectors:
        absolutefilepaths=get_absolutefilepaths_ordered_by_size(self._embeddingsfolderpath, ".w2v")
        return FileKeyedVectors(absolutefilepaths)

    def get_model(self, name_id) -> FileKeyedVectors:
        absolutefilepath = os.path.join(self._embeddingsfolderpath, f"{name_id}")#.w2v
        return load_kvs(absolutefilepath)
