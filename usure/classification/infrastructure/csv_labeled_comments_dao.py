import math
import csv
from typing import Iterable
from usure.classification.core import LabeledCommentsDao, LabeledComments, SentenceCleaner
from .intertass_xml_parser import InterTassXMLParser
from usure.common import fileutils

class CsvLabeledCommentsDao(LabeledCommentsDao):

    def __init__(self, folderpath:str, cleaner:SentenceCleaner):
        self._folderpath = folderpath
        self._cleaner = cleaner

    def get(self, name:str) -> LabeledComments:
        path = fileutils.join(self._folderpath, name)
        comments = []
        labels = []
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                comments.append(self._cleaner.clean(row["text"])), 
                labels.append(row["polarity"])
        return LabeledComments(name, comments, labels)

    def save(self, labeled_comments:LabeledComments):
        path = fileutils.join(self._folderpath, labeled_comments.name)
        with open(path, "w") as f:
            writer = csv.DictWriter(f)
            for comment, label in zip(labeled_comments.comments, labeled_comments.labels):
                row = {"text":comment, "polarity":label}
                writer.writerow(row)

    def save_from_origin(self, labeled_comments : LabeledComments, origin_name):
        path = fileutils.join(self._folderpath, labeled_comments.name)
        path_origin = fileutils.join(self._folderpath, origin_name)
        ids = []
        with open(path_origin, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ids.append(row["id"]), 
        with open(path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "text", "polarity"])
            for id, comment, label in zip(ids, labeled_comments.comments, labeled_comments.labels):
                row = {"id": id, "text":comment, "polarity":label}
                writer.writerow(row)