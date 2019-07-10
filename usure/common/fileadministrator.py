import os
from os import path
import re
from pathlib import Path


def get_filenames_ordered_by_size(absolutefolderpath:str, extension:str):
    dirnames = os.listdir(absolutefolderpath)
    filenames = [dirname for dirname in dirnames if path.isfile(path.join(absolutefolderpath, dirname))]
    filenames = [filename for filename in filenames if Path(filename).suffix == extension]
    filenames.sort(key = lambda filename: path.getsize(path.join(absolutefolderpath, filename)))
    return filenames

def get_absolutefilepaths_ordered_by_size(absolutefolderpath:str,extension:str):
    filenames = get_filenames_ordered_by_size(absolutefolderpath, extension)
    return [path.join(absolutefolderpath, filename) for filename in filenames]