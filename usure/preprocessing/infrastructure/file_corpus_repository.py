import os
from os import path
from pathlib import Path
from typing import List, Callable, Iterable
from usure.preprocessing.core import Corpus, CorpusRepository
from usure.common import fileutils

class FileCorpusRepository(CorpusRepository):

    def __init__(self, corpus_folder_path:str):
        self._corpus_folder_path = corpus_folder_path      

    def get(self, name:str) -> Corpus:
        result = Corpus(name, lambda: fileutils.read_file(path.join(self._corpus_folder_path, name), "utf_8"))
        return result
    
    def get_all(self) -> Iterable[Corpus]:
        files = fileutils.read_files(self._corpus_folder_path, [".txt", ".usu", ".xml"], "utf_8")
        for name, get_corpus in files:
            yield Corpus(name, get_corpus)

    def save(self, corpus:Corpus):
        fullpath = path.join(self._corpus_folder_path, corpus.name)
        fileutils.save_file(fullpath, "ascii", corpus.__iter__())