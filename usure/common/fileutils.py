import os
from os import path
import re
from pathlib import Path
from typing import Iterator, Tuple, Callable, Iterable


def get_filenames_ordered_by_size(absolutefolderpath: str, extensions: Iterable[str]):
    dirnames = os.listdir(absolutefolderpath)
    filenames = [dirname for dirname in dirnames if path.isfile(
        path.join(absolutefolderpath, dirname))]
    filenames = [filename for filename in filenames if Path(
        filename).suffix in extensions]
    filenames.sort(key=lambda filename: path.getsize(
        path.join(absolutefolderpath, filename)))
    return filenames


def get_absolutefilepaths_ordered_by_size(absolutefolderpath: str, extensions: Iterable[str]):
    filenames = get_filenames_ordered_by_size(absolutefolderpath, extensions)
    return [path.join(absolutefolderpath, filename) for filename in filenames]


def read_file(path, encoding) -> Iterator[str]:
    with open(path, encoding=encoding, errors='backslashreplace') as file:
        line = file.readline()
        while line:
            yield line
            line = file.readline()


def read_files(folderpath, extensions, encoding) -> Iterator[Tuple[str, Callable[[], Iterator[str]]]]:
    dirnames = os.listdir(folderpath)
    filenames = [dirname for dirname in dirnames if path.isfile(
        path.join(folderpath, dirname))]
    filenames = [filename for filename in filenames if Path(
        filename).suffix in extensions]
    filenames.sort(key=lambda filename: path.getsize(
        path.join(folderpath, filename)))
    for filename in filenames:
        yield filename, lambda: read_file(path.join(folderpath, filename), encoding)


def save_file(path, encoding, lines: Iterator[str]):
    with open(path, 'w', encoding=encoding) as file:
        file.write("\n".join(lines))
