import os
from os import path
from pathlib import Path
from typing import List, Callable, Iterable
from usure.preprocessing.core import Corpus, CorpusRep
from usure.common import fileutils


class FileCorpusRep(CorpusRep):

    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def get(self, name: str) -> Corpus:
        result = Corpus(name, lambda: fileutils.read_file(
            path.join(self.folder_path, name), "utf_8"))
        return result

    def get_all(self) -> Iterable[Corpus]:
        files = fileutils.read_files(
            self.folder_path, [".usu"], "utf_8")
        for name, get_corpus in files:
            yield Corpus(name, get_corpus)

    def save(self, corpus: Corpus):
        fullpath = path.join(self.folder_path, corpus.name)
        fileutils.save_file(fullpath, "utf_8", corpus.__iter__())
