import re
from .cleaner import Cleaner


class TwitterCorpusCleaner(Cleaner):

    def __init__(self):
        self.__id_pattern = re.compile("\"\d+\",")
        self.__quote_pattern = re.compile("\"\"")

    def clean(self, text: str) -> str:
        text = self.__id_pattern.sub("", text)
        #text = self.__quote_pattern.sub("", text)
        return text
