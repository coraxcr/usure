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

    def save(self, labeled_comments:LabeledComments):
        raise NotImplementedError()

    def save_from_origin(self, labeled_comments : LabeledComments, origin_name):
        parser = InterTassXMLParser(self._folderpath, origin_name, self._cleaner)
        xml = parser.change_polarity_value(labeled_comments.labels)
        parser.save(self._folderpath, labeled_comments.name, xml)

    def _get_from_xml(self, name):
        parser = InterTassXMLParser(self._folderpath, name, self._cleaner)
        return parser.get()