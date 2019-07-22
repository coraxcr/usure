from os import path
from typing import Iterable
from gensim.models import Word2Vec
from pathlib import Path
from usure.common import fileutils

def load_w2v(path) -> Word2Vec:
    w2v = Word2Vec.load(path)
    w2v.name = Path(path).name
    return w2v


class FileWord2VecRep:

    def __init__(self, folderpath: str):
        self._folder_path = folderpath

    def get(self, name: str) -> Word2Vec:
        w2v = load_w2v(path.join(self._folder_path, name))
        w2v.name = name
        return w2v

    def get_all(self) -> Iterable[Word2Vec]:
        file_names = fileutils.get_filenames_ordered_by_size(
            self._folder_path, [".w2v"])
        return (self.get(file_name) for file_name in file_names)

    def save(self, w2v: Word2Vec):
        filepath = path.join(self._folder_path, w2v.name)
        w2v.save(filepath)
