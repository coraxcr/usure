import math
from xml.etree import ElementTree as et
from typing import Iterable
from usure.common import fileutils
from usure.classification.core import LabeledCommentsDao, LabeledComments


class FileLabeledCommentsDao(LabeledCommentsDao):

    def __init__(self, folderpath:str):
        self._folderpath = folderpath

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
        parser = InterTassXMLParser(self._folderpath, name)
        return parser.get()

class InterTassXMLParser:
    
    def __init__(self, folderpath, filename):
        self._name = filename
        self._xml = et.parse(fileutils.join(folderpath, filename)).getroot()

    def get(self) -> LabeledComments:
        tweets = self._xml.findall("tweet")
        comments, labels = [], []
        for tweet in tweets:
            comments.append(tweet.find("content").text)
            labels.append(tweet.find("./sentiment/polarity/value").text)
        return LabeledComments(self._name, comments, labels)