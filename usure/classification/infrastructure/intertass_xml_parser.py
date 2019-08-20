from typing import Iterable
from usure.common import fileutils
from xml.etree import ElementTree as et
from usure.classification.core import LabeledComments, SentenceCleaner
from .basic_sentence_cleaner import BasicSentenceCleaner


class InterTassXMLParser:
    
    def __init__(self, folderpath, filename, cleaner:SentenceCleaner):
        self._name = filename
        self._xml = et.parse(fileutils.join(folderpath, filename))
        self._cleaner = cleaner

    def get(self) -> LabeledComments:
        tweets = self._xml.getroot().findall("tweet")
        comments, labels = [], []
        for tweet in tweets:
            content = tweet.find("content").text
            content = self._cleaner.clean(content)
            comments.append(content)
            labels.append(tweet.find("./sentiment/polarity/value").text)
        return LabeledComments(self._name, comments, labels)

    def change_polarity_value(self, labels:Iterable[str]):
        tweets = self._xml.getroot().findall("tweet")
        for i, tweet in enumerate(tweets):
            tweet.find("./sentiment/polarity/value").text = labels[i]
        return self._xml

    def save(self, folderpath, filename, xml):
        path = fileutils.join(folderpath, filename)
        xml.write(path)
                 