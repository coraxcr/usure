import os
from os import path
from typing import Iterable
from gensim.models import KeyedVectors
from usure.common import fileutils


def load_kvs(path) -> KeyedVectors:
    kvs = KeyedVectors.load_word2vec_format(path, binary=True)
    kvs.name = Path(path).name
    return kvs

class FileKeyedVectorsRepository:
    
    def __init__(self, folderpath:str):
        self._folder_path =  folderpath

    def get(self, name:str) -> KeyedVectors:
        kvs = load_kvs(path.join(self._folder_path, name))
        kvs.name = name
        return kvs
    
    def get_all(self) -> Iterable[KeyedVectors]:
        file_names = fileutils.get_filenames_ordered_by_size(self._folder_path, [".kvs", ".bin"])
        return (self.get(file_name) for file_name in file_names)

    def save(self, kvs:KeyedVectors):
        filepath = path.join(self._folder_path, kvs.name)
        kvs.save_word2vec_format(filepath, binary=True)