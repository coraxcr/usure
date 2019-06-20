from usure.preprocessing.cleaning.cleaner import Cleaner
import re

class UrlCleaner(Cleaner):

    def __init__(self):
        self.__pattern = re.compile("(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})")

    def clean(self, text:str):
        result = self.__pattern.sub("", text)
        return result