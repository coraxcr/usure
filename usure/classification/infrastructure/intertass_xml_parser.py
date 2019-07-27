from usure.common import fileutils
from xml.etree import ElementTree as et
from usure.classification.core import LabeledComments, SentenceCleaner
from .basic_sentence_cleaner import BasicSentenceCleaner


class InterTassXMLParser:
    
    def __init__(self, folderpath, filename, cleaner:SentenceCleaner):
        self._name = filename
        self._xml = et.parse(fileutils.join(folderpath, filename)).getroot()
        self._cleaner = cleaner

    def get(self) -> LabeledComments:
        tweets = self._xml.findall("tweet")
        comments, labels = [], []
        for tweet in tweets:
            content = tweet.find("content").text
            content = self._cleaner.clean(content)
            comments.append(content)
            labels.append(tweet.find("./sentiment/polarity/value").text)
        return LabeledComments(self._name, comments, labels)