import os
import re
from os import path
from pathlib import Path
from io import TextIOWrapper


class TrainingCorpusDAO:

    def __init__(self):
        self._basepath = "assets/corpora/preprocessed/"
        self._location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def get_trainingcorpora(self):
        dirfullpath = path.join(self._location, self._basepath)
        return FileTrainingCorpora(dirfullpath)


class FileTrainingCorpora:

    def __init__(self, folderpath): 
        self._folderpath = folderpath
        self._ignoreconvention = re.compile(".+\.ignore$")

    def __iter__(self):
        dirnames = os.listdir(self._folderpath)
        filenames = [dirname for dirname in dirnames if path.isfile(path.join(self._folderpath, dirname))]
        filenames = [filename for filename in filenames if not self._ignoreconvention.match(filename)]
        filenames.sort(key = lambda filename: path.getsize(path.join(self._folderpath, filename)))
        for filename in filenames:
            yield FileTrainingCorpus(Path(filename).stem, path.join(self._folderpath, filename))


class FileTrainingCorpus:

    def __init__(self, name:str, filepath:str):
        self._name = name
        self._filepath = filepath

    @property
    def name(self):
        return self._name

    def __iter__(self):
        with open(self._filepath, encoding="ascii") as file:
            line = file.readline()
            while line:
                yield line.split()
                line = file.readline()
