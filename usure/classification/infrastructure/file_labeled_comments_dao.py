import math
from typing import Iterable
from usure.classification.core import LabeledCommentsDao, LabeledComments, SentenceCleaner
from .intertass_xml_parser import InterTassXMLParser


class FileLabeledCommentsDao(LabeledCommentsDao):

    def __init__(self, folderpath:str, cleaner:SentenceCleaner):
        self._folderpath = folderpath
        self._cleaner = cleaner

    def get(self, name:str) -> LabeledComments:
        comments = self._get_from_xml(name)
        return comments

    def get_chunks(self, name, *percentages) -> Iterable[LabeledComments]:
        assert sum(percentages) == 100, "Arguments total must be 100%"
        comments = self._get_from_xml(name)
        chunk_sizes = list(map(lambda percentage: round(comments.count * percentage/100), percentages))
        if comments.count > sum(chunk_sizes):
            remainder =  comments.count - sum(chunk_sizes)
            chunk_sizes[-1] += remainder
        pivot = 0
        chunks = []
        for chunk_size in chunk_sizes:
            chunks.append(LabeledComments(comments.name, comments.comments[pivot:pivot+chunk_size], comments.labels[pivot:pivot+chunk_size]))
            pivot += chunk_size
        return chunks 

    def _get_from_xml(self, name):
        parser = InterTassXMLParser(self._folderpath, name, self._cleaner)
        return parser.get()