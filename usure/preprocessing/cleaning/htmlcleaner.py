from usure.preprocessing.cleaning.cleaner import Cleaner
from gensim import utils
from bs4 import BeautifulSoup


class HtmlCleaner(Cleaner):

    def clean(self, text: str) -> str:
        result = self.__decode_htmlentities(text)
        result = self.__remove_htmltags(result)
        return result

    def __decode_htmlentities(self, text):
        return utils.decode_htmlentities(text)

    def __remove_htmltags(self, text):
        htlmprocesor = BeautifulSoup(text, features="html.parser")
        return htlmprocesor.get_text()
