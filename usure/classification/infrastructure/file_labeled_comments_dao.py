from xml.etree import ElementTree as et
from usure.common import fileutils
from usure.classification.core import LabeledCommentsDao, LabeledComments


class FileLabeledCommentsDao(LabeledCommentsDao):

    def __init__(self, folderpath:str):
        self._folderpath = folderpath

    def get(self, name:str) -> LabeledComments:
        comments = self._get_from_xml(name)
        return comments

    def _get_from_xml(self, name):
        parser = InterTassXMLParser(self._folderpath, name)
        return parser.get()

class InterTassXMLParser:
    
    def __init__(self, folderpath, filename):
        self._name = filename
        self._xml = et.parse(fileutils.join(folderpath, filename)).getroot()

    def get(self):
        tweets = self._xml.findall("tweet")
        comments, labels = [], []
        for tweet in tweets:
            comments.append(tweet.find("content").text)
            labels.append(tweet.find("./sentiment/polarity/value").text)
        return LabeledComments(self._name, comments, labels)